from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text, insert
from sqlalchemy.sql import select


# engine = create_engine('sqlite:///task.db', echo= True)

# meta_data = MetaData()

# users_table = Table(
#     'users',
#     meta_data,
#     Column('id', Integer, primary_key= True),
#     Column('name', String),
#     Column('age', Integer)
# )

# meta_data.create_all(engine)

# with engine.connect() as connection:
#     with connection.begin():
#         connection.execute(users_table.insert(),[
#             {'name': 'Alice', 'age': 25},
#             {'name': 'Bob', 'age': 30},
#             {'name': 'Charlie', 'age': 35}
#         ])
        

# with engine.connect() as connection:
#     with connection.begin():
#         result = connection.execute(
#             users_table
#             .update()
#             .where(users_table.c.name == 'Alice')
#             .values(age=29))
#         print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
#         print("Updated Alice's age.")




# Basics of Statement Execution

# ----------------------------------------
# Retrive data from table 
# -----------------------------------------

# with engine.connect() as connection:
#     result = connection.execute(select(users_table))
#     rows = result.fetchone()
#     for row in rows:
#         print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
#         print (row)

# with engine.connect() as connection:
#     result = connection.execute(text("SELECT * FROM users WHERE name = ?"), {'name': 'Alice'})
#     for row in result:
#         print (row)


# with engine.connect() as connection:
#     result = connection.execute(text("SELECT * FROM users WHERE name = :name"), {'name': 'Alice'})
#     for row in result:
#         print(row)


# engine = create_engine('sqlite:///users.db', echo= True)


# metadata = MetaData()

# users = Table(
#     'users', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('username', String),
#     Column('email', String)
# )

# metadata.create_all(engine)

# اجرای دستور INSERT
# with engine.connect() as conn:
#     stmt = insert(users).values(username='alice', email='alice@example.com')
#     conn.execute(stmt)
#     conn.commit() 

# with engine.connect() as conn:
#     stmt = insert(users).values(username='Bouji', email='bouji@example.com') 
#     conn.execute(stmt)   
#     conn.commit()


engine = create_engine ("sqlite+pysqlite:///example.db", echo=True)

with engine.begin() as conn:
    conn.execute(
        text('INSERT INTO users (username, email) VALUES (:username, :email)'),
        {'username': 'Alice', 'email': 'alice@example.com'}
    )