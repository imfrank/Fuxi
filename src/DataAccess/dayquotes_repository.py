from Domain.dayquotes import DayQuotes
from repositorybase import RepositoryBase
#日行情 仓储
class DayquotesRepository(RepositoryBase):
    def __init__(self, app, db):
        super(DayquotesRepository, self).__init__(db)

    def get_by_code(self, code):
        try:
            return self.session().query(DayQuotes).filter_by(code=code).one()
        except:
            return None