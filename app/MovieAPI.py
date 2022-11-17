from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "null"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Movie(BaseModel):
    name: str
    year: int
    genre: str
    director: str
    actors: str
    description: str

class UpdateMovie(BaseModel):
    name: Optional[str] = None
    year: Optional[int] = None
    genre: Optional[str] = None
    director: Optional[str] = None
    actors: Optional[str] = None
    description: Optional[str] = None
movies = []
movies.append(Movie(name="Fight Club", year=1999, genre="Drama", director="David Fincher",actors="Brad Pitt, Edward Norton Meat Loaf", description="An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more."))
movies.append(Movie(name="Inception", year=2010, genre="Action, Adventure, Sci-Fi", director="Christopher Nolan",actors="Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page", description="A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO."))
movies.append(Movie(name="The Dark Knight", year=2008, genre="Action, Crime, Drama", director="Christopher Nolan", actors="Christian Bale, Heath Ledger, Aaron Eckhart, Michael Caine", description="When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice."))
movies.append(Movie(name="The Lord of the Rings: The Return of the King", year=2003, genre="Action, Adventure, Drama", director="Peter Jackson", actors="Elijah Wood, Viggo Mortensen, Ian McKellen, Orlando Bloom", description="Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring."))
movies.append(Movie(name="Avengers Endgame", year=2019, genre="Action, Adventure, Drama", director="Anthony Russo, Joe Russo", actors="Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth", description="After the devastating events of Avengers: Infinity War, the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe."))
movies.append(Movie(name="Transformers", year=2007, genre="Action, Adventure, Sci-Fi", director="Michael Bay", actors="Shia LaBeouf, Megan Fox, Josh Duhamel, Tyrese Gibson", description="Young teenager, Sam Witwicky becomes involved in the ancient struggle between two extraterrestrial factions of transforming robots - the heroic Autobots and the evil Decepticons. Sam holds the clue to unimaginable power and the Decepticons will stop at nothing to retrieve it."))
movies.append(Movie(name="Black Panther", year=2018, genre="Action, Adventure, Sci-Fi", director="Ryan Coogler", actors="Chadwick Boseman, Michael B. Jordan, Lupita Nyong'o, Danai Gurira", description="T'Challa, the King of Wakanda, rises to the throne in the isolated, technologically advanced African nation, but his claim is challenged by a vengeful outsider who was a childhood victim of T'Challa's father's mistake."))
movies.append((Movie(name="Avatar", year=2009, genre="Action, Adventure, Fantasy", director="James Cameron", actors="Sam Worthington, Zoe Saldana, Sigourney Weaver, Michelle Rodriguez", description="A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.")))
movies.append(Movie(name="Sound of Music", year=1965, genre="Musical", director="Robert Wise", actors="Julie Andrews, Christopher Plummer, Eleanor Parker, Richard Haydn", description="Maria, a free-spirited nun in Austria, is sent to serve as governess to the seven children of a widowed naval captain."))
movies.append(Movie(name="Lightyear", year=2022, genre="Animation, Adventure, Comedy", director="Daveed Diggs, Justin K. Thompson", actors="Chris Evans, Jamie Foxx, Tessa Thompson, Phylicia Rashad", description="Based on the popular '90s toy line, this animated adventure follows a young space ranger who dreams of becoming a real astronaut."))
movies.append(Movie(name="Minions: The Rise of Gru", year=2022, genre="Animation, Adventure, Comedy", director="Kyle Balda, Pierre Coffin", actors="Pierre Coffin, Steve Carell, Kristen Wiig, Trey Parker", description="Gru meets his long-lost charming, cheerful, and more successful twin brother Dru who wants to team up with him for one last criminal heist."))



@app.get("/movies")
def get_movies():
    return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    if movie_id > len(movies):
        return {"error": "Movie ID out of range"}
    return movies[movie_id]
@app.get("/movies/search")
def search_movies(name: Optional[str] = None):
    if name:
        movies_by_name = []
        for i in movies:
            if name in i.name:
                movies_by_name.append(i)
            return movies_by_name




@app.post("/movies")
def add_movie(movie: Movie):
    for i in movies:
        if i.name == movie.name and i.year == movie.year and i.director == movie.director:
            return {"error": "Movie already exists"}
    movies.append(movie)
    return movies[-1]

@app.get("/movies/genre/{genre}")
def get_movies_by_genre(genre: str):
    movies_by_genre = []
    for i in movies:
        if genre in i.genre:
            movies_by_genre.append(i)
    if len(movies_by_genre) == 0:
        return {"error": "No movie found with genre " + genre}
    return movies_by_genre

@app.get("/movies/name/{name}")
def get_movies_by_name(name: str):
    movies_by_name = []
    for i in movies:
        if name in i.name:
            movies_by_name.append(i)
    if len(movies_by_name) == 0:
        return {"error": "No movie found with name " + name}
    return movies_by_name

@app.get("/movies/director/{director}")
def get_movies_by_director(director: str):
    movies_by_director = []
    for i in movies:
        if director in i.director:
            movies_by_director.append(i)
    if len(movies_by_director) == 0:
        return {"error": "No movie found with director " + director}
    return movies_by_director

@app.get("/movies/actor/{actor}")
def get_movies_by_actor(actor: str):
    movies_by_actor = []
    for i in movies:
        if actor in i.actors:
            movies_by_actor.append(i)
    if len(movies_by_actor) == 0:
        return {"error": "No movie found with actor " + actor}
    return movies_by_actor


@app.get("/movies/year/{year}")
def get_movies_by_year(year: int):
    movies_by_year = []
    for i in movies:
        if year == i.year:
            movies_by_year.append(i)
    if len(movies_by_year) == 0:
        return {"error": "No movie found with year " + str(year)}
    return movies_by_year

@app.post("/movies/{movie_id}")
def update_movie(movie_id: int, movie: UpdateMovie):
    if movie_id > len(movies) or movie_id < 1:
        return {"error": "Movie ID out of range"}
    movies[movie_id - 1] = movie
    return movies[movie_id - 1]

