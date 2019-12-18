class DBContext(object):
    #初始化
    def __init__(self,app):
        from flask_sqlalchemy import SQLAlchemy     
        from DataAccess import dayquotes_repository   
        db = SQLAlchemy(app)
        self.db = db
        self.dayquotesRepository =dayquotes_repository.DayquotesRepository(app, db)
    #设置
    def setup(self):
        self.db.create_all()
