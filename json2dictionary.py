"""
Code that will read a JSON file
Save the JSON as a list of dictionaries 
Answer questions about the data set by casting the values 
and splitting the strings into meaningsful sub-lists
Then plotting the data in some diagrams

The example file will be a huge data set with electric bike rentals

The questions are as follows:
Du skal lage et program som leser inn informasjon fra datasettet og presenterer dette i to oversikter. Du skal bruke datasettet fra forberedelsen. Hvis du ikke har forberedt dette kan du også laste ned datasettet fra forberedelsesdelen nå.
 
a)
- Lag et program som presenterer de tre mest brukte startlokasjonene og de tre minst brukte startlokasjonene. Presentasjonen skal også vise antall turer fra disse startlokasjonene.
 
b)
- Utvid programmet slik at det også presenter et passende diagram som viser totalt antall turer fra alle startlokasjoner til sammen, per ukedag.

Eksempeleksamen file:
0__started_at: (utc--> yyyy-mm-dd hh:mm:ss),
1__ended_at: (utc--> yyyy-mm-dd hh:mm:ss),
2__duration: (float),
3__start_station_id (int),
4__start_station_name (str),
5__start_station_description (str)

For komplett løsning, bruk kode fra filen csv2dictionary.py


"""
import csv
import json
import os.path
import matplotlib.pyplot as pl
import datetime
import matplotlib.pyplot

file_name = "Data eksempeleksamen/Eksempeleksamen22.json"
this_path = os.path.abspath(os.path.dirname(__file__))
path_json = os.path.join(this_path, file_name)

data = {}#Storage of the data set in dictionary format
#heading = [] #The heading for the csv file
#skiplines = 0 #THe number of lines to be skipped while reading after the heading
#To count the number of something, it is pretty easy to convert to a dictionary, giving you the option to use not in to count the number of occurrences
count_dict = {}

#I prefer having this as a function

#Function to read json and store as dictionary
def json2dict():
    #output = {}
    #path_csv = os.path.join(this_path, file_name)
    with open(path_json, 'r') as file_json:
        output = json.load(file_json)
    
    return output

data = json2dict()

for i in range(3):
    print(data[i])

def clean_data(raw_data):
    for i in range(len(raw_data)):
        tmp = raw_data[i]['started_at']
        #print(tmp)
        try: 
            dt = tmp.split(" ")
            ymd = dt[0].split("-")
            hmstz = dt[1].split("+")
            hms = hmstz[0].split(":")
            raw_data[i]['started_at'] = {
                'year': int(ymd[0]), 
                'month': int(ymd[1]), 
                'day': int(ymd[2]), 
                'hour': int(hms[0]), 
                'min': int(hms[1]), 
                'sec': float(hms[2])}
        except:
            #print("Error, line ", i)
            pass

        #for debugging:
        #print("ymd: ",ymd,"--> hms: ",hms )
        #print(raw_data[i]['started_at'])
        raw_data[i]['duration'] = int(raw_data[i]['duration'])
        raw_data[i]['start_station_id'] = int(raw_data[i]['start_station_id'])

clean_data(data)
for i in range(3):
    print(data[i])