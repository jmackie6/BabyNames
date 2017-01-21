import os
import csv
import tmdbsimple as tmdb
import re
import json
import requests



# start_year = 1940
# this_year = 2016
#
# func(x, y)
#
# for year from start year to this_year
#   actors = []
#   character_names = []
#   top_x_movies[] = top x movies from year
#   for movie in top_x_movies
#     actors += movie.actors
#     character_names += movie.char_names
#
#   for name in actors, character_names
#     for year in range(y)(ex. year-5 to year+5)
# 	for file_name in files
# 		if file_name has year
# 			for baby_names in file
# 				is baby_name in name

class MovieNameStudy:

    def __init__(self, year, span, pages):
        tmdb.API_KEY = 'e026cff454ca0e6e446e959e87c05bcf'
        self.year = year
        self.span = span
        self.pages = pages
        self.name_results = {}
        self.get_names()


        self.get_cast_names()
        # kwargs = {'primary_release_year':self.year, 'page':'1'}
        # disc_obj = tmdb.Discover()
        # top = disc_obj.movie(**kwargs)
        # movies = top['results']
        # movie_ids = []
                # for item in movies:
                #     movie_ids.append(item['id'])
                # for id in movie_ids:
                #     movie = tmdb.Movies(id)
                #     response = movie.info()
                #     genre = movie.info()['genres']
                #     genres = [g['name'] for g in genre]
                # print("GENRES: ",genres)
        for i in self.name_results:
            if self.name_results[i].movies:
                #print(i)

                for k in self.name_results[i].movies:
                    print("MOVIE: ", k, self.name_results[i].movies[k])

                    #print("GENRES: ", self.name_results[i].movies)
                print("NAME: ",i)
                for j in self.name_results[i].occurances:
                    print("\t", j,": ", self.name_results[i].occurances[j])
                #print("MOVIES: ", self.name_results[i].movies)
                print("\n")

    class Name:
        def __init__(self, name, year, num):
            self.name = name
            self.occurances = {year: num}
            self.movies = {}

        def add_year(self, add_year, num):
            if add_year in self.occurances:
                self.occurances[add_year] = int(self.occurances[add_year]) + int(num)
            else:
                self.occurances[add_year] = num


    def count_instances(self, movie_name, names_list):
        # Store the names and num of babies born with that name for every name that showed up in the movie
        names_dict = {}
        for name in names_list:
            try:
                self.name_results[name].movies[movie_name] = self.year
            except KeyError:
                #print(name, "not used")
                #print("")
                name = ""

    # Read in the csv and put the names and their counts for that year into a dict
    def get_names(self):
        for i_year in (range(self.year - self.span, self.year + (self.span+ 1))):
            path = os.getcwd()
            file_path = path + '/names/yob' + str(i_year) + '.csv'
            if os.path.exists(file_path):
                print("found", i_year, "file")
                file = open(file_path, 'r')
                names = csv.reader(file)
                for i, name in enumerate(names):
                    if name[0] in self.name_results:
                        self.name_results[name[0]].add_year(i_year, name[2])
                    else:
                        self.name_results[name[0]] = self.Name(name[0], i_year, name[2])
                    #print(name)



    def has_numbers(self, input):
        return bool(re.search(r'\d', input))


    def get_cast_names(self):
        # Get the  top movies for a year (10 per page)
        kwargs = {'primary_release_year':self.year, 'page':'1'}
        disc_obj = tmdb.Discover()
        top = disc_obj.movie(**kwargs)
        movies = top['results']
        movie_ids = []
        for item in movies:
            movie_ids.append(item['id'])
        for id in movie_ids:
            movie = tmdb.Movies(id)
            response = movie.info()
            print("\nMOVIE TITLE:",movie.title)
            #print("GENRES:",movie.genres)
            cast = movie.credits()['cast']
            genre = movie.info()['genres']
            genre_list = []
            genres = [g['name'] for g in genre]

            print("GENRES: ",genres)

            names_list = []
            for value in cast:
                if not self.has_numbers(value['character']):
                    for n in value['character'].split(' '):
                        if n == '(voice)' or n is '/' or n is '|':
                            continue
                        names_list.append(n)
                for n in value['name'].split(' '):
                    names_list.append(n)
            #print("CHARACTER/ACTOR NAMES:",names_list, "\n")
            self.count_instances(movie.title, names_list)

MovieNameStudy(1885, 5, 2)