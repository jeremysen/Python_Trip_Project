# -*- coding: utf-8 -*-

'''
@Description: This file is used to generate suitable service for customer
@Author:      Shanyue
@Time:        2019-10-02
'''

import pandas as pd

def add_range_air(price,air_down,air_up):
    '''
    Add range for air line
    :param price: price in df
    :param air_down: air_down
    :param air_up: air_up
    :return: whether in range
    '''
    price = int(price)
    if(price<=(int)(air_up) and price>=(int)(air_down)):
        return 1
    else:
        return 0

def get_suitable_hotel(city, mode):
    '''
    Get suitable hotel based on mode
    :param city: city
    :param mode: mode of customer
    :return: hotel series
    '''
    hotel = pd.read_csv("dataset/hotel_data.csv")
    hotel_city = hotel[(hotel["city"]==city) & (hotel["rate"] == "Excellent ")]
    if(len(hotel_city) == 0):
        hotel_city = hotel[(hotel["city"]==city) & (hotel["rate"] == "Very good ")]
    hotel_city = hotel_city.sort_values(by="price", ascending=True).reset_index(drop=True)
    if(mode=="Economy"):
        return list(hotel_city.iloc[0])[2], list(hotel_city.iloc[0])[6]
    else:
        return list(hotel_city.iloc[60])[2], list(hotel_city.iloc[60])[6]
    

def get_suitable_airline(city, air_down, air_up):
    '''
    Get suitable airline
    :param city: city
    :param air_down: air_down
    :param air_up: air_up
    :return: airline series
    '''
    airline = pd.read_excel("dataset/airline_data.xlsx")
    airline_city = airline[(airline["ArrivalAirport"].str.contains(city))]
    airline_city = airline_city[~airline_city["Price"].isna()]
    airline_city["Price"] = airline_city["Price"].astype(int)
    airline_city["price_within"] = airline_city["Price"].apply(lambda x:add_range_air(x,air_down,air_up))
    airline_city = airline_city[airline_city["price_within"] == 1]
    airline_city = airline_city.sort_values(by="Price", ascending=True).reset_index(drop=True)
    return list(airline_city.iloc[0])[5], list(airline_city.iloc[0])[10], list(airline_city.iloc[0])


if(__name__=="__main__"):
    suitable_hotel, hotel_price = get_suitable_hotel("Adelaide")
    