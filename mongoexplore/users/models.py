from django.db import models
from mongoengine import *

# Create your models here.

class Employee(EmbeddedDocument):
    employee_id = StringField(required=True)
    designation = StringField(max_length=50)
    

class Student(EmbeddedDocument):
    student_id = IntField(required=True)
    grade = StringField(max_length=50)
    
    

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    employees = ListField(EmbeddedDocumentField(Employee))
    students = ListField(EmbeddedDocumentField(Student))
    

'''
class CustomUser(User):
    phone = StringField(required=True)
'''