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
    
def save_result_db(result):
    session = SessionLocal()

    row = Result(
        name=result["name"],
        score = result["score"],
        total_questions = result["total_questions"],
        selected_difficulty = result["selected_difficulty"],
        percentage=result["percentage"]
    )
    session.add(row)
    session.commit()
    session.close()
    
    
def load_results_db():
    session = SessionLocal()
    rows = session.query(Result).all()
    
    results = []
    
    for r in rows:
        results.append({
            "id": r.id,
            "name": r.name,
            "score": r.score,
            "total_questions": r.total_questions,
            "selected_difficulty": r.selected_difficulty,
            "percentage": r.percentage,
        })
    session.close()
    return results
