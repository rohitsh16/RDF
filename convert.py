import sqlalchemy as sqla

db_str = 'postgresql://postgres:postgres@localhost:5432/postgres'
db = sqla.create_engine(db_str)

