# Squad Travels, Inc. <img src="README_Pictures/squad_logo.jpeg" alt="Sky Walking logo" height="180px" align="right" />


[![GitHub stars](https://img.shields.io/github/stars/Marxh/Python_Trip_Project.svg?style=for-the-badge&label=Stars&logo=github)](https://github.com/Marxh/Python_Trip_Project)

## 0. Group Members

Group name  | Andrew ID | Email
------------- | ------------- | -------------
Yuanli Gu  | Content Cell | 
Yuou Lei  | Content Cell |
Xinrui Zheng  | Content Cell |
Shanyue Wan  | shanyuew | shanyuew@andrew.cmu.edu
Rhea-Luz Valbuena | Content Cell | 

## 1. Software
### 1.1. Abstract
**Squad Travels, Inc** is a software to provide comprehensive personalized suggestions for travellers from China. We scraped data including, geography data, social media comments, weather website, hotel data. Our suggestions are based on the integration of those information. Our version is to be the premier choice of Chinese travelers who want to travel to Australia for travel information needs. 

**Following is our core functions:**

- Route Guidance: Map and Trip Plans
- Airline Information Recommend
- Hotel Information Recommend
- Weather Information Display
- Calculate Distance and Total Costs
- Word Cloud Generation

### 1.2. Dependence

Library | Version 
------------- | ------------- 
pandas | 0.25.1
numpy | 1.16.4
matplotlib | 3.1.0 
folium | 0.10.0
wordcloud | 1.5.0
prettytable | 0.7.2
jieba | 0.39

### 1.3. File Structure
> main.py
> 
> graph_generator.py
>
> map_generator.py
>
> filter_suitable_service.py
>
> weather_analysis.py
>
> NLP
> > nlp_analytics.py 
> 
> dataset
> > AdelaideMetroStops_GDA2020.json
> > 
> > AdelaideMetroStops_GDA94.json
> > 
> > airline_data.xlsx
> > 
> > ctrip_cleaned_data.csv
> > 
> > hotel_data.xlsx
> > 
> > weather_data.xlsx

### 1.4. Library Install

Use command line: `pip install -r requirements.txt` to install all the python modules that you need.

### 1.5. Running

Running the main modle.

Input Mode: `Economy`/`Luxury`

Input City: `Adelaide`

Input Beginning Time: `2018-01-01`

Input Ending Time: `2018-04-01`

Input Down-Bound Hotel Price: `50`

Input Up-Bound Hotel Price: `500`

Input Down-Bound Flight Price: `500`

Input Up-Bound Flight Price: `1000`

### 1.6. Live Deomo
### a). Get Input
<img src="README_Pictures/screenshot1.jpg" alt="Sky Walking logo" height="50%" width="50%" align="right"/>

At the beginning, to get personalized services, customers should input their preferences. Based on the preference, our program can then give the services, travelling route they want.
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />

### b). Hotel Price Pie Chart
<img src="README_Pictures/screenshot2.jpg" alt="Sky Walking logo" height="50%" width="50%" align="right"/>

Based on the output of the price range of the customer, our program displays the hotel information as a pie chart. Customers can know what percentage of the price range takes in the selected city.
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
### c). Temperature Line Chart
<img src="README_Pictures/screenshot3.jpg" alt="Sky Walking logo" height="50%" width="50%" align="right"/>

Our program will display the weather changes in the selected city. Detailed and past year's temperature will be displayed.
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
### d). Airline Price Pie Chart
<img src="README_Pictures/screenshot4.jpg" alt="Sky Walking logo" height="50%" width="50%" align="right"/>

Airline information will be displayed as pie chart. 
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
### e). Map Visualization
<img src="README_Pictures/map.jpg" alt="Sky Walking logo" height="50%" width="50%" align="right"/>

In the `map/map.html`, a route map will be displayed to guide the customers where to go and how to play in selected city. 
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
### f). Plan Steps
<img src="README_Pictures/screenshot5.jpg" alt="Sky Walking logo" height="50%" width="50%" align="right"/>

A more specific route plan will be displayed below.
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
### g). Cost and Distance Steps
<img src="README_Pictures/screenshot6.jpg" alt="Sky Walking logo" height="50%" width="50%" align="right"/>

Costs and diatance information about the route are displayed as table.
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />

### h). Word Clouds
<img src="README_Pictures/screenshot7.jpg" alt="Sky Walking logo" height="50%" width="50%" align="right"/>

Word clouds corresponding with every spots are listed below. Each cloud demonstates the word that has the highest frequency in the comments.
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />

## 2. Scrape

### 2.1. Abstract

Data sources we use include the follows:

- Ctrip comment data
- Weibo data
- Tripadvisor hotel data
- Weather data
- Airline data
- Adelaide Metro Bus data

<img src="README_Pictures/data_source.png" alt="Sky Walking logo" align="center"/>

### 2.2. Analytics Process

<img src="README_Pictures/analytic_process.png" alt="Sky Walking logo" align="center"/>

### 2.3. Hotel Data Scrape

Library | Version 
------------- | ------------- 
Library| Version
pandas|0.24.2
numpy|1.16.1
beautifulsoup4|4.7.1
selenium|3.141.0

**Running**  
Run Hotel_Worm.py to scrap the hotel information in different Australia cities (Sydney, Melbourne, Adelaide, Canberra, Brisbane). After the sunning of this file, you will get four csv files which named as raw_data_hotel_SD.csv, raw_data_hotel_MEL.csv, raw_data_hotel_AD.csv, raw_data_hotel_CAN.csv, raw_data_hotel_BR.csv.

**Cleaning**  
Run Hotel_Clean.py to clean the data, which will replace the city column data from number to city name. Then it will slice the “AUD$” in price column. Finally, it will output Hotel_Clean.csv.

**Description**  
This script file will scrape hotel information from https://www.trivago.com.au/. The data fields include city, hotel name, customers’ rate, location and price. It is about different day’s price for each hotel from 2019.11.01 to 2019.11.29.

### 2.4. Hotel Data Scrape

Library | Version 
------------- | ------------- 
Library| Version
pandas|0.24.2
numpy|1.16.1
beautifulsoup4|4.7.1
selenium|3.141.0

**Running**  
Run Hotel_Worm.py to scrap the hotel information in different Australia cities (Sydney, Melbourne, Adelaide, Canberra, Brisbane). After the sunning of this file, you will get four csv files which named as raw_data_hotel_SD.csv, raw_data_hotel_MEL.csv, raw_data_hotel_AD.csv, raw_data_hotel_CAN.csv, raw_data_hotel_BR.csv.


**Cleaning**  
Run Hotel_Clean.py to clean the data, which will replace the city column data from number to city name. Then it will slice the “AUD$” in price column. Finally, it will output Hotel_Clean.csv.

**Description**  
This script file will scrape hotel information from https://www.trivago.com.au/. The data fields include city, hotel name, customers’ rate, location and price. It is about different day’s price for each hotel from 2019.11.01 to 2019.11.29.