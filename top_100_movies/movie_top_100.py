import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
movies_list = soup.find_all(name="h3", class_="title")
# print(movie_list)
movies = []
for movie in movies_list:
    # print(movie.getText())
    movie_name = movie.getText()
    if movie_name == "The Godfather":
        movies.append("1) The Godfather")
    elif movie_name == "12: The Godfather Part II":
        movies.append("12) The Godfather Part II")
    else:
        movies.append(movie_name)


# print(movies)
movies.reverse()
# print(movies)

for movie in movies:
    with open("movies.txt", "a", encoding="utf-8") as file:
        file.write(f"{movie}\n")

