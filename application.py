from flask import Flask, jsonify,render_template, redirect, request
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/fxg/dev/web/flask-ajax/db.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/search")
# def search():
    ## movies = db.execute("SELECT title FROM movie ORDER BY RANDOM LIMIT=20 WHERE title LIKE ?", "%" + request.args.get("q") + "%")
    # result = db.engine.execute(
    #     "SELECT title FROM movie WHERE title LIKE ? LIMIT 15", "%" + request.args.get("q") + "%")
    ## movies = db.engine.execute(
    ##     "SELECT title FROM movie ORDER BY RANDOM() LIMIT 60")
    
    # movie_titles = []

    # for r in result:
    #     movie_titles.append({
    #         "title": r.title
    #     })

    # return jsonify(movie_titles)
