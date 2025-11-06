import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)

for index, movie in enumerate(data):
    print(index, ":",(movie)['title'])

# year after and before
# choice = int(input("year after"))
# choicee = int(input("year before"))

# for movie in data:
#     if choice < movie['year'] < choicee:
#         print(movie['title'], movie['year'])

# during year
# choiceee = int(input("during year"))
# for movie in data:
#     if choiceee == movie['year']:
#         print(movie['title'])

for i in data:  
    specific = input("EXACT movie u like")
    booth = []
    booth.append(specific)
    booth.append(movie['title'])
    if len(specific) == len(movie['title']):
        print(f"{movie['title']} is avliable")
    else: 
        print(f"{specific} is not found")
        break 