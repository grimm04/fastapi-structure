from sqlalchemy.sql import text

from .config import database_test_config


###
# Suport test for database insertions
###

engine = database_test_config.engine


# def insert_into_cars(input):
#     ''' Insert into table cars '''
#     with engine.connect() as con:

#         data = (input, )

#         statement = text(
#             """INSERT INTO cars(id, name, year, brand) VALUES(:id, :name, :year, :brand)""")

#         for line in data:
#             con.execute(statement, **line)
 