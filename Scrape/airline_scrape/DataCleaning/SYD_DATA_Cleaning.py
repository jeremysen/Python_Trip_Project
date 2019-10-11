"""
@Description: This file is to clean the Guangzhou to Sydney flight data
@Author:      Liyuan Gu
@Time:        2019-10-03
"""

import pandas as pd

FlightData = pd.read_excel('AirlineData_SYD.xlsx')

# To change the IATA code to common language.
FlightData['DepartureAirport'].replace(
    {'CAN T2': 'Guangzhou Baiyun Airport T2', 'CAN T1': 'Guangzhou Baiyun Airport T1'}, inplace=True)
del FlightData['TransferAirport']
FlightData['ArrivalAirport'].replace(
    {'SYD\xa0T1': 'Sydney Kingsford Smith Airport T1', 'SYD': 'Sydney Kingsford Smith Airport'}, inplace=True)
FlightData['Price'] = FlightData["Price"].str[3:]
DepartureLatitude = []
DepartureLongitude = []
ArrivalLatitude = []
ArrivalLongitude = []
for i in range(len(FlightData)):
    DepartureLatitude.append('23.3959128')
    DepartureLongitude.append('113.3057812')
    ArrivalLatitude.append('-33.9399183')
    ArrivalLongitude.append('151.1730877')
FlightData.insert(3, 'DepartureLatitude', DepartureLatitude)
FlightData.insert(4, 'DepartureLongitude', DepartureLongitude)
FlightData.insert(7, 'ArrivalLatitude', ArrivalLatitude)
FlightData.insert(8, 'ArrivalLongitude', ArrivalLongitude)
FlightData.to_excel('AirlineData_SYD_cleaned.xlsx', index=None)
