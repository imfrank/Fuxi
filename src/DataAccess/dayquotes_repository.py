from Domain.dayquotes import DayQuotes
from DataAccess.repositorybase import RepositoryBase
#日行情 仓储
class DayquotesRepository(RepositoryBase):
    def __init__(self, app, db):
         super(DayquotesRepository, self).__init__(db)

    def GetAll(self):
         self.session().query(DayQuotes).all()
