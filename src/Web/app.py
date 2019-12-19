from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template
from flask_sqlalchemy import SQLAlchemy
from Domain.dayquotes import DayQuotes
from Infrastructure.context import DBContext

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

Context =DBContext(app)

@app.route('/')
def signup():  
    Context.dayquotesRepository.GetAll()    
    return   render_template("index.html")

       