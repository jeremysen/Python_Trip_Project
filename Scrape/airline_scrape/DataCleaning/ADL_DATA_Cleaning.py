"""
@Description: This file is to clean the Guangzhou to Adelaide flight data
@Author:      Liyuan Gu
@Time:        2019-10-03
"""

import pandas as pd

AdlFlightData = pd.read_excel('AirlineData_ADL.xlsx')
# To change the IATA code to common language.
AdlFlightData['DepartureAirport'].replace(
    {'CAN T2': 'Guangzhou Baiyun Airport T2', 'CAN T1': 'Guangzhou Baiyun Airport T1'}, inplace=True)
del AdlFlightData['TransferAirport']
AdlFlightData['ArrivalAirport'].replace(
    {'ADL\xa0T1': 'Adelaide Airport T1', 'ADL': 'Adelaide Airport'}, inplace=True)
AdlFlightData['Price'] = AdlFlightData["Price"].str[3:]
DepartureLatitude = []
DepartureLongitude = []
ArrivalLatitude = []
ArrivalLongitude = []
for i in range(len(AdlFlightData)):
    DepartureLatitude.append('23.3959128')
    DepartureLongitude.append('113.3057812')
    ArrivalLatitude.append('-34.9461513')
    ArrivalLongitude.append('138.5310491')
AdlFlightData.insert(3, 'DepartureLatitude', DepartureLatitude)
AdlFlightData.insert(4, 'DepartureLongitude', DepartureLongitude)
AdlFlightData.insert(7, 'ArrivalLatitude', ArrivalLatitude)
AdlFlightData.insert(8, 'ArrivalLongitude', ArrivalLongitude)
AdlFlightData.to_excel('AirlineData_ADL_cleaned.xlsx', index=None)
