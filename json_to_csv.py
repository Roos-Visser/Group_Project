import json
import csv

# This function shall convert a json file into a csv file for R analyses

# Defining the function
# It receives a file which we have to type in, these are the ones of the zip file 
with open ('Group_Project/FullDataSet.json', 'r', encoding='utf-16') as json_file:
    data = json.load(json_file)

    # lines that we need:
    # ontology/activeYearsStartYear
    # ontology/genre_label

    # creating a new csv file. 'a' specifies that that append the entries to the same file
    # That way we can create one csv file with all the relevant data we need
with open('csv_data.csv', 'w', encoding='utf8') as file:
    file.write(f'genres, year \n')
    for entry in data:
        file.write(f'{entry["ontology/activeYearsStartYear"]},{entry["ontology/genre_label"]}\n')