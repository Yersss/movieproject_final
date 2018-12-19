# Movie Recommender System "Qino Qoru"
We have created a movie websirt using **Django** as backend framework, SQLite3 as database.

## Data and DB
1600+ movie from this [movie dataset](https://grouplens.org/datasets/movielens/) are the origin data source.
Then we filter them and there are about **1000 movies** movies in database

The database file is 'db.sqilte3' in the root directory

##Recommender
It takes all genres from list of seen movies and finally system will recommend **same genres** to user in profile page

## Deployment Instructions
1. Install [**Python 3**]( https://www.python.org/) in your computer, and make sure to set environment variable correctly.
2. Install **Django** for the Python environment. The easiest way is to use pip by running `pip install django`.
3. Open a terminal, input command: `python manage.py runserver 8080`
4. Open your web browser, input `localhost:8080` in the address bar.
- P.S. If you fail running `python manage.py runserver 8080`.
