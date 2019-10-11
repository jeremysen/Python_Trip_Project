"""
@Description: This file is to write all raw data into one Excel file
@Author:      Liyuan Gu
@Time:        2019-10-02
"""
import pandas as pd

df1 = pd.read_excel('AirlineData_MEL.xlsx')
df2 = pd.read_excel('AirlineData_SYD.xlsx')
df3 = pd.read_excel('AirlineData_BNE.xlsx')
df4 = pd.read_excel('AirlineData_CBR.xlsx')
df5 = pd.read_excel('AirlineData_ADL.xlsx')
frames = [df1, df2, df3, df4, df5]
rawData = pd.concat(frames)
rawData.to_excel('AirlineRawData.xlsx', index=None)

df6 = pd.read_excel('AirlineData_MEL_cleaned.xlsx')
df7 = pd.read_excel('AirlineData_SYD_cleaned.xlsx')
df8 = pd.read_excel('AirlineData_BNE_cleaned.xlsx')
df9 = pd.read_excel('AirlineData_CBR_cleaned.xlsx')
df10 = pd.read_excel('AirlineData_ADL_cleaned.xlsx')
frames2 = [df6, df7, df8, df9, df10]
cleanedData = pd.concat(frames2)
cleanedData.to_excel('AirlineCleanedData.xlsx', index=None)