import pandas as pd

SD_data = pd.read_csv("raw_data_hotel_SD.csv")
# Replace the city column by city name
SD_data.city = "Sydney"
SD_data.price = SD_data.price.str[3:]
SD_data.location = SD_data.location
print(SD_data)
SD_data.to_csv("CLEAN_SD_HOTEL.csv")


ML_data = pd.read_csv("raw_data_hotel_MEL.csv")
ML_data.city = "Melbourne"
ML_data.price = ML_data.price.str[3:]
ML_data.location = ML_data.location
ML_data.to_csv("CLEAN_ML_HOTEL.csv")

BR_data = pd.read_csv("raw_data_hotel_BR.csv")
ML_data.city = "Brisbane"
BR_data.price = BR_data.price.str[3:]
BR_data.location = BR_data.location
BR_data.to_csv("CLEAN_BR_HOTEL.csv")


CAN_data = pd.read_csv("raw_data_hotel_CAN.csv")
ML_data.city = "Canberra"
CAN_data.price = CAN_data.price.str[3:]
CAN_data.location = CAN_data.location
CAN_data.to_csv("CLEAN_CAN_HOTEL.csv")



AD_data = pd.read_csv("raw_data_hotel_AD.csv")
ML_data.city = "Adelaide"
AD_data.price = AD_data.price.str[3:]
AD_data["location"] = AD_data["location"].str.replace('"','')
AD_data.to_csv("CLEAN_AD_HOTEL.csv",index = 0)

SD_data.append(ML_data).append(AD_data).append(CAN_data).append(BR_data).to_csv("Hotel_data.csv",index = 0)

# SD_data.to_csv("Hotel_data.csv",index = 0)