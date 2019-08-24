from pytrends.request import TrendReq
import pandas as pd
from pandas import ExcelWriter
import csv


pytrends = TrendReq(hl='en-US', tz=360, timeout=(10,25))

kw_list = ["VR Game"]

'''
#searching related queries
pytrends.build_payload(kw_list, cat=0, timeframe='2017-07-01 2018-07-29', geo='US', gprop='')
related_queries = pytrends.related_queries()[str(kw_list[0])]['top']
'''

#getting hourly interest (relative value for the maximum searched item
historical_hourly_interest = \
    pytrends.get_historical_interest(kw_list, year_start=2018, month_start=1,
                                     day_start=1, hour_start=0, year_end=2018,
                                     month_end=1, day_end=10, hour_end=0, cat=0,
                                     geo='US', gprop='', sleep=0)

#data type pandas.core.frame.DataFrame
#print(historical_hourly_interest)

#converting index of pandas dataframe into column
#reset_index() for integer index
#reset.index().set_index for date values index
#print(df.reset_index().set_index('date', drop=False))

df = historical_hourly_interest
df_without_index = df.reset_index()
print(df_without_index)
# df_without_index.to_csv(index=False)
df_without_index.to_csv(r'C:/Users/pc/Documents/GitHub/VR_Trend_teller/'+kw_list[0]+'.csv',index=False)


'''
#setting file name
file_name = "related queries about " + kw_list[0]
writer = ExcelWriter(file_name+'.xlsx')
#Write on excel using pandas writer
historical_hourly_interest.to_excel(writer,'sheet1',index=False)
writer.save()
'''



