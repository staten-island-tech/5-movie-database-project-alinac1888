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

# def search():
#     specific = input("EXACT movie u like")
#     found = 0
#     for i in data:  
#         if specific.lower() in i['title'].lower():
#             print(f"{i['title'].lower()} is avliable")
#             found += 1
#         elif found == 0:
#             print("is not found")     
# search()

def search():
    choice = input("genre")
    found = 0
    for i in data:  
        if choice in i['genres']:
                print(f"{i['title']} is avaliable")
                found += 1
        elif found == 0:
                print("is not found")
search()