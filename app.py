from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

"""
create secret key: 
import secrets
secrets.token_hex(16)
"""

app.config['SECRET_KEY'] = '4de8d73dbee7bf5c8d05dc4a61403ceb'

posts = [
  {
    'author': 'John Zorn',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'April 1, 2020'
  },
  {
    'author': 'Jane Doe',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'April 21, 2025'
  }
]

@app.route("/home")
@app.route("/")
def home():
  return render_template('home.html', posts=posts)

@app.route("/about")
def about():
  return render_template('about.html', title='About')

@app.route("/register")
def register():
  form = RegistrationForm()
  return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
  form = LoginForm()
  return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
  app.run(debug=True)