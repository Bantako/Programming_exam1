import csv
import pandas as pd
import numpy as np
import warnings

TIMEOUT = 4000 
warnings.simplefilter('ignore')

# https://algorithm.joho.info/programming/python/count-continuous-values/
# 連続した欠損値の値を数える
def count_continuous_values(df, column_name, time=TIMEOUT):
    y = df[column_name].replace("-", TIMEOUT).astype("int64")
    df[column_name+ "_counum"] = y.groupby((y < time).cumsum()).cumcount()
    return df
 
def get_failure_time(df, N=2):
    df = df.append(df.tail(1))
    df = df.reset_index(drop=True)
    df.iat[-1, 2] = 0
    df = count_continuous_values(df, 'time')

    df['failure_time'] = pd.NaT
    df.at[0, 'failure_time'] = "19700101000000" # 番兵
    df.loc[df['time_counum'] == 1, 'failure_time'] = df['date']
    df['failure_time'].ffill(inplace=True)
    index = (df['time_counum'] == 0) & (df['time_counum'].shift(1) >= N)
    sub_time = df[index]['date'] - df[index]['failure_time']
    # print(sub_time)
    address = df[index]['address']
    return pd.DataFrame({'address': address, 'failure_starttime': df[index]['failure_time'], 'failure_period': sub_time})

def add_average_time(df, m=3):
    hoge = df['time'].replace("-", -TIMEOUT * m)
    average_time = hoge.rolling(m).mean()
    df["average_time"] = average_time
    return df

def get_overload_time(df, m=3, t=10):
    df = add_average_time(df, m)
    df = count_continuous_values(df[m-1:].copy(), "average_time", time=t)
    print(df)
    df['failure_time'] = pd.NaT
    df.at[0, 'failure_time'] = "19700101000000" # 番兵
    df.loc[df['average_time_counum'] == 1, 'failure_time'] = df['date']
    df['failure_time'].ffill(inplace=True)
    
    index = (df['average_time_counum'] == 0) & (df['average_time_counum'].shift(1) >= 1)
    print(df[index]['date'])
    print(df[index]['failure_time'])
    sub_time = df[index]['date'] - df[index]['failure_time']
    print(sub_time)
    address = df[index]['address']
    return pd.DataFrame({'address': address, 'overload_starttime': df[index]['failure_time'], 'overload_period': sub_time})




# example

def problem1(df):
    failure_df = pd.DataFrame({'address':[], 'failure_starttime': [], 'failure_period': []})
    for address, sdf in df.groupby('address'):
        print('address:', address)
        print(sdf, end="\n\n")

        fdf = get_failure_time(sdf, N=1)
        failure_df = failure_df.append(fdf)
    
    print(failure_df)

def problem2(df, N=2):
    failure_df = pd.DataFrame({'address':[], 'failure_starttime': [], 'failure_period': []})
    for address, sdf in df.groupby('address'):
        print('address:', address)
        print(sdf, end="\n\n")

        fdf = get_failure_time(sdf, N)
        failure_df = failure_df.append(fdf)
    
    print(failure_df)

def problem3(df, N=2, m=3, t=10):
    failure_df = pd.DataFrame({'address':[], 'failure_starttime': [], 'failure_period': []})
    overload_df = pd.DataFrame({'address': [], 'overload_starttime': [], 'overload_period': []})

    for address, sdf in df.groupby('address'):
        print('address:', address)
        print(sdf, end="\n\n")

        fdf = get_failure_time(sdf, N)
        failure_df = failure_df.append(fdf)
        odf = get_overload_time(sdf, m, t)
        overload_df = overload_df.append(odf)
    
    print(failure_df)
    print(overload_df)

if __name__ == '__main__':
    filepath = './log/log3.csv'
    # date = 'YYYYMMDDhhmmss'
    df = pd.read_csv(filepath, names=('date', 'address', 'time'), parse_dates=['date'])       
    # pd.to_datetime(df['date'], format="%Y%m%d%H%M%S")
    df = df.sort_values(['address', 'date'])
    print(df)

    # problem1(df)
    # problem2(df, N=2)
    problem3(df, N=2, m=3, t=10)

'''
    for address, sdf in df.groupby('address'):
        print('address:', address)
        print(sdf)
        print()

        count_continuous_values(sdf, 'time')
        print(sdf)
        print()

        df2 = get_overload_time(sdf)
        print(df2)

        add_failure_time(sdf)
        print(sdf)

        df2 = get_failure_time(sdf, 1)
        print(df2)
'''