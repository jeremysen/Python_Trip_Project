"""
@Description: This file is to clean the Guangzhou to Melbourne flight data
@Author:      Liyuan Gu
@Time:        2019-10-03
"""

import pandas as pd

MelFlightData = pd.read_excel('AirlineData_MEL.xlsx')
MelFlightData['DepartureAirport'].replace(
    {'CAN T2': 'Guangzhou Baiyun Airport T2', 'CAN T1': 'Guangzhou Baiyun Airport T1'}, inplace=True)

del MelFlightData['TransferAirport']
# To change the IATA code to common language.
MelFlightData['ArrivalAirport'].replace(
    {'MEL\xa0T2': 'Melbourne Airport T2', 'MEL': 'Melbourne Airport', 'AVV': 'Melbourne Avalon Airport'}, inplace=True)
MelFlightData['Price'] = MelFlightData["Price"].str[3:]
DepartureLatitude = []
DepartureLongitude = []
ArrivalLatitude = []
ArrivalLongitude = []
for i in range(len(MelFlightData)):
    DepartureLatitude.append('23.3959128')
    DepartureLongitude.append('113.3057812')
    if MelFlightData['ArrivalAirport'][i] is 'Melbourne Avalon Airport':
        ArrivalLatitude.append('-38.0267645')
        ArrivalLongitude.append('144.4710507')
    else:
        ArrivalLatitude.append('-37.669008')
        ArrivalLongitude.append('144.8388386')
MelFlightData.insert(3, 'DepartureLatitude', DepartureLatitude)
MelFlightData.insert(4, 'DepartureLongitude', DepartureLongitude)
MelFlightData.insert(7, 'ArrivalLatitude', ArrivalLatitude)
MelFlightData.insert(8, 'ArrivalLongitude', ArrivalLongitude)
MelFlightData.to_excel('AirlineData_MEL_cleaned.xlsx', index=None)
