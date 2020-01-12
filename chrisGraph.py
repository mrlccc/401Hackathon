import csv
from statistics import mean
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#Does tv series length correlate with ratings?
with open('netflix_titles_nov_2019.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    #genre is key: value is array of all seasons
    genre = {}
    for row in reader:
        if row["type"] != "TV Show":
            continue

        show_seasons = int(row["duration"].split(" ")[0])

        show_genres = [x.strip() for x in row["listed_in"].split(",")]
        for show_genre in show_genres:
            if show_genre in genre:
                genre[show_genre].append(show_seasons)
            else:
                genre[show_genre] = [show_seasons]

    #Calculate season averages of each genre
    genre_name = []
    genre_season_len = []
    for g_name in genre.keys():
        genre_name.append(g_name)
        genre_season_len.append(mean(genre[g_name]))

    #Sort by season
    genre_name = [x for _,x in sorted(zip(genre_season_len,genre_name))]
    genre_season_len = sorted(genre_season_len)

    y_pos = np.arange(len(genre_name))

    plt.barh(y_pos, genre_season_len, align='center', alpha=0.5)
    plt.yticks(y_pos, genre_name)
    plt.xlabel('Number of Seasons')
    plt.title('Number of Seasons by Genre')

    plt.show()

#Movie lengths based on genre
with open('netflix_titles_nov_2019.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    #genre is key: value is array of all seasons
    genre = {}
    for row in reader:
        if row["type"] != "Movie":
            continue

        show_seasons = int(row["duration"].split(" ")[0])

        show_genres = [x.strip() for x in row["listed_in"].split(",")]
        for show_genre in show_genres:
            if show_genre in genre:
                genre[show_genre].append(show_seasons)
            else:
                genre[show_genre] = [show_seasons]

    #Calculate season averages of each genre
    genre_name = []
    genre_season_len = []
    for g_name in genre.keys():
        genre_name.append(g_name)
        genre_season_len.append(mean(genre[g_name]))

    #Sort by season
    genre_name = [x for _,x in sorted(zip(genre_season_len,genre_name))]
    genre_season_len = sorted(genre_season_len)

    y_pos = np.arange(len(genre_name))

    plt.barh(y_pos, genre_season_len, align='center', alpha=0.5)
    plt.yticks(y_pos, genre_name)
    plt.xlabel('Number of Minutess')
    plt.title('Number of Minutes by Genre')

    plt.show()

#Movies that have "kill" based on genre
while True:
    search_word = input("Type a word to search: ")
    with open('netflix_titles_nov_2019.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #genre is key: value count of movies with the keyword
        genre = {}
        for row in reader:
            # if row["type"] != "Movie":
            #     continue
            if search_word.lower() not in row["title"].lower() and search_word.lower() not in row["description"].lower():
                continue

            show_genres = [x.strip() for x in row["listed_in"].split(",")]
            for show_genre in show_genres:
                if show_genre in genre:
                    genre[show_genre] += 1
                else:
                    genre[show_genre] = 1

        #Calculate season averages of each genre
        genre_name = []
        genre_season_len = []
        for g_name in genre.keys():
            genre_name.append(g_name)
            genre_season_len.append(genre[g_name])

        #Sort by season
        genre_name = [x for _,x in sorted(zip(genre_season_len,genre_name))]
        genre_season_len = sorted(genre_season_len)

        y_pos = np.arange(len(genre_name))

        plt.barh(y_pos, genre_season_len, align='center', alpha=0.5)
        plt.yticks(y_pos, genre_name)
        plt.xlabel('Number of times showed up')
        plt.title('Number of times "'+search_word+'" appeared in Netflix Shows and Movies by Genre')

        plt.show()

        

    


for k in genre.keys():
    print(k)


