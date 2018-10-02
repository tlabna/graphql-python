# GraphQL-Python

A simple GraphQL server by developing a Hackernews clone using Python.

| <center>Technologies Used </center>     |
| --------------------------------------- |
| GraphQL                                 |
| Python                                  |
| Django Framework                        |
| Graphene & Graphene-Django              |
| JWT Authentication (django-graphql-jwt) |

##### To play around with it:

1. Download or clone this repo
1. `$ cd /path/to/directory`
1. Create a virtual environment `$ python3 -m venv venv`
1. Activate virtual environment `$ source venv/bin/activate`
1. Install packages and dependencies `$ pip install -r requirements.txt`
1. Run local django server `$ python hackernews/manage.py runserver`
1. Open your browser at `http://localhost:8000/graphql` to run in-browser IDE (graphiQL) to play around with the graphQL server
   - You'll find included a **`documentation`** tab that will contain information on the graphQL schema available
   - **Note.** You won't be able to test out authentication since graphiQL doesn't accept custom HTTP headers.
     - You can use the [Insomnia app](https://insomnia.rest) instead.
