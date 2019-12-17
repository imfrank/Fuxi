class DBContext(object):
    #初始化
    def __init__(self,app):
        from flask_sqlalchemy import SQLAlchemy        
        db = SQLAlchemy(app)
        self.db = db
    #设置
    def setup(self):
        self.db.create_all()
