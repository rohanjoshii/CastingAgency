# Casting Agency

Udacity Capstone Final Project
A casting agency that lists both movies and actors. This API allows different roles to read, add, change, and delete movies and actors

This application is deployed to Heroku at the link https://thawing-beyond-72939.herokuapp.com

## Getting Started

### Installing Dependencies

Recommended for interacting with this project are the following:

- Python 3.7+
- Virtual Environment
- PIP Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Authentication and Authorization

To generate a JSON web token to include in Postman requests which interact with the database, visit the following url:

```bash
https://rohanjoshi03.us.auth0.com/authorize?audience=Casting&response_type=token&client_id=lp7nVfQysF3Q2FSta2R4G7ZfA5HarJHE&redirect_uri=https://thawing-beyond-72939.herokuapp.com/login-results
```

At this site, you will be prompted to login. Use the following login information for whichever role you choose

Casting Assistant (can view actors and movies)

Email: castingassistant@casting.com
Password: Assistant1234

Casting Director (Casting Assistant permissions + can add/delete actors and modify actors and movies)

Email: castingdirector@casting.com
Password: Director1234

Executive Producer (Casting Director permissions + can add/delete movies)

Email: executiveproducer@casting.com
Password: Exec1234


## Testing

To run the test_app.py tests, use source setup.sh to set your environment variables, run createdb casting_test, and then run python test_app.py

## Endpoints

```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code.

Endpoints
GET '/movies'
GET '/actors'
POST '/movies'
POST '/actors'
PATCH '/movies/<int:movie_id>'
PATCH '/actors/<int:actor_id>'
DELETE '/movies/<int:movie_id>'
DELETE '/actors/<int:actor_id>'

GET '/movies'
- Fetches a dictionary of movies
- Request Arguments: None
- Example Response:
{
  "movies": [
{
  "actors": [],
  "id": 56,
  "release_date": "Fri, 24 Jul 2020 00:00:00 GMT",
  "title": "Title"
}
],
"success": true
}


GET '/actors'
- Fetches a dictionary of actors
- Request Arguments: None
- Example Response:

{
  "actors": [
    {
      "age": 42,
      "gender": "M",
      "id": 5,
      "movies": [],
      "name": "Name"
    }
    ],
    "success": true
  }


POST '/movies'
- Creates a new movie
- Request body: {title:string, release_date:string}
- Example Response:
{
  'created': '1',
  'success': True
  }

POST '/actors'
- Creates a new actor
- Request body: {name:string, age:int, gender:string}
- Example Response:
{
  'created': '1',
  'success': True
  }



PATCH '/movies/<int:movie_id>'
- Updates an existing movie
- Request body: {title:string, release_date:string}
- Example Response:
{
  'updated': {
      "actors": [],
      "id": 40,
      "release_date": "Thu, 23 Jul 2020 00:00:00 GMT",
      "title": "Title"
    },
  'success': True
  }

PATCH '/actors/<int:actor_id>'
- Updates an existing actor
- Request body: {name:string, age:int, gender:string}
- Example Response:
{
  'updated': {
      "movies": [],
      "id": 40,
      "gender": "Male",
      "age": 34,
      "name": "Name"
    },
  'success': True
  }

DELETE '/movies/<int:movie_id>'
- Deletes a specific movie
- Request Arguments: movie_id
- Example Response:
{
  'deleted': '1',
  'success': True
  }

DELETE '/actors/<int:actor_id>'
- Deletes a specific actor
- Request Arguments: actor_id
- Example Response:
{
  'deleted': '1',
  'success': True
  }


```
