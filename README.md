# US-Accidents

This is a countrywide car accident dataset, which covers 49 states of the USA. The data is collected from February 2016 to March 2019, using several data providers, including two APIs which provide streaming traffic event data. These APIs broadcast traffic data in real-time.

- `Source`: https://www.kaggle.com/sobhanmoosavi/us-accidents

- `Description`: This is a countrywide car accident dataset, which covers 49 states of the USA. The data is collected from February 2016 to March 2019, using several data providers, including two APIs which provide streaming traffic event data. These APIs broadcast traffic data in real-time.

- `Content`: This dataset has been collected in real-time, using multiple Traffic APIs. Currently, it contains data which is collected from February 2016 to March 2019 for the Contiguous United States. It contains data of 3.5 million traffic accidents. The data was collected from two APIs that provide streaming traffic event data. These APIs broadcast traffic data in real-time. The dataset also contains data from different sources such as MapQuest, Bing, MapQuest-Bing, and MapQuest-Bing-MapQuest.

- `Acknowledgements`: Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. “A Countrywide Traffic Accident Dataset.”, 2019.

- `Inspiration`: This is a countrywide car accident dataset, which covers 49 states of the USA. The data is collected from February 2016 to March 2019, using several data providers, including two APIs which provide streaming traffic event data. These APIs broadcast traffic data in real-time.

- `Columns`: 
    - ID: This is a unique identifier of the accident record.
    - Source: Indicates source of the accident report (i.e. the API which reported the accident.).
    - TMC: A traffic accident may have a Traffic Message Channel (TMC) code which provides more detailed description of the event.
    - Severity: Shows the severity of the accident, a number between 1 and 4, where 1 indicates the least impact on traffic (i.e., short delay as a result of the accident) and 4 indicates a significant impact on traffic (i.e., long delay).
    - Start_Time: Shows start time of the accident in local time zone.
    - End_Time: Shows end time of the accident in local time zone.
    - Start_Lat: Shows latitude in GPS coordinate of the start point.
    - Start_Lng: Shows longitude in GPS coordinate of the start point.
    - End_Lat: Shows latitude in GPS coordinate of the end point.
    - End_Lng: Shows longitude in GPS coordinate of the end point.
    - Distance(mi): The length of the road extent affected by the accident.
    - Description: Shows natural language description of the accident.
    - Number: Shows the street number in address field.
    - Street: Shows the street name in address field.
    - Side: Shows the relative side of the street (Right/Left) in address field.
    - City: Shows the city in address field.
    - County: Shows the county in address field.
    - State: Shows the state in address field.
    - Zipcode: Shows the zipcode in address field.
    - Country: Shows the country in address field.
    - Timezone: Shows timezone based on the location of the accident (eastern, central, etc.).
    - Airport_Code: Denotes an airport-based weather station which is the closest one to location of the accident.
    - Weather_Timestamp: Shows the time-stamp of weather observation record (in local time).
    - Temperature(F): Shows the temperature (in Fahrenheit).
    - Wind_Chill(F): Shows the wind chill (in Fahrenheit).
    - Humidity(%): Shows the humidity (in percentage).
    - Pressure(in): Shows the air pressure (in inches).
    - Visibility(mi): Shows visibility (in miles).
    - Wind_Direction: Shows wind direction.
    - Wind_Speed(mph): Shows

