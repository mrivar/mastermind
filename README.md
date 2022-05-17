# Mastermind Game

This Django app runs a server executing a API to play the Mastermind game.

## Endpoints

This API is composed of 3 simple endpoints:

- A POST endpoint to create a new game.
- A GET endpoint to retrieve the current state of a game, with the
all its information.
- A POST endpoint to create a new guess for an on-going game.


## How to use

### Run server
In order to run the server you can either run it locally using the django default server
(it will run in `localhost:8000`). You might want to use a `venv` to do so.
```
make libs # Install needed libraries
make run # Run Django default server
```

Or you can build the docker image and run it (it will run in `localhost:8020`):
```
make docker # Build docker image
make run_docker_server # Run docker server
```


### Call the API

The route to the api will be `localhost:8000` or `localhost:8020` whne run locally,
depending on whether you used the django default server or the docker server respectively.
For these examples we will stick to `localhost:8000`.

You can check the whole app documentation in `localhost:8000/api/doc` as a swagger. 
You can call the API using httpie:
```
pip install httpie
```
You could create a game using:
```
http POST http://localhost:8000/game/ code='ABCD'
```
It will return the id of the created game, which you can use to create guesses.
Once the game is over it will raise an exception if you try to add a new guess
```
http POST http://localhost:8000/guess/ code='BCYO' game='<game_id>'
```
You can also retrieve the current game state
```
http GET http://localhost:8000/game/<game_id>
```
Or retrieve the list of all games using
```
http GET http://localhost:8000/game/
```
