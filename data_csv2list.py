#
"""
For å behandle CSV-filer, trenger vi noen metoder

ha en ekstern fil
åpne fila
lagre resultatet fra innlesinga. 
Rense data, få over til riktig datatype
Lagre i liste eller ordbok eller annet?
Lukke fila

Videre: Mer generaliserte versjoner?
"""

#Steg 1: Beskrive datafilen
#Tips: Bruk korrekte stier. her er tips fra https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
import csv
import json
import os.path

file_name = "Data skogeiere/skogeiere.csv"
valg2023 = "Data Valg2023/valg2023.csv"
this_path = os.path.abspath(os.path.dirname(__file__))
path_csv = os.path.join(this_path, file_name)
file_json = os.path.join(this_path, "Data sykefravær/sykefravær.json")


"""
Videre: Åpne fila med with kodeordet som gjør at du ikke trenger å lukke
fila til slutt
Fra https://www.geeksforgeeks.org/with-statement-in-python/

Det er dessuten lurt å vite litt om csv-biblioteket:
https://docs.python.org/3/library/csv.html

csv.reader()
"""

data = []
#Dette kommer ikke til å gå hvis vi skriver encoding = "utf-8" i open
with open(path_csv,'r') as file_csv:
    spamreader = csv.reader(file_csv, delimiter=';', quotechar='"')
    for row in spamreader:
        #print(row)
        data.append(row)

#implementerer dette som en funksjon
def read_csv(file_name: str =""):

    output = []
    path_csv = os.path.join(this_path, file_name)
    with open(path_csv,'r') as file_csv:
        spamreader = csv.reader(file_csv, delimiter=';', quotechar='"')
        
        for row in spamreader:
            #print(row)
            output.append(row)
    return output

csv_list = read_csv("Data sykefravær/sykefravær.csv")

for entry in csv_list:
    print(entry)

