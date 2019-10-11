"""
@Description: This file is to clean the Guangzhou to Brisbane flight data
@Author:      Liyuan Gu
@Time:        2019-10-03
"""

import pandas as pd

FlightData = pd.read_excel('AirlineData_BNE.xlsx')

# To change the IATA code to common language.
FlightData['DepartureAirport'].replace(
    {'CAN T2': 'Guangzhou Baiyun Airport T2', 'CAN T1': 'Guangzhou Baiyun Airport T1'}, inplace=True)
del FlightData['TransferAirport']
FlightData['ArrivalAirport'].replace(
    {'BNE\xa0D': 'Brisbane Airport D', 'BNE\xa0I': 'Brisbane Airport I', 'BNE': 'Brisbane Airport'}, inplace=True)
FlightData['Price'] = FlightData["Price"].str[3:]
DepartureLatitude = []
DepartureLongitude = []
ArrivalLatitude = []
ArrivalLongitude = []
for i in range(len(FlightData)):
    DepartureLatitude.append('23.3959128')
    DepartureLongitude.append('113.3057812')
    ArrivalLatitude.append('-27.3942096')
    ArrivalLongitude.append('153.1196416')
FlightData.insert(3, 'DepartureLatitude', DepartureLatitude)
FlightData.insert(4, 'DepartureLongitude', DepartureLongitude)
FlightData.insert(7, 'ArrivalLatitude', ArrivalLatitude)
FlightData.insert(8, 'ArrivalLongitude', ArrivalLongitude)
FlightData.to_excel('AirlineData_BNE_cleaned.xlsx', index=None)
