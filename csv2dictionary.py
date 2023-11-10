"""
Code that will read a csv file
Save the csv as a list of dictionaries 
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

"""

import csv
import json
import os.path
import matplotlib.pyplot as pl
import datetime
import matplotlib.pyplot

file_name = "Data eksempeleksamen/Eksempeleksamen22.csv"
this_path = os.path.abspath(os.path.dirname(__file__))
path_csv = os.path.join(this_path, file_name)

data = []#Storage of the data set in list format
heading = [] #The heading for the csv file
skiplines = 0 #THe number of lines to be skipped while reading after the heading
#To count the number of something, it is pretty easy to convert to a dictionary, giving you the option to use not in to count the number of occurrences
count_dict = {}

#I prefer having this as a function

#Function to read csv and store as dictionary
def csv2dict():

    output = []
    #path_csv = os.path.join(this_path, file_name)
    with open(path_csv,'r',encoding = "utf-8") as file_csv:
        try:
            output = list(csv.DictReader(file_csv, delimiter=','))
        except UnicodeDecodeError:
            print("UnicodeDecodeError")
        else: 
            print("Lol")
            pass
     
    return output

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

data = csv2dict()
clean_data(data)
#print(data[0:10])

count_dict = {}

for row in data:
    station = row['start_station_name']
    if station not in count_dict.keys():
        count_dict[station] = 1
    else:
        count_dict[station] +=1

sorted_count = sorted(count_dict.items(), key=lambda item: item[1],reverse=True)

#print(sorted_count[0:3])

def get_extreme_N(N: int = 3, top: bool = True):

    if top:
        sorted_count = sorted(count_dict.items(), key=lambda item: item[1],reverse=True)
        print(f"Topp {N} stasjoner benyttet er:")

    else: 
        sorted_count = sorted(count_dict.items(), key=lambda item: item[1])
        print(f"De {N} minst benyttede stasjonene er:")

    #print("Topp tre stasjoner benyttet er ")
    i = 0
    while i < N:
        print("Stasjon: ",sorted_count[i][0],". Antall turer: ",sorted_count[i][1])
        i +=1

get_extreme_N()
get_extreme_N(top = False)

days_total = [0,0,0,0,0,0,0]
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

def get_sum_daily():
    for i in range(len(data)):
        y = data[i]['started_at']['year']
        m = data[i]['started_at']['month']
        d = data[i]['started_at']['day']
        #print(f"year = {y}, month = {m}, day = {d}")
        
        day_number = int(datetime.datetime(y,m,d).weekday())
        days_total[day_number] +=1
        
get_sum_daily()
print(days_total)
#print(data[5])

def plot_data():
    pl.figure()
    pl.bar(days,days_total)
    pl.xlabel("Weekday")
    pl.ylabel("Number of rides")
    pl.title("Some graph lol")
    pl.show()
    #print(count_dict)
    #print(data)
plot_data()