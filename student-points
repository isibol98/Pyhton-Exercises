import json
import os

class Student:
    def __init__(self, name, surname, point1, point2, point3):
        self.name = name
        self.surname = surname
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

class StudentPoints:
    def __init__(self):
        self.students = []

    def read_points(self):
        if os.path.exists('exam_points.json'):
            with open('exam_points.json', 'r', encoding='utf-8') as file:
                students = json.load(file)
                print(students)
        else:
            print('You have not saved any points.')
    def enter_points(self, student):
        self.students.append(student)
        
        print('Done!')
        
    def save(self):
        list = []
        for student in self.students:
            list.append(json.dumps(student.__dict__))

        with open("exam_points.json", "w", encoding="utf-8") as file:
            json.dump(list,file)
        print('Save Succesful!')

points = StudentPoints()

while (True):
    options = input('1- Read Points\n2- Enter Points\n3- Save\n4- Exit\nI want = ')
    if options == '4':
        break
    else:
        if options == '1':
            points.read_points()
        elif options == '2':
            name = input("Student's Name: ")
            surname = input("Studen's Surname: ")
            point1 = input("Point 1: ")
            point2 = input("Point 2: ")
            point3 = input("Point 3: ")
            student = Student(name, surname, point1, point2, point3)
            points.enter_points(student)
        elif options == '3':
            points.save()
        else:
            print('Unable. Please enter again.')
    