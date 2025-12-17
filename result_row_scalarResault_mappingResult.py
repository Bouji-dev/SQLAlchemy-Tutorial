from sqlalchemy import create_engine, select, text, Table, Column, Integer, String, MetaData


engine = create_engine("sqlite+pysqlite:///example.db", echo=True, future=True)


metadata = MetaData()
users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String),
    Column('email', String)
)
rows = [
    {"username": "bob", "email": "bob@example.com"},
    {"username": "carol", "email": "carol@example.com"},
    {"username": "dave", "email": "dave@example.com"},
]

with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO users (username, email) VALUES (:username, :email)"),
        rows,
    )
metadata.create_all(engine)

stmt = select(users.c.id, users.c.username, users.c.email)

with engine.connect() as conn:
    result = conn.execute(stmt)
    rows = result.all()  #list[Row]
    # print(rows)


stmt = select(users.c.username)
with engine.connect() as conn:
    usernames = conn.execute(stmt).scalars().all() # ['alice', 'bob', ...]
    # print(usernames)

stmt = select(users.c.id, users.c.username)

with engine.connect() as conn:
    data = conn.execute(stmt).mappings().all()
    print(data)  #[{'id': 1, 'username': 'alice'}, ...]


stmt = select(users).where(users.d.username == 'alice')
with engine.connect() as conn:
    row = conn.execute(stmt).first() # row | None
    value = conn.execute(select(users.c.id)).scalar() # first row first column
    print({'row': row, 'value': value})