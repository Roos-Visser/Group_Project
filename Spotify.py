#open file and load its contents
with open ('top10s.csv') as file:
    #read keys and content
    header = file.readline()
    content_spotify = file.readlines()

header = header.split(',')

#create an empty list
spotify_list = []

# for line in content_spotify:
# #Split the list by lines
#     line = line.strip().split(',')
#     # Add each line to the the list
#     spotify_list.append({
#         'genre': line[3], 'pop': line[-1]
#     })

# print(spotify_list)

# create a new csv file with the list of dictionairies
with open ('spotify.csv', 'w') as file:
    #create the header
    file.write(f'genre, popularity\n')
    for line in content_spotify:
        #Split the list by lines
        line = line.strip().split(',')
        # Add each line to the the list
        spotify_list.append({
            'genre': line[3], 'pop': line[-1]
        })
    





