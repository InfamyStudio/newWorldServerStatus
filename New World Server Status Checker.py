import requests
import json
import sys

def serverInput():
       while True:
              print("Enter 'List' To See All Servers/Status!")
              print("Or Enter Server Name To See Statuts!")
              print("Or Enter 'E' To Stop The Program!")
              serverInput = input("Server Input: ").lower()
              if serverInput == "":
                     print("Invalid Server Name")
              elif serverInput == "list":
                     serverInput = ""
                     serverRequest(serverInput)
              elif serverInput == "e":
                     exit()
              else:
                     print("==========================================")
                     serverRequest(serverInput)
                            
def serverRequest(x):
       serverInput = x
       url = "https://new-world-server-status.p.rapidapi.com/servers/" + serverInput
              
       headers = {
              'x-rapidapi-host': "new-world-server-status.p.rapidapi.com",
              'x-rapidapi-key': ""
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


def defaultServerFile():
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
       serverRequest(defaultServer)

def changeDefaultServer():
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
                                   break
                     print("==========================================")
                     break
              elif changeDefault == "n":
                     break
              else:
                     print("Invalid Input")
                     print("==========================================")
                                 

if __name__ == "__main__":   
       defaultServerFile()
       changeDefaultServer()
       serverInput()
       
