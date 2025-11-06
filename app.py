from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, Book
from forms import BookForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)


@app.route("/book/<int:id>")
def detail(id):
    book = Book.query.get_or_404(id)
    return render_template("detail.html", book=book)


@app.route("/create", methods=["GET", "POST"])
def create():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            title=form.title.data,
            author=form.author.data,
            description=form.description.data,
        )
        db.session.add(book)
        db.session.commit()
        flash("Book added successfully!", "success")
        return redirect(url_for("index"))
    return render_template("create.html", form=form)


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    book = Book.query.get_or_404(id)
    form = BookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.description = form.description.data
        db.session.commit()
        flash("Book updated successfully!", "success")
        return redirect(url_for("index"))
    return render_template("update.html", form=form, book=book)


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash("Book deleted successfully!", "info")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
