import pickle
import time

import dill
import pandas as pd
from pyrebase import pyrebase


data = pd.read_pickle("/home/retro/Desktop/projectepidemic/Main_Codes/27Features.pkl")


with open('/home/retro/Desktop/projectepidemic/Main_Codes/27Features.pkl', 'rb') as fh: # Load data set
            X = dill.load(fh)
X.drop(X.columns[[0, 1, 2]], axis = 1, inplace = True)
with open('/home/retro/Desktop/projectepidemic/Main_Codes/y.pkl', 'rb') as fh:
            y = dill.load(fh)

with open("/home/retro/Desktop/projectepidemic/Main_Codes/model_pickel","rb") as f:
            model=pickle.load(f)
# print(X)
values=model.predict(X)

# for i in range(0,12):
#     if values[i]==1:
#         print("Zika Bool:",values[i],"\tFor Location:",data.at[i, 'Location'])
#
#     # else:
#     #     print("False")

config = {
    'apiKey': "Use your firebase api",
    'authDomain': "fill this with appropriate firbase key",
    'databaseURL': "fill this with appropriate firbase key",
    'projectId': "fill this with appropriate firbase key",
    'storageBucket': "fill this with appropriate firbase key",
    'messagingSenderId': "fill this with appropriate firbase key",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

for i in range(0,12):
    # if values[i]==1:
        place = data.at[i, 'Location']
        lat = float(data.at[i, 'Latitude'])  #Latitude,Longitude
        lng = float(data.at[i, 'Longitude'])
        location = {"lat": lat , "lng" : lng}
        print("Zika Bool:",values[i],"\tFor Location:",data.at[i, 'Location'],"With coordinates:",location)
        time.sleep(1)
        # db.child('diseases').child('zika').child('places').child(place).set(location)

    # else:
    #     print("False")
# place = "xync"
# lat = 8
# lng = 3

# location = {"lat": lat , "lng" : lng}
# print(location)
#
# db.child('diseases').child('zika').child('places').child(place).set(location)
