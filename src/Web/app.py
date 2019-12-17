from flask import Flask, render_template, url_for, request

import Infrastructure.context
app = Flask(__name__)

# secret key neccessary for form submission, encryption, etc
app.config['SECRET_KEY'] = 'aBcDeFgHiJkLmNoP123'

#Context = app.config["CONTEXT_FACTORY"](app)

@app.route('/')
def signup():
   return  render_template('../templates/index.html')

       