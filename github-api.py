from urllib import response
import requests
   
class Github:
    def __init__ (self):
        self.api_url = 'https://api.github.com'

    def getUser (self, username):
        response = requests.get(self.api_url+'/users/' + username)
        return response.json()
    def getRepos (self, username):
        response = requests.get(self.api_url+'/users/' + username+'/repos')
        return response.json()
    def createRepo (self, name):
        my_token = github.getToken()
        response = requests.post(self.api_url+'/user/repos?access_token'+my_token,json={
            "name": name,
            "description": "This is your repository.",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()
    def getToken (self):
        with open('mytoken.txt', 'r') as file:
            for i in file:
                result = i
        return result

github = Github()

while True:
    options = input("1- Find User\n2- Get Repositories\n3- Create A Repository\n4- Exit\nEnter: ")
    if options == '4':
        break
    else:
        if options == '1':
            username = input("Please enter an username: ")
            result = github.getUser(username)
            print(f"Name: {result['name']}\nPublic Repos: {result['public_repos']}\nFollowers: {result['followers']}\n")
        elif options == '2':
            username = input("Please enter an username: ")
            result = github.getRepos(username)
            for repo in result:
                print(repo['name'])
        elif options == '3':
            name = input('Please Enter A Repository Name: ')
            result = github.createRepo(name)
            print(result)
        else:
            print("Unvalid. Please try again.")
