# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1
def imdb_score(movie):
    return movie["imdb"]>5.5
#2
def imdb_scoresss(movies):
    return [movie for movie in movies if movie["imdb"]>5.5]
#3
def categories(categor):
    category_movie=[]
    for i in movies:
        if i['category']==categor:
            category_movie.append(i['name'])
    return category_movie

#4
def averege_imdb(movies):
    sum=0
    for movie in movies:
        sum+=movie["imdb"]
    return sum/len(movies)
#5
def categories_imdb(categor):
    sum=0
    imdb_category=[]
    for movie in movies:
        if movie['category']==categor:
            imdb_category.append(movie['name'])
            sum+=movie['imdb']
    return sum/len(imdb_category)
print(imdb_score(movies[-2]))
print(imdb_scoresss(movies))
print(categories('Romance'))
print(averege_imdb(movies))
print(categories_imdb('Thriller'))
