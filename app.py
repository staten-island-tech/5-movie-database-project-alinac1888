import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)

for index, movie in enumerate(data):
    print(index, ":",(movie)['title'])

# choice = int(input("year after"))
# choicee = int(input("year before"))

# for movie in data:
#     if choice < movie['year'] < choicee:
#         print(movie['title'], movie['year'])

choiceee = int(input("during year"))
for movie in data:
    if choiceee == movie['year']:
        print(movie['title'])

specific = input("EXACT movie u like")
while True:
    if specific == movie['title']:
        print(movie['title'])