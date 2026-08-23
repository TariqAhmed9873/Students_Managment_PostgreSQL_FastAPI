from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:karachi.90@localhost:5432/student_db"

engine = create_engine(
    DATABASE_URL,
    # connect_args=False,
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()