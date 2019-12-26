from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from Domain.dayquotes import DayQuotes
from Infrastructure.context import DBContext
from Web.controllers import stock_controllers
from flasgger import Swagger

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

app.register_blueprint(stock_controllers.blueprint_dayquotes)
Context =DBContext(app)
swagger=Swagger(app)

@app.route('/')
def signup():   
    Context.dayquotesRepository.GetAll()    
    return   render_template("index.html")
       