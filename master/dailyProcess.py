from subprocess import call

call(["python", "dailyStream.py", "EUR_USD", "--granularity", "D", "--from-time", "2017-05-27 00:00:00"])

#call(["python", "dailyCandles.py", "EUR/USD", "--granularity", "D"])