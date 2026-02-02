from dataclasses import dataclass



@dataclass()
class Student:
    bannerid:int
    first_name:str
    last_name:str
    gpa:float
    credits:int


    def __str__(self):
        return f"""Student Object with 
BannerID: {self.bannerid}
Name: {self.first_name} {self.last_name}
Credits: {self.credits}
GPA: {self.gpa}"""


    def __lt__(self, other:'Student'):
        return self.gpa < other.gpa


