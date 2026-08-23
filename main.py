from fastapi import FastAPI, Depends, HTTPException, status
from database import engine, SessionLocal
import models, schemas
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/home")
async def home():
    return{
        "Message":"This API is for Students Managment Records",
        "Message":"Database Connected Successfully"
    }

@app.post("/add_student", response_model=schemas.ResponceStudents)
async def addstd(add_studet: schemas.CreateStudents, db: Session = Depends(get_db)):
    addstud = models.Students(
        name = add_studet.name,
        email = add_studet.email,
        grade = add_studet.grade
    )

    db.add(addstud)
    db.commit()
    db.refresh(addstud)

    return addstud
        

@app.get("/see_std", response_model=list[schemas.ResponceStudents])
async def see_stud(db: Session = Depends(get_db)):
    return db.query(models.Students).all()

@app.get("/see_student/{id}", response_model=schemas.ResponceStudents)
async def see_std(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Students).filter(models.Students.id == id).first()

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student Not FOund"
        )
    
    return student

@app.put("/update_std/{id}", response_model=schemas.ResponceStudents)
async def updatestd(id: int, student: schemas.ResponceStudents, db: Session = Depends(get_db)):
    exist_std = db.query(models.Students).filter(models.Students.id == id).first()

    if not exist_std:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student's Not Found"
        )
    
    exist_std.name = student.name
    exist_std.email = student.email
    exist_std.grade = student.grade

    db.commit()
    db.refresh(exist_std)

    return exist_std


@app.delete("/delete/{id}")
async def delet_std(id: int, db: Session = Depends(get_db)):
    deltstd = db.query(models.Students).filter(models.Students.id == id).first()

    if not deltstd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student Not Found"
        )
    
    db.delete(deltstd)
    db.commit()
    return{
        "Message":"Student delete Successfully"
    }