from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "https://leaner50.github.io"
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

movies = {}
movies[0] = Movie(name="Fight Club", year=1999, genre="Drama", director="David Fincher",actors="Brad Pitt, Edward Norton Meat Loaf", description="An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.")
movies[1] = Movie(name="Inception", year=2010, genre="Action, Adventure, Sci-Fi", director="Christopher Nolan",actors="Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page", description="A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.")
movies[2] = Movie(name="The Dark Knight", year=2008, genre="Action, Crime, Drama", director="Christopher Nolan", actors="Christian Bale, Heath Ledger, Aaron Eckhart, Michael Caine", description="When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.")
movies[3] = Movie(name="The Lord of the Rings: The Return of the King", year=2003, genre="Action, Adventure, Drama", director="Peter Jackson", actors="Elijah Wood, Viggo Mortensen, Ian McKellen, Orlando Bloom", description="Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.")
movies[4] = Movie(name="Avengers Endgame", year=2019, genre="Action, Adventure, Drama", director="Anthony Russo, Joe Russo", actors="Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth", description="After the devastating events of Avengers: Infinity War, the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.")
movies[5] = Movie(name="Transformers", year=2007, genre="Action, Adventure, Sci-Fi", director="Michael Bay", actors="Shia LaBeouf, Megan Fox, Josh Duhamel, Tyrese Gibson", description="Young teenager, Sam Witwicky becomes involved in the ancient struggle between two extraterrestrial factions of transforming robots - the heroic Autobots and the evil Decepticons. Sam holds the clue to unimaginable power and the Decepticons will stop at nothing to retrieve it.")
movies[6] = Movie(name="Black Panther", year=2018, genre="Action, Adventure, Sci-Fi", director="Ryan Coogler", actors="Chadwick Boseman, Michael B. Jordan, Lupita Nyong'o, Danai Gurira", description="T'Challa, the King of Wakanda, rises to the throne in the isolated, technologically advanced African nation, but his claim is challenged by a vengeful outsider who was a childhood victim of T'Challa's father's mistake.")
movies[7] = Movie(name="Avatar", year=2009, genre="Action, Adventure, Fantasy", director="James Cameron", actors="Sam Worthington, Zoe Saldana, Sigourney Weaver, Michelle Rodriguez", description="A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.")
movies[8] = Movie(name="Sound of Music", year=1965, genre="Musical", director="Robert Wise", actors="Julie Andrews, Christopher Plummer, Eleanor Parker, Richard Haydn", description="Maria, a free-spirited nun in Austria, is sent to serve as governess to the seven children of a widowed naval captain.")
movies[9] = Movie(name="Lightyear", year=2022, genre="Animation, Adventure, Comedy", director="Daveed Diggs, Justin K. Thompson", actors="Chris Evans, Jamie Foxx, Tessa Thompson, Phylicia Rashad", description="Based on the popular '90s toy line, this animated adventure follows a young space ranger who dreams of becoming a real astronaut.")
movies[10]= Movie(name="Minions: The Rise of Gru", year=2022, genre="Animation, Adventure, Comedy", director="Kyle Balda, Pierre Coffin", actors="Pierre Coffin, Steve Carell, Kristen Wiig, Trey Parker", description="Gru meets his long-lost charming, cheerful, and more successful twin brother Dru who wants to team up with him for one last criminal heist.")

@app.get("/")
def read_root():
    return {"error": "Please use /movies to get all movies or /movies/{id} to get a specific movie by id or /movies/genre/{genre} to get all the movies with that specific genre"}

@app.get("/movies")
def get_movies():
    return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    if movie_id < 0:
        return {"error": "Please enter a valid id"}
    if movie_id not in movies:
        return {"error": "There is no movie with id: " + str(movie_id)}
    return movies[movie_id]


@app.get("/movies/genre/{genre}")
def get_movie_genre(genre: str):
    genreMovies = {}
    for movie_id in movies:
        if genre.lower() in movies[movie_id].genre.lower():
            genreMovies[movie_id] = movies[movie_id]
    if not genreMovies:
        return {"error": "Genre not found"}
    return genreMovies

@app.post("/movies")
def add_movie(movie: Movie):
    for movie_id in movies:
        if movie.name == movies[movie_id].name and movie.year == movies[movie_id].year:
            return {"error": "Movie already exists"}
    movies[len(movies)] = movie
    return {"success": "Movie added"}
