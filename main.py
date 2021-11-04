import pandas as pd
from datetime import datetime
import json
from main_one import notify,login
import time

with open('CSE/classes.json') as f:
    courses = json.load(f) #get class links



day = datetime.today().weekday() #get today's day

data = pd.read_csv('CSE/timetable.csv') #get timetable

period = list(data.columns) #get class hour

login("USERNAME", "PASSWORD")

    
for i in range(len(period)-1):
    classes = data.iloc[0][period[i+1]]
    
    class_link = courses[classes][0]
    join_link = courses[classes][1]
    class_type = courses[classes][2]
    if classes:
        notify(class_link, join_link, class_type)
        time.sleep(4200)
      
        
        

