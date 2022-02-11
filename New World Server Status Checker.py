import requests
import json
import sys

def serverInput(y):
       apiKey = y
       while True:
              print("Enter 'List' To See All Servers/Status!")
              print("Or Enter Server Name To See Status!")
              print("Or Enter 'E' To Stop The Program!")
              serverInput = input("Server Input: ").lower()
              if serverInput == "":
                     print("Invalid Server Name")
              elif serverInput == "list":
                     serverInput = ""
                     serverRequest(serverInput, apiKey)
              elif serverInput == "e":
                     exit()
              else:
                     print("==========================================")
                     serverRequest(serverInput, apiKey)
                            
def serverRequest(x,y):
       serverInput = x
       apiKey = y
       url = "https://new-world-server-status.p.rapidapi.com/servers/" + serverInput
              
       headers = {
              'x-rapidapi-host': "new-world-server-status.p.rapidapi.com",
              'x-rapidapi-key': apiKey
              }

       response = requests.request("GET", url, headers=headers)

       jsonResponse = response.json()
       if jsonResponse == [None]:
              print("Invalid Server Name")
              print("==========================================")
       else:
              for item in jsonResponse:
                     serverName = item['ServerName']
                     serverStatus = item['ServerStatus']
                     print(serverName + " " + "Is Currently: " + serverStatus)
                     print("==========================================")

def APIFileSetup():
       try:
              f = open("NewWorldStatusAPIKey.txt","r")
              apikey = f.read()
              f.close()
              defaultServerFile(apikey)
       except FileNotFoundError:
              f = open("NewWorldStatusAPIKey.txt","w")
              f.close()
              keyInput()

def keyInput():
       while True:
              keyInput = input("Please Input Your API Key: ")
              if keyInput == "":
                     print("Invalid API key")
              else:
                     f = open("NewWorldStatusAPIKey.txt","w")
                     f.write(keyInput)
                     f = open("NewWorldStatusAPIKey.txt","r")
                     apiKey = f.read()
                     defaultServerFile(apiKey)
                     break

def defaultServerFile(apikey):
       key = apikey
       try:
              f = open("defaultServer.txt","r")
              defaultServer = f.read()
              f.close()
       except FileNotFoundError:
              f = open("defaultServer.txt","w")
              placeholder = "Bifrost"
              f.write(placeholder)
              f = open("defaultServer.txt","r")
              defaultServer = f.read()
              f.close()
       print("==========================================")
       print("Default Server Is: " + defaultServer)
       serverRequest(defaultServer, key)
       changeDefaultServer(key)

def changeDefaultServer(apiKey):
       key = apiKey
       while True:
              changeDefault = input("Do You Want To Change Your Default Server? Enter Y(yes) or N(no): ").lower()
              print("==========================================")
              if changeDefault == "y":
                     while True:
                            defaultServer = input("Please Enter Your New Default Server: ")
                            if defaultServer == "":
                                   print("Invalid Server Name")
                            else:
                                   f = open("defaultServer.txt","w")
                                   f.write(defaultServer)
                                   f.close()
                                   print("==========================================")
                                   break
              elif changeDefault == "n":
                     serverInput(key)
                     break
              else:
                     print("Invalid Input")
                     print("==========================================")
                                 

if __name__ == "__main__":
       APIFileSetup()
       
