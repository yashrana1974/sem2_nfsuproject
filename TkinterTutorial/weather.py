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

root.geometry("600x200")

# Create zipcode lookup function
def zipLookup():
    # zip.get()
    # zipLabel = Label(root, text=zip.get())
    # zipLabel.grid(row=1, column=0, columnspan=2)
 
    # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=02D47AC2-D170-4FD5-B2B0-E0EE61885838


    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zip.get() +"&distance=5&API_KEY=02D47AC2-D170-4FD5-B2B0-E0EE61885838")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality =  api[0]['AQI']
        category = api[0]['Category']['Name']
        
        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"  
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"
            
        myLabel = Label(root, text=city + " Air Quality " + str(quality) +" "+ category, font=("Helvetica", 20), background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
            
        root.configure(background=weather_color)
            
    except Exception as e:
        api = "Error..."    

zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, sticky=W+E+N+S)

#creating a quit button
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonQuit.grid(row=2, column=0, columnspan=2)

#creating loop to continuosly execute the app
root.mainloop()
