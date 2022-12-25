from sqlalchemy import create_engine, MetaData

# "mysql+pymysql://root@localhost:3306/fastApi"

engine = create_engine("sqlite:///database.sqlite3")  # sqlite:///database.db
# engine.execute("USE teste")
# engine.execute("CREATE TABLE IF NOT EXISTS users")
meta = MetaData()
conn = engine.connect()
# engine.execute("""CREATE TABLE users (
#       id integer primary key autoincrement,
#      name text,
#       email text,
#       password text
#    );""")


"""
CREATE TABLE tbl2 (
   ...>   f1 varchar(30) primary key,
   ...>   f2 text,
   ...>   f3 real
   ...> );
"""