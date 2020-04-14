from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def acceuil():
    courses_titles = ["Title 1", "Title2", "Title3"]
    categories = ["Marketing" , "Social Network", "Entrepreneurship", "Subject N° ...", "Subject N° ..", "Subject N° .."]
    return render_template("accueil.html", courses_titles = courses_titles, categories = categories)
