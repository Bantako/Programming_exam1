# Programming_exam1
プログラム試験問題の回答
現在問３まで実装済み
本プログラムはPython3とpandasを使用

# Requirement
  
* Python 3.8.10
* pandas 1.2.4
* numpy 1.20.2
 
# Usage
  
```bash
$ git clone https://github.com/Bantako/Programming_exam1.git
$ cd Programming_exam1
$ python main.py
```

本プログラムはコマンドライン引数でオプションを指定できる
| option | description |
| -- | -- |
| problem | 問題番号 １－３まで対応 |
| file | 実行ファイル |
| N,m,t | パラメータ |

# Description
本プログラムはcsvファイルからデータを読みとり，故障期間・過負荷期間を出力する．
故障期間・過負荷期間は以下のように出力される

```
$ python3 main.py --problem 3 --N 1 --m 1 --t 10 --file ./log/log3.csv
                  date address time
0  2020-10-19 13:00:10       a    1
1  2020-10-19 13:01:10       a    3
2  2020-10-19 13:02:10       a    3
3  2020-10-19 13:03:10       a  100
4  2020-10-19 13:04:10       a    4
5  2020-10-19 13:05:10       a    2
6  2020-10-19 13:06:10       a    6
7  2020-10-19 13:07:10       a    -
8  2020-10-19 13:08:10       a  500
9  2020-10-19 13:09:10       a  200
10 2020-10-19 13:10:10       a  300
address: a
                  date address time
0  2020-10-19 13:00:10       a    1
1  2020-10-19 13:01:10       a    3
2  2020-10-19 13:02:10       a    3
3  2020-10-19 13:03:10       a  100
4  2020-10-19 13:04:10       a    4
5  2020-10-19 13:05:10       a    2
6  2020-10-19 13:06:10       a    6
7  2020-10-19 13:07:10       a    -
8  2020-10-19 13:08:10       a  500
9  2020-10-19 13:09:10       a  200
10 2020-10-19 13:10:10       a  300

  address   failure_starttime  failure_period
8       a 2020-10-19 13:07:10 0 days 00:01:00
  address  overload_starttime overload_period
4       a 2020-10-19 13:03:10 0 days 00:01:00
```
addressは当該IPアドレス，failure_starttimeは故障開始時間，failure_periodは故障期間を表す．
同様に，overload_starttimeは過負荷開始時間，overload_periodは過負荷期間を表す．

# Test
以下に作成したテストケースとその実行結果を示す．
``` log1.csv
20201019133124,10.20.30.1/16,2
20201019133125,10.20.30.2/16,1
20201019133134,192.168.1.1/24,10
20201019133135,192.168.1.2/24,5
20201019133224,10.20.30.1/16,522
20201019133225,10.20.30.2/16,1
20201019133234,192.168.1.1/24,8
20201019133235,192.168.1.2/24,15
20201019133324,10.20.30.1/16,-
20201019133325,10.20.30.2/16,2
```

```python3 main.py --problem 1 --file ./log/log1.csv
                 date         address time
0 2020-10-19 13:31:24   10.20.30.1/16    2
4 2020-10-19 13:32:24   10.20.30.1/16  522
8 2020-10-19 13:33:24   10.20.30.1/16    -
1 2020-10-19 13:31:25   10.20.30.2/16    1
5 2020-10-19 13:32:25   10.20.30.2/16    1
9 2020-10-19 13:33:25   10.20.30.2/16    2
2 2020-10-19 13:31:34  192.168.1.1/24   10
6 2020-10-19 13:32:34  192.168.1.1/24    8
3 2020-10-19 13:31:35  192.168.1.2/24    5
7 2020-10-19 13:32:35  192.168.1.2/24   15
address: 10.20.30.1/16
                 date        address time
0 2020-10-19 13:31:24  10.20.30.1/16    2
4 2020-10-19 13:32:24  10.20.30.1/16  522
8 2020-10-19 13:33:24  10.20.30.1/16    -

address: 10.20.30.2/16
                 date        address time
1 2020-10-19 13:31:25  10.20.30.2/16    1
5 2020-10-19 13:32:25  10.20.30.2/16    1
9 2020-10-19 13:33:25  10.20.30.2/16    2

address: 192.168.1.1/24
                 date         address time
2 2020-10-19 13:31:34  192.168.1.1/24   10
6 2020-10-19 13:32:34  192.168.1.1/24    8

address: 192.168.1.2/24
                 date         address time
3 2020-10-19 13:31:35  192.168.1.2/24    5
7 2020-10-19 13:32:35  192.168.1.2/24   15

         address   failure_starttime failure_period
3  10.20.30.1/16 2020-10-19 13:33:24         0 days
```

```log2.csv
20201019130010,a,1
20201019130110,a,-
20201019130210,a,3
20201019130310,a,-
20201019130410,a,-
20201019130510,a,2
20201019130610,a,2
20201019130710,a,-
20201019130810,a,-
20201019130910,a,-
20201019131010,a,3
```

``` python3 main.py --problem 2 --N 2 --file ./log/log2.csv
                  date address time
0  2020-10-19 13:00:10       a    1
1  2020-10-19 13:01:10       a    -
2  2020-10-19 13:02:10       a    3
3  2020-10-19 13:03:10       a    -
4  2020-10-19 13:04:10       a    -
5  2020-10-19 13:05:10       a    2
6  2020-10-19 13:06:10       a    2
7  2020-10-19 13:07:10       a    -
8  2020-10-19 13:08:10       a    -
9  2020-10-19 13:09:10       a    -
10 2020-10-19 13:10:10       a    3
address: a
                  date address time
0  2020-10-19 13:00:10       a    1
1  2020-10-19 13:01:10       a    -
2  2020-10-19 13:02:10       a    3
3  2020-10-19 13:03:10       a    -
4  2020-10-19 13:04:10       a    -
5  2020-10-19 13:05:10       a    2
6  2020-10-19 13:06:10       a    2
7  2020-10-19 13:07:10       a    -
8  2020-10-19 13:08:10       a    -
9  2020-10-19 13:09:10       a    -
10 2020-10-19 13:10:10       a    3

   address   failure_starttime  failure_period
5        a 2020-10-19 13:03:10 0 days 00:02:00
10       a 2020-10-19 13:07:10 0 days 00:03:00
```

```log3.csv
20201019130010,a,1
20201019130110,a,3
20201019130210,a,3
20201019130310,a,100
20201019130410,a,4
20201019130510,a,2
20201019130610,a,6
20201019130710,a,-
20201019130810,a,500
20201019130910,a,200
20201019131010,a,300
```

```python3 main.py --problem 3 --N 1 --m 2 --t 10 --file ./log/log3.csv
                  date address time
0  2020-10-19 13:00:10       a    1
1  2020-10-19 13:01:10       a    3
2  2020-10-19 13:02:10       a    3
3  2020-10-19 13:03:10       a  100
4  2020-10-19 13:04:10       a    4
5  2020-10-19 13:05:10       a    2
6  2020-10-19 13:06:10       a    6
7  2020-10-19 13:07:10       a    -
8  2020-10-19 13:08:10       a  500
9  2020-10-19 13:09:10       a  200
10 2020-10-19 13:10:10       a  300
address: a
                  date address time
0  2020-10-19 13:00:10       a    1
1  2020-10-19 13:01:10       a    3
2  2020-10-19 13:02:10       a    3
3  2020-10-19 13:03:10       a  100
4  2020-10-19 13:04:10       a    4
5  2020-10-19 13:05:10       a    2
6  2020-10-19 13:06:10       a    6
7  2020-10-19 13:07:10       a    -
8  2020-10-19 13:08:10       a  500
9  2020-10-19 13:09:10       a  200
10 2020-10-19 13:10:10       a  300

  address   failure_starttime  failure_period
8       a 2020-10-19 13:07:10 0 days 00:01:00
  address   overload_starttime overload_period
5       a  2020-10-19 13:03:10 0 days 00:02:00
```
