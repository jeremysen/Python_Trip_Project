"""
@Description: This file is to scrap flight information (from Guangzhou to Brisbane) from Trip.com
@Author:      Liyuan Gu
@Time:        2019-10-02
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import ssl
import xlsxwriter
import datetime
import time

def datelist(start, end):
    """

    :param start:
    :param end:
    :return:
    """
    start_date = datetime.date(*start)
    end_date = datetime.date(*end)

    result = []
    curr_date = start_date
    while curr_date != end_date:
        result.append("%04d-%02d-%02d" % (curr_date.year, curr_date.month, curr_date.day))
        curr_date += datetime.timedelta(1)
    result.append("%04d-%02d-%02d" % (curr_date.year, curr_date.month, curr_date.day))
    return result


Airline = []
FlightNo = []
DepartureAirport = []
ArrivalAirport = []
TransferAirport = []
DepartureTime = []
ArrivalTime = []
Price = []
browser = []
html = []
body = []
FlightDate = []
date = datelist((2019, 11, 1), (2019, 11, 30))
pattern1 = 'https://au.trip.com/flights/guangzhou-to-brisbane/tickets-can-bne/?flighttype=s&dcity=can&acity=bne&startdate='
pattern2 = '&class=ys&quantity=1&searchboxarg=t.html'
for i in date:
    pattern = pattern1 + i + pattern2
    ssl._create_default_https_context = ssl._create_unverified_context
    # Access to the url by using Chrome
    browser = webdriver.Chrome('chromedriver')
    browser.get(pattern)
    time.sleep(5)  # control the process time
    html = browser.page_source
    body = BeautifulSoup(html, "html.parser")
    # print(soup.prettify())

    for a in body.findAll('div', {'class': 'name c-result-airline__name'}):
        Airline.append(a.text)
        FlightDate.append(i)
    for b in body.findAll('div', {'class': 'c-result-airline__wrap'}):
        flightNo = ''
        for p in b.findAll('span', {'class': 'flightNo'}):
            flightNo += p.text + ' '
        FlightNo.append(flightNo)
    for c in body.findAll('div', {'class': 'c-result-period__depart'}):
        for q in c.findAll('div', {'class': 'bod-bottom-dotted'}):
            DepartureAirport.append(q.text)
        for r in c.findAll('div', {'class': 'c-result-period__time'}):
            DepartureTime.append(r.text)
    for d in body.findAll('div', {'class': 'flight-time c-result-period result-period'}):
        if d.find('div', {'class': 'time-cell line-cell c-result-period__cell c-result-period_beeline help'}):
            s = d.find('span', {'class': 'bod-bottom-dotted'})
            TransferAirport.append(s.text)
        else:
            TransferAirport.append(' ')
    for e in body.findAll('div', {'class': 'c-result-period__arrive'}):
        for t in e.findAll('div', {'class': 'bod-bottom-dotted'}):
            ArrivalAirport.append(t.text)
        for u in e.findAll('div', {'class': 'time c-result-period__time'}):
            ArrivalTime.append(u.text)
    for g in body.findAll('div', {'class': 'result-item J_FlightItem'}):
        flightPrice = g.findAll('span', {'class': 'o-price-flight'})[0].text
        Price.append(flightPrice)

    workbook = xlsxwriter.Workbook('AirlineData_BNE.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Airline')
    worksheet.write('B1', 'FlightNo')
    worksheet.write('C1', 'DepartureAirport')
    worksheet.write('D1', 'TransferAirport')
    worksheet.write('E1', 'ArrivalAirport')
    worksheet.write('F1', 'DepartureTime')
    worksheet.write('G1', 'ArrivalTime')
    worksheet.write('H1', 'Price')
    worksheet.write('I1', 'Date')
    row = 1
    col = 0
    for j in range(Airline.__len__()):
        worksheet.write_string(row, col, Airline[j])
        worksheet.write_string(row, col + 1, str(FlightNo[j]))
        worksheet.write_string(row, col + 2, str(DepartureAirport[j]))
        worksheet.write_string(row, col + 3, str(TransferAirport[j]))
        worksheet.write_string(row, col + 4, str(ArrivalAirport[j]))
        worksheet.write_string(row, col + 5, str(DepartureTime[j]))
        worksheet.write_string(row, col + 6, str(ArrivalTime[j]))
        worksheet.write_string(row, col + 7, str(Price[j]))
        worksheet.write_string(row, col + 8, str(FlightDate[j]))
        row += 1
    workbook.close()




