# Auth Cafe
Full-stack Ionic & Flask-RESTful webapp powering managers, baristas, and guests in a digitally enabled cafe!

- Displays graphics representing the ratios of ingredients in each drink.
- Allows guests i.e. public users to view drink names and graphics.
- Allows baristas to see the recipe information.
- Allow  managers to create new drinks and edit existing drinks.

## Getting Started

### Backend Core Dependencies
#### Install core dependencies
```
$ pipenv install flask-restful
$ pipenv install flask-cors
$ pipenv install flask-sqlalchemy
$ pipenv install python-jose-cryptodome
```
#### Currently-installed core dependency graph information.
```
$ pipenv graph 
```
```
Flask-Cors==3.0.8
  - Flask [required: >=0.9, installed: 1.1.1]
    - click [required: >=5.1, installed: 7.0]
    - itsdangerous [required: >=0.24, installed: 1.1.0]
    - Jinja2 [required: >=2.10.1, installed: 2.10.3]
      - MarkupSafe [required: >=0.23, installed: 1.1.1]
    - Werkzeug [required: >=0.15, installed: 0.16.0]
  - Six [required: Any, installed: 1.13.0]
Flask-RESTful==0.3.7
  - aniso8601 [required: >=0.82, installed: 8.0.0]
  - Flask [required: >=0.8, installed: 1.1.1]
    - click [required: >=5.1, installed: 7.0]
    - itsdangerous [required: >=0.24, installed: 1.1.0]
    - Jinja2 [required: >=2.10.1, installed: 2.10.3]
      - MarkupSafe [required: >=0.23, installed: 1.1.1]
    - Werkzeug [required: >=0.15, installed: 0.16.0]
  - pytz [required: Any, installed: 2019.3]
  - six [required: >=1.3.0, installed: 1.13.0]
Flask-SQLAlchemy==2.4.1
  - Flask [required: >=0.10, installed: 1.1.1]
    - click [required: >=5.1, installed: 7.0]
    - itsdangerous [required: >=0.24, installed: 1.1.0]
    - Jinja2 [required: >=2.10.1, installed: 2.10.3]
      - MarkupSafe [required: >=0.23, installed: 1.1.1]
    - Werkzeug [required: >=0.15, installed: 0.16.0]
  - SQLAlchemy [required: >=0.8.0, installed: 1.3.11]
python-jose-cryptodome==1.3.2
  - ecdsa [required: <1.0, installed: 0.14.1]
    - six [required: Any, installed: 1.13.0]
  - future [required: <1.0, installed: 0.18.2]
  - pycryptodome [required: >=3.3.1,<3.4.0, installed: 3.3.1]
  - six [required: <2.0, installed: 1.13.0]
```
#### Install code quality dependencies
```
$ pipenv install flake8  --dev
$ pipenv install black==19.3b0 --dev
$ pipenv install isort --dev
```

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:drinks-detail`
    - `post:drinks`
    - `patch:drinks`
    - `delete:drinks`
6. Create new roles for:
    - Barista
        - can `get:drinks-detail`
    - Manager
        - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 2 users - assign the Barista role to one and Manager role to the other.
    - Sign into each account and make note of the JWT.
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.
    - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`
