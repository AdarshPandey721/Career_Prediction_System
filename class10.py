from tkinter import *
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import os

# Get the current working directory
cwd = os.getcwd()
# Load the dataset
df_10th = pd.read_csv(os.path.join(cwd,"generated_dataset_10th.csv"))

features_10th = ['Maths', 'Bio', 'Physics', 'Chemistry']
target_10th = 'Fields_10th'

X_train_10th, X_test_10th, y_train_10th, y_test_10th = train_test_split(df_10th[features_10th], df_10th[target_10th], test_size=0.2, random_state=42)

# Train the KNN models
knn_10th = KNeighborsClassifier(n_neighbors=5)
knn_10th.fit(X_train_10th, y_train_10th)

def KNN_10th():
    # Get user inputs from the GUI for 10th class
    maths_score = int(Interest1_10th.get())
    bio_score = int(Interest2_10th.get())
    physics_score = int(Interest3_10th.get())
    chemistry_score = int(Interest4_10th.get())

    # Make predictions using the trained model for 10th class
    prediction = knn_10th.predict([[maths_score, bio_score, physics_score, chemistry_score]])

    # Display the prediction
    t1.delete("1.0", END)
    t1.insert(END, prediction[0])


def predict_10th():
    KNN_10th()


# Create the root window

root = Tk()
root.configure(background='#FFF5BA')  # Set background color to light yellow
root.geometry("1000x600")  # Set window size

# 10th class entries
OPTIONS = ['1', '2', '3', '4', '5']
Interest1_10th = StringVar()
Interest1_10th.set("Select")
Interest2_10th = StringVar()
Interest2_10th.set("Select")
Interest3_10th = StringVar()
Interest3_10th.set("Select")
Interest4_10th = StringVar()
Interest4_10th.set("Select")

# Heading
w2 = Label(root, justify=CENTER, text="Career Prediction System using Machine Learning", fg="black", bg="#FFF5BA")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=4, padx=80)

# 10th class labels and entries
w1_10th = Label(root, justify=LEFT, text="10th Class", fg="white", bg="green")
w1_10th.config(font=("Elephant", 20))
w1_10th.grid(row=3, column=0, padx=50, sticky=W)

S1Lb_10th = Label(root, text="Maths", fg="black", bg="#FFF5BA")
S1Lb_10th.grid(row=6, column=0, pady=7, sticky=W)
S1En_10th = OptionMenu(root, Interest1_10th, *OPTIONS)
S1En_10th.grid(row=6, column=1, padx=50)

S2Lb_10th = Label(root, text="Bio", fg="black", bg="#FFF5BA")
S2Lb_10th.grid(row=7, column=0, pady=7, sticky=W)
S2En_10th = OptionMenu(root, Interest2_10th, *OPTIONS)
S2En_10th.grid(row=7, column=1, padx=50)

S3Lb_10th = Label(root, text="Physics", fg="black", bg="#FFF5BA")
S3Lb_10th.grid(row=8, column=0, pady=7, sticky=W)
S3En_10th = OptionMenu(root, Interest3_10th, *OPTIONS)
S3En_10th.grid(row=8, column=1, padx=50)

S4Lb_10th = Label(root, text="Chemistry", fg="black", bg="#FFF5BA")
S4Lb_10th.grid(row=9, column=0, pady=7, sticky=W)
S4En_10th = OptionMenu(root, Interest4_10th, *OPTIONS)
S4En_10th.grid(row=9, column=1, padx=50)

# KNN button and prediction outcome box
KNNButton_10th = Button(root, text="Prediction - 10th", fg="black", bg="yellow" , command= KNN_10th)  # Add command for KNN_10th function
KNNButton_10th.grid(row=14, column=1, pady=10)

t1 = Text(root, height=2, width=20, bg="#FFA07A", fg="black")
t1.grid(row=15, column=1)

# Start the GUI
root.mainloop()
