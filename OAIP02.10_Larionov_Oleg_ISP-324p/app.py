from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {
        "id": 1,
        "title": "Интерстеллар",
        "year": 2014,
        "rating": 8.7,
        "genre": "Фантастика",
        "description": "Фильм о путешествии через черную дыру ради спасения человечества."
    },
    {
        "id": 2,
        "title": "Матрица",
        "year": 1999,
        "rating": 8.5,
        "genre": "Фантастика",
        "description": "Хакер узнает, что реальность - это симуляция машин."
    },
    {
        "id": 3,
        "title": "Шрек",
        "year": 2001,
        "rating": 8.1,
        "genre": "Мультфильм",
        "description": "Огр отправляется спасать принцессу и находит друзей."
    },
    {
        "id": 4,
        "title": "Начало",
        "year": 2010,
        "rating": 8.8,
        "genre": "Фантастика",
        "description": "Вор проникает в сны, чтобы украсть идею из подсознания."
    },
    {
        "id": 5,
        "title": "Король Лев",
        "year": 1994,
        "rating": 8.5,
        "genre": "Мультфильм",
        "description": "Львенок Симба возвращается, чтобы занять место отца."
    }
]


@app.route("/")
def index():
    return render_template("index.html", movies=movies)


@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return render_template("movie.html", movie=movie)

    return "Фильм не найден", 404


if __name__ == "__main__":
    app.run(debug=True)