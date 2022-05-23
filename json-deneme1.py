import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password 
        self.email = email 

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
    def loadUsers (self):
        if os.path.exists('users1.json'):
            with open('users1.json', 'r', encoding='utf-8') as file:
                users = json.load(file)   
    def register (self, user: User):
        self.users.append(user)
        self.saveToFile()
        print('Register Complete!')
    def login (self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Login Succesful!')
                break
        else:
            print('Incorrect usarname or password.')
    def logout (self):
        self.isLoggedIn = False
        print('Logout Succesful.')
    def identity (self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}\nemail: {self.currentUser.email}')
        else:
            print('Please login.')
    def saveToFile (self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        
        with open('users1.json', 'w', encoding='utf-8') as file:
            json.dump(list, file)



repository = UserRepository()

while(True):
    print('Menu'.center(50,'*'))
    option = input('1 -Register\n2 -Login\n3 -Logout\n4 -My Profile\n5 -Exit\nYour option: ')
    if option == '5':
        break
    else:
        if option == '1':
            username = input('username: ')          
            password = input('password: ')          
            email = input('email: ')          

            user = User(username, password, email)
            repository.register(user)
        elif option == '2':
            if repository.isLoggedIn:
                print('You have already logged in!')
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username, password)
        elif option == '3':
            repository.logout()
        elif option == '4':
            repository.identity()
        else:
            print('Unvalid. Please try again.')