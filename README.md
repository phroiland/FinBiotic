# FinBiotic

**FinBiotic** _is a python wrapper program that takes in streaming Forex data; computes breakouts, pivot points, 
and position sizes to execute trades on the [Oanda](https://www.oanda.com/) trading platform._

    user@host:~$ git clone https://github.com/phroiland/FinBiotic.git

**Setup Virtual Environment**
```
user@host:~$ cd FinBiotic

user@host:~/FinBiotic$ virtualenv finbiotic

user@host:~/FinBiotic$ source finbiotic/bin/activate
```
**Required Modules**
(_will eventually automate this with a package manager or requirements.txt file_)

    (finbiotic) user@host:~/FinBiotic$ pip install oandapyV20 pyyaml v20 pandas tabulate

**Generating v20 Configuration File**

_v20 configuration files may be generated manually, 
however a script is provided that will generate one interactively located at app/configure.py._

To run it and generate a v20 configuration file, simply run:

    (finbiotic) user@host:~/FinBiotic$ v20-configure

and follow the instructions.

**Set Environment Variables**
```
(finbiotic) user@host:~/FinBiotic$ export V20_CONF=/path/to/.v20.conf

(finbiotic) user@host:~/FinBiotic$ export OANDA_API_ACCESS_TOKEN=123456789qwerty-987654321poiuy

(finbiotic) user@host:~/FinBiotic$ export OANDA_API_ACCOUNT_ID=yourID

(finbiotic) user@host:~/FinBiotic$ export CSV_DIR=/path/to/csv/files (i.e., /home/user/csv)
```
**Get Pivot Point, Resistance, and Support Levels**

    (finbiotic) user@host:~/FinBiotic$ python daily/dailyStream.py EUR_USD --granularity D 

(_default granularity is H1_)

**Run the Application**

    (finbiotic) user@host:~/FinBiotic$ python app/master.py -i EUR_USD

**Tips & Tricks**

* In **daily/dailyStream.py** 
    * change output csv to respective granularity

* In **app/master.py** 
    * change StreamingData() resample string parameter to various time intervals:
        * **'5min'**
        * **'1s'**
        * etc.

* Review Oanda API docs for further info on interacting with the API