import csv
import json

with open('Billboard_Data.json') as file:
    billboard = json.load(file)

billboard_many_genres = []

for year in billboard:
    for song in year["songs"]:
        billboard_many_genres.append([song["year"], song["pos"], song["tags"]])
        

billboard_incl_count = [["year","pos","genre","count"]]

for song in billboard_many_genres:
    number_of_genres = len(song[2])
    for genre in song[2]:
        row = [song[0], song[1], genre, 1 / number_of_genres]
        billboard_incl_count.append(row)

with open('billboard.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(billboard_incl_count)