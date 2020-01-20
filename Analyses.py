import json

# This function shall convert a json file into a csv file for R analyses

# Defining the function
# It receives a file which we have to type in, these are the ones of the zip file
def convert_csv(filepath): 
    with open (filepath) as json_file:
        data = json.load(json_file)


    # lines that we need:
    # ontology/activeYearsStartYear
    # ontology/genre_label

    # creating a new csv file. 'a' specifies that that append the entries to the same file
    # That way we can create one csv file with all the relevant data we need
    with open('names_data.csv', 'a', encoding='utf8') as file:
        file.write(f'genres, year \n')
        for entry in data:
            if "ontology/activeYearsStartYear" in entry and 'ontology/genre_label' in entry and "ontology/background" in entry and entry["ontology/background"] == 'solo_singer':
                file.write(f'{entry["ontology/activeYearsStartYear"]},{entry["ontology/genre_label"]}\n')

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for letter in alphabet:
    convert_csv(f'./People/{letter}_people.json')