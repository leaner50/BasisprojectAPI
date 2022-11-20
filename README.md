# BasisprojectAPI

## Table of Contents

- [Description of the project](#description-of-the-project)
- [Theme of the project](#theme-of-the-project)
- [Github repository](#github-repository)
- [The API](#the-api)
- [API Frontend](#api-frontend)
- [Working API pictures using Postman](#working-api-pictures-using-postman)
- [Screenshot of the API docs](#screenshot-of-the-api-docs)


## Description of the project

This is a project that contains my for API development for the Basisproject.

## Theme of the project

I choose to make an API about movies because i'm a big fan of movies. It's alose a good theme to work with because there are a lot of movies and it's easy to find information about it.


## Github repository
Url: https://github.com/leaner50/BasisprojectAPI

## The API
The api contains movies that have the following paramters : name, year, genre, director, actors, description.
The API is developed using the FastAPI framework. 
The API is used to communicate with python files and the frontend. The API is can be used to create a new movie, display all the movies, search the movies by given id and can give all the movies that contain the given genre.

Url: https://movies-service-leaner50.cloud.okteto.net

(If this api is used regurlarly it will go to sleep and not work. If this is the case please contact me and I will wake it up)

## API Frontend
The frontend is developed using HTML, CSS and Alpine Js. The frontend can be used to communicate with the API. You can use the functions to get or post data to the api.
You can search movies by given id, display movies with a specific genre and add new movies to the api.

Url: https://leaner50.github.io/BasisprojectAPI 

![image](https://github.com/leaner50/BasisprojectAPI/blob/main/img/screencapture-frondend.png)

## Working API pictures using Postman

- Screenshot of the API when it is used to display all the movies

![image](https://github.com/leaner50/BasisprojectAPI/blob/main/img/screencapture-postman-all-movies.png)

- Screenshot of the API when it is used to display the movie with the given id

![image](https://github.com/leaner50/BasisprojectAPI/blob/main/img/screencapture-postman-search-movie-by-id.png)

- Screenshot of the API when it is used to display the movie with the given id but the id is not found

![image](https://github.com/leaner50/BasisprojectAPI/blob/main/img/screencapture-postman-search-movie-by-id-id-not-found.png)
*Screenshot of the API when it is used to display the movies with the given genre

![image](https://github.com/leaner50/BasisprojectAPI/blob/main/img/screencapture-postman-search-all-movies-with-that-genre.png)

- Screenshot of the API when it is used to display the movies with the given genre but the genre is not found

![image](https://github.com/leaner50/BasisprojectAPI/blob/main/img/screencapture-postman-search-all-movies-with-that-genre-if-genre-not-found.png)

- Screenshot of the API when it is used to create a new movie

![image](https://github.com/leaner50/BasisprojectAPI/blob/main/img/screencapture-postman-add-new-movie.png)

- Screenshot of the API when it is used to create a new movie but the movie already exists

![image](https://github.com/leaner50/BasisprojectAPI/blob/main/img/screencapture-postman-add-new-movie-already-exists.png)

## Screenshot of the API docs:
Url: https://movies-service-leaner50.cloud.okteto.net/docs

![image](https://github.com/leaner50/BasisprojectAPI/blob/main/img/screencapture-api-docs.png)

## Author
Leander Van Bael





