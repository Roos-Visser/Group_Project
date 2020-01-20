import json
import csv

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
    with open('genres_data.csv', 'a', encoding='utf8') as file:
        
        list_data = []

        for entry in data:
            if "ontology/activeYearsStartYear" in entry and 'ontology/genre_label' in entry and "ontology/background" in entry and entry["ontology/background"] == 'solo_singer':
                if type(entry["ontology/genre_label"]) == list:
                    for genre in entry["ontology/genre_label"]:
                        list_data.append([entry["ontology/activeYearsStartYear"],genre])
                else:
                    list_data.append([entry["ontology/activeYearsStartYear"],entry["ontology/genre_label"]])

            classification of the genres
        for genre in list_data:
            if genre[1] in ("Hard rock", "blues rock"):
                genre[1] = "Rock music"
            elif genre[1] in ("Britpop", "Christian alternative rock", "college rock", "dream pop", "emo", "geek rock", "gothic rock", "grunge", "indie rock", "math rock", "noise pop", "nu gaze", "post-grunge","post-punk revival", "post-rock", "shoegazing"):
                genre[1] = "Alternative rock"
            elif genre[1] in ("Art pop", "Bubblegum pop", "Dance-pop", "Experimental pop", "New wave music", "Operatic pop", "Progressive pop", "Sophisti-pop", "Space age pop", "Sunshine pop", "Synthpop", "Teen pop", "K-pop", "Electropop", "Latin pop", "Arabic pop music", "Indian pop", "Mexican pop music", "Europop", "French pop music", "Power pop", "Traditional pop music", "Operatic pop", "Baroque pop", "Britpop", "Art pop", "Balkan_pop", "Dream pop", "J-pop"):
                genre[1] = "Pop music"
            elif genre[1] in ("Alternative hip hop", "Christian hip hop", )
            

        writer = csv.writer(file)
        writer.writerows(list_data)
                # file.write(f'{entry["ontology/activeYearsStartYear"]},{entry["ontology/genre_label"]}\n')

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('genres_data.csv', 'w', encoding='utf8') as file:
    file.write(f'year, genre \n')

# convert_csv('./People/A_people.json')

for letter in alphabet:
    convert_csv(f'./GroupProject/Group_Project/People/{letter}_people.json')