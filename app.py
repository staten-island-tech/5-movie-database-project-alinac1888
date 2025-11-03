import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

for index, movie in enumerate(data):
    print(index, ":",(movie)['title'])

choice = int(input("e"))
if int({data[movie]['year']}) > ({data(movie)[choice]}):
    print({data[movie]['title']})