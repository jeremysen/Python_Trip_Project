#coding: utf-8
'''
@Description: This file is to provide scraping website
@Author:      Yuou
@Time:        2019-10-01
'''
from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import DataFrame
import numpy as np


# Website url
url1 = "https://www.trivago.com.au/"
url3 = "&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0" \
      "&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2" \
      "&cpt2="
url4 = "%2F200" \
      "&iViewType=0&bIsSeoPage=0&sortingId=1" \
      "&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode="
url5 = "&offset=0&ra="
location=['25057','25061','25059','54568','25058']
url2 =  '?aDateRange%5Barr%5D=2019-11-01&aDateRange%5Bdep%5D=2019-11-02'

urllist = []

# Worming function
def Worm(bsyc,loc):
    ''''''
    result=[]
    for k in bsyc.findAll('div', {'class': 'pos-relative item__wrapper'}):
        print('1111')
        info = []
        info.append(loc)
        info.append(k.find('span', {'class': 'item-link name__copytext'}).a.string)
        info.append(k.find('spac', {'class': 'item-components__pillValue--738db item-components__value-sm--226ff item-components__pillValue--738db'}).string) \
            if k.find('span', {'class': 'item-components__pillValue--738db item-components__value-sm--226ff item-components__pillValue--738db'}) \
            else info.append("")#rate
        info.append(k.find('span', {'class': 'item__accommodation-type'}).string) if k.find('span', {
            'class': 'item__accommodation-type'}) else info.append("")#type
        info.append(k.find('p', {'class': 'details-paragraph details-paragraph--location location-details'}).string) if k.find('p', {
            'class': 'details-paragraph details-paragraph--location location-details'}) else info.append("")#location
        info.append(k.find('strong',{'class':"item__best-price price_min"}).string
                    if k.find('strong',{'class':"item__best-price price_min"}) else info.append(""))
        print(info)
        result.append(info)
    return result

raw_data=[]
for loc in location:
    for date in range(29):
        list2 = list(url2)
        list2[29] = (date+1)//10
        list2[30] = (date+1)%10
        list2[60] = (date+2)//10
        list2[61] = (date+2)%10
        print(list2)
        url2 = ''.join('%s' %id for id in list2)
        url = url1+url2+url3+loc+url4+url5
        while(int(list(url)[-5])<1):
            print(url)
            browser = webdriver.Chrome('chromedriver')
            browser.get(url)
            # Locker waiting for loading
            browser.implicitly_wait(90)
            browser.find_element_by_class_name("item__flex-column")
            html = browser.page_source
            bsyc = BeautifulSoup(html, "html.parser")
            fout = open('bsyc_temp.txt', 'wt',
                        encoding='utf-8')
            urllist.append(url)

            for k in bsyc.findAll('div', {'class': 'item__flex-column'}):
                info = []
                info.append(loc)
                info.append(url2[29:31]+"-"+url2[60:62])
                info.append(k.find('span', {'class': 'item-link name__copytext'}).string)
                info.append(k.find('strong', {
                    'class': 'item__rating-number'}).string) \
                    if k.find('strong', {
                    'class': 'item__rating-number'}) \
                    else info.append("")  # rate
                info.append(k.find('span', {'class': 'item__accommodation-type'}).string) if k.find('span', {
                    'class': 'item__accommodation-type'}) else info.append("")  # type
                info.append(k.find('p', {
                    'class': 'details-paragraph details-paragraph--location location-details'}).string) if k.find(
                    'p', {
                        'class': 'details-paragraph details-paragraph--location location-details'}) else info.append(
                    "")  # location
                info.append(k.find('strong', {'class': "item__best-price price_min"}).string
                            if k.find('strong', {'class': "item__best-price price_min"}) else info.append(""))
                raw_data.append(info)

            temp = list(url)
            offset = int(temp[-5])
            offset += 1
            temp[-5] = str(offset)
            url = ''.join(temp)
            data = np.array(raw_data)
            df = DataFrame(data, columns=["city", "time", "name", "rate", "type", "location", "price"])
            if loc == "25057":
                df.to_csv("raw_data_hotel_SD.csv", index=False)
            elif loc == "25061":
                df.to_csv("raw_data_hotel_MEL.csv", index=False)
            elif loc == "25059":
                df.to_csv("raw_data_hotel_AD.csv", index=False)
            elif loc == "54568":
                df.to_csv("raw_data_hotel_CAN.csv", index=False)
            elif loc == "25058":
                df.to_csv("raw_data_hotel_BR.csv", index=False)