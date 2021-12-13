import json
import csv
from pathlib import Path

FILE_FOR_PARSE = Path('J.json')
FILE_FOR_SAVE = 'j_data.csv'
def read_Json(filename):
    with open(filename, 'r', encoding= 'utf-8') as F:
        return json.load(F)
#print(read_Json('J.json'))

def get_content():
    j_data = []
    JSON = read_Json(FILE_FOR_PARSE)
    for item in JSON['response']['items']:
        a = item['first_name']
        b = item['last_name']
        j_data.append({
            'name': (a +' '+ b).strip("'")
            #'name': [a, b] #list file with '

        })
        #print(j_data)
    return j_data

def save_file(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Полное Имя:'])
        for item in items:
            writer.writerow([item['name']])

def parse():
    if FILE_FOR_PARSE.exists():
        j_data = []
        j_data.extend(get_content())
        save_file(j_data, FILE_FOR_SAVE)
    else:
        print('No File')
parse()