"""
Code that will read a csv file
Save the csv as a two dimensional list
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
import os.path
import matplotlib.pyplot as pl
import datetime
from dateutil.parser import parse

file_name = "Data eksempeleksamen/Eksempeleksamen22.csv"
this_path = os.path.abspath(os.path.dirname(__file__))
path_csv = os.path.join(this_path, file_name)

data = []#Storage of the data set in list format
heading = [] #The heading for the csv file
skiplines = 0 #THe number of lines to be skipped while reading after the heading
#To count the number of something, it is pretty easy to convert to a dictionary, giving you the option to use not in to count the number of occurrences
count_dict = {}

#I prefer having this as a function

def read_csv():
    with open(path_csv,'r',encoding = 'utf-8') as file_csv:
        reader_object = csv.reader(file_csv, delimiter=',')
        i = 0
        for row in reader_object:
            if i==0:
                heading = row
            else:
                data.append(row)
            i +=1
#Calling the function
read_csv()

#Cleaning the data means casting strings to int and floats, splitting strings and so on

def clean_data(raw_data):#Converting to int values
    for i in range(len(raw_data)):
        raw_data[i][2] = int(raw_data[i][2])
        raw_data[i][3] = int(raw_data[i][3])
        raw_data[i][8] = int(raw_data[i][8])
        raw_data[i][0] = raw_data[i][0].split(" ")
        raw_data[i][0][0] = raw_data[i][0][0].split("-")
        raw_data[i][1] = raw_data[i][1].split(" ")
        raw_data[i][1][0] = raw_data[i][1][0].split("-")
        raw_data[i][0][0][2]=int(raw_data[i][0][0][2])     
        print(raw_data[i][0])
#calling
clean_data(data)

# Loop through each row in the data list
def get_count_dict():
    for row in data:
        # Get the value of the third column, which contains the station ID
        station_id = int(row[3])
        # Vi kan få stasjonsnavnet direkte ved å legge inn station_id = row[3]    
        # If the station ID is not already in the dictionary, add it with a value of 1
        if station_id not in count_dict:
            count_dict[station_id] = 1
        # If the station ID is already in the dictionary, increment its value by 1
        else:
            count_dict[station_id] += 1


sorted_count_dict = dict(sorted(count_dict.items(), key=lambda item: item[1]))
#print(sorted_count_dict)

"""
Jeg har mer lyst til å bruke todimensjonal liste, det lar seg sortere for å hente ut topp [n]
"""

sorted_data = sorted(data,key = lambda x: x[3])
#print(sorted_data[0],sorted_data[1],sorted_data[2])

#A function to return a list with tuples [station_id, counter] for every unique station_id
def count_2_list(list):

    count_list = []
    i = 0
    while i <len(list):

        # Get the value of the fourth column, which contains the station ID
        # or the name which is in the fifth column
        #station_id = list[3]
        station_id = list[i][4]

        counter = 0
        try:
            while list[i][4]==station_id and i<len(list):
                counter +=1
                i +=1
            count_list.append([station_id,counter])
            i +=1
        except IndexError:
            break
    return count_list

#Saving lists with countings and sorting them using langda, reverse for "top N"
count_list = count_2_list(sorted_data)
count_list = sorted(count_list,key=lambda x:x[1], reverse = True)

#print(count_list)
print("De tre mest brukte startstedene er:")
print(count_list[0])
print(count_list[1])
print(count_list[2])

#Bottom N are found using count_list and sorting, not reversed
count_list = sorted(count_list,key=lambda x:x[1], reverse = False)
#print(count_list)
print("De tre minst brukte startstedene er:")
print(count_list[0])
print(count_list[1])
print(count_list[2])

days_total = [0,0,0,0,0,0,0]
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

def get_sum_daily():
    for i in range(len(data)):
        y = int(data[i][0][0][0])
        m = int(data[i][0][0][1])
        d = int(data[i][0][0][2])
        
        day_number = int(datetime.datetime(y,m,d).weekday())
        days_total[day_number] +=1
        """
        First method, bad programming
        #print(int(data[i][0][0][2]) % 7)
        match int(data[i][0][0][2]) % 7:
            case 1:
                days_total[0]+=1
            case 2:
                days_total[1]+=1
            case 3:
                days_total[2]+=1
            case 4:
                days_total[3]+=1
            case 5:
                days_total[4]+=1
            case 6:
                days_total[5]+=1
            case _:
                days_total[6]+=1
        """
    #return days_total
    #days_total[3]=-9

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