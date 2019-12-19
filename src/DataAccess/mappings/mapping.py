from sqlalchemy import ForeignKey, Integer, String, Boolean, Text, DateTime,DECIMAL
from sqlalchemy.orm import mapper, relationship
from Domain.dayquotes import *
from sqlalchemy import Table, MetaData, Column

def init(db):
        daystock_mapping = db.Table('dayquotes',
        db.Column('id', Integer, primary_key=True),
        db.Column('name', String(100)),
        db.Column('openingPrice',DECIMAL(10,2)),
        db.Column('closingPrice',DECIMAL(10,2)),
        db.Column('highestPrice', DECIMAL(10,2)),
        db.Column('minimumPrice', DECIMAL(10,2)),
        db.Column('transactionDate', DateTime),
        )
    
        db.mapper(DayQuotes, daystock_mapping)