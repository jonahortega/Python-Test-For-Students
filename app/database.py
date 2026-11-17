from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

engine = create_engine('postgresql+psycopg2://jonahortega@localhost:5432/jonahortega')

class Result(Base):
    __tablename__ = 'results'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)
    total_questions = Column(Integer)
    selected_difficulty = Column(String)
    percentage = Column(Float)
    
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
    

