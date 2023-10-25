#
"""
For å behandle CSV-filer, trenger vi noen metoder

ha en ekstern fil
åpne fila
lagre resultatet fra innlesinga. 
Rense data, få over til riktig datatype
Lagre i liste eller ordbok eller annet?
Lukke fila

SSB-filen i sykefravær har et ugunstig format for dictionary lesning

"""

#Steg 1: Beskrive datafilen
#Tips: Bruk korrekte stier. her er tips fra https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
import csv
import json
import os.path
import pprint

this_path = os.path.abspath(os.path.dirname(__file__))
path_csv = os.path.join(this_path, "Data Valg2023/valg2023.csv")
file_json = os.path.join(this_path, "Data sykefravær/sykefravær.json")


"""
Videre: Åpne fila med with kodeordet som gjør at du ikke trenger å lukke
fila til slutt
Fra https://www.geeksforgeeks.org/with-statement-in-python/

Det er dessuten lurt å vite litt om csv-biblioteket:
https://docs.python.org/3/library/csv.html

csv.reader()
"""



data_dict = []
#Det kommer ikke til å gå med mindre encoding = "utf-8"
with open(path_csv,'r',encoding = "utf-8") as file_csv:
    data_dict = list(csv.DictReader(file_csv, delimiter=';', quotechar='"'))


"""for k,v in data_dict:
    print("key: ",k,"--> Value: ",v)
"""
#implementerer dette som en funksjon
def csv2dict(file_name: str =""):

    output = []
    path_csv = os.path.join(this_path, file_name)
    with open(path_csv,'r') as file_csv:
        try:
            output = list(csv.DictReader(file_csv, delimiter=';', quotechar='"'))
        except UnicodeDecodeError:
            print("UnicodeDecodeError")
        else: 
            print("Lol")
     
    #for row in output:
    #    print(row)

    return output

for row in data_dict:
    pprint.pprint(row)