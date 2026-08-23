from pydantic import BaseModel


class CreateStudents(BaseModel):
    id : int
    name : str
    email : str
    grade : str


class ResponceStudents(BaseModel):
    id : int
    name : str
    email : str
    grade : str

    class config:
        from_attribute = True