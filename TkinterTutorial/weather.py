from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import requests
import json

root = Tk()
#Title for the window
root.title("Learn To Code at Codemy.com")

#Image icon for tool icon
root.iconbitmap("TkinterTutorial\\christmas-tree.ico")

root.geometry("400x60")

root.configure(background="green")
 
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=02D47AC2-D170-4FD5-B2B0-E0EE61885838


try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=02D47AC2-D170-4FD5-B2B0-E0EE61885838")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality =  api[0]['AQI']
    category = api[0]['Category']['Name']
except Exception as e:
    api = "Error..."    

myLabel = Label(root, text=city + " Air Quality " + str(quality) +" "+ category, font=("Helvetica", 20), background="green")
myLabel.pack()

#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.pack()

#creating loop to continuosly execute the app
root.mainloop()
