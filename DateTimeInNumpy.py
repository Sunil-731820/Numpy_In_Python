import numpy as np
today = np.datetime64("2022-05-17")
print("the today date is",today)
print("the year from the given date is ")
print(np.datetime64(today,'Y'))

#creating the array of the dates in the months
date = np.arange('2017-02','2017-03',dtype='datetime64[D]')
print("the dates are")
print(date)

#again printing the date of the months 
dates = np.arange('2022-05','2022-06',dtype='datetime64[D]')
print("the dates are")
print(dates)
