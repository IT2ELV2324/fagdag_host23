#Steg 1: Beskrive datafilen
#Tips: Bruk korrekte stier. her er tips fra https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory

"""
Eksempeleksamen:
started_at,ended_at,duration,start_station_id,start_station_name,start_station_description
0           1       2           3               4                   5  
"""
import csv
#import json
import os.path
import datetime
import matplotlib.pyplot as pl


file_name = "Data eksempeleksamen/Eksempeleksamen22.csv"
this_path = os.path.abspath(os.path.dirname(__file__))
path_csv = os.path.join(this_path, file_name)
file_json = os.path.join(this_path, "Data sykefravær/sykefravær.json")

data = []
heading = []
#Dette kommer ikke til å gå hvis vi skriver encoding = "utf-8" i open
with open(path_csv,'r',encoding = 'utf-8') as file_csv:
    spamreader = csv.reader(file_csv, delimiter=',')
    i = 0
    for row in spamreader:
        if i==0:
            heading = row
        else:
            data.append(row)
        i +=1
        #if i>100:
        #    break


        

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
        
        

clean_data(data)
#print(data[2])

"""
Bruke ordbok for å telle antall forekomster av start-stasjon
I stor grad inspirert av ki.osloskolen.no samtalen vedlagt: Hjelpemiddel ki.osloskolen.no i mappen Data eksempeleksamen
"""
count_dict = {}

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
#kaller funksjonen
get_count_dict()

#Må sortere denne ordboken

sorted_count_dict = dict(sorted(count_dict.items(), key=lambda item: item[1]))
#print(sorted_count_dict)


"""
Jeg har mer lyst til å bruke todimensjonal liste, det lar seg sortere for å hente ut topp [n]
"""

sorted_data = sorted(data,key = lambda x: x[3])
#print(sorted_data[0],sorted_data[1],sorted_data[2])

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

count_list = count_2_list(sorted_data)
count_list = sorted(count_list,key=lambda x:x[1], reverse = True)
#print(count_list)
print("De tre mest brukte startstedene er:")
print(count_list[0])
print(count_list[1])
print(count_list[2])

count_list = sorted(count_list,key=lambda x:x[1], reverse = False)
#print(count_list)
print("De tre minst brukte startstedene er:")
print(count_list[0])
print(count_list[1])
print(count_list[2])

days_total = [0,0,0,0,0,0,0]

def get_sum_daily():
    for i in range(len(data)):
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
    #return days_total
    #days_total[3]=-9

day1 = datetime.datetime(2022,5,1)
"""day2 = datetime.datetime(2022,05,01)
day3 = datetime.datetime(2022,05,01)
day4 = datetime.datetime(2022,05,01)
day5 = datetime.datetime(2022,05,01)
day6 = datetime.datetime(2022,05,01)
day7 = datetime.datetime(2022,05,01)
"""

print("2022-05-01 is a day number ",day1.weekday())
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']


get_sum_daily()
print(days_total)
#print(data[5])
pl.figure()
pl.bar(days,days_total)
pl.show()
#print(count_dict)
#print(data)