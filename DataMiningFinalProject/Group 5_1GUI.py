from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import OptionMenu, ttk
import tkinter.messagebox

# action for drop down menu
def selected(event):
    # if texas selected
    if clicked.get() == 'Texas':
        w = 0.4
        x = ["Positive Tweets"]
        y = ["Negative Tweets"]
        texasPositive = [4529]
        texasNegative = [7603]

        plt.bar(x,texasPositive, w, label = "Positive Tweet")
        plt.bar(y,texasNegative, w, label = "Negative Tweet")

        plt.xlabel("Model Predicted Texas Electric Costs Trending: UP \n Electric Costs Actual Trend: UP \n SUCCESS")
        plt.ylabel("Number of Tweets")
        plt.title("Predicting Electric Trends With Tweet Sentiment")
        plt.legend()
        plt.show()
        
    # if hawaii selected
    if clicked.get() == 'Hawaii':
        w = 0.4
        x = ["Positive Tweets"]
        y = ["Negative Tweets"]
        hawaiiPositive = [161]
        hawaiiNegative = [111]

        plt.bar(x,hawaiiPositive, w, label = "Positive Tweet")
        plt.bar(y,hawaiiNegative, w, label = "Negative Tweet")

        plt.xlabel("Model Predicted Hawaii Electric Costs Trending: DOWN \n Electric Costs Actual Trend: UP \n FAILURE")
        plt.ylabel("Number of Tweets")
        plt.title("Predicting Electric Trends With Tweet Sentiment")
        plt.legend()
        plt.show()
        
    # if idaho selected
    if clicked.get() == 'Idaho':
        w = 0.4
        x = ["Positive Tweets"]
        y = ["Negative Tweets"]
        idahoPositive = [34]
        idahoNegative = [18]

        plt.bar(x,idahoPositive, w, label = "Positive Tweet")
        plt.bar(y,idahoNegative, w, label = "Negative Tweet")

        plt.xlabel("Model Predicted Idaho Electric Costs Trending: DOWN \n Electric Costs Actual Trend: DOWN \n SUCCESS")
        plt.ylabel("Number of Tweets")
        plt.title("Predicting Electric Trends With Tweet Sentiment")
        plt.legend()
        plt.show()
        
    # if kansas selected
    if clicked.get() == 'Kansas':
        w = 0.4
        x = ["Positive Tweets"]
        y = ["Negative Tweets"]
        kansasPositive = [632]
        kansasNegative = [602]

        plt.bar(x,kansasPositive, w, label = "Positive Tweet")
        plt.bar(y,kansasNegative, w, label = "Negative Tweet")

        plt.xlabel("Model Predicted Kansas Electric Costs Trending: DOWN \n Electric Costs Actual Trend: DOWN \n SUCCESS")
        plt.ylabel("Number of Tweets")
        plt.title("Predicting Electric Trends With Tweet Sentiment")
        plt.legend()
        plt.show()
        
    # if louisiana selected
    if clicked.get() == 'Louisiana':
        w = 0.4
        x = ["Positive Tweets"]
        y = ["Negative Tweets"]
        louisianaPositive = [2308]
        louisianaNegative = [2979]

        plt.bar(x,louisianaPositive, w, label = "Positive Tweet")
        plt.bar(y,louisianaNegative, w, label = "Negative Tweet")

        plt.xlabel("Model Predicted Louisiana Electric Costs Trending: UP \n Electric Costs Actual Trend: DOWN \n Failure")
        plt.ylabel("Number of Tweets")
        plt.title("Predicting Electric Trends With Tweet Sentiment")
        plt.legend()
        plt.show()
        
    # if massachusetts selected
    if clicked.get() == 'Massachusetts':
        w = 0.4
        x = ["Positive Tweets"]
        y = ["Negative Tweets"]
        massachusettsPositive = [816]
        massachusettsNegative = [685]

        plt.bar(x,massachusettsPositive, w, label = "Positive Tweet")
        plt.bar(y,massachusettsNegative, w, label = "Negative Tweet")

        plt.xlabel("Model Predicted Massachusetts Electric Costs Trending: DOWN \n Electric Costs Actual Trend: UP \n Failure")
        plt.ylabel("Number of Tweets")
        plt.title("Predicting Electric Trends With Tweet Sentiment")
        plt.legend()
        plt.show()
        
    # if arizona selected
    if clicked.get() == 'Arizona':
        w = 0.4
        x = ["Positive Tweets"]
        y = ["Negative Tweets"]
        arizonaPositive = [203]
        arizonaNegative = [429]

        plt.bar(x,arizonaPositive, w, label = "Positive Tweet")
        plt.bar(y,arizonaNegative, w, label = "Negative Tweet")

        plt.xlabel("Model Predicted Arizona Electric Costs Trending: UP \n Electric Costs Actual Trend: UP \n SUCCESS")
        plt.ylabel("Number of Tweets")
        plt.title("Predicting Electric Trends With Tweet Sentiment")
        plt.legend()
        plt.show()
        
    # if utah selected
    if clicked.get() == 'Utah':
        w = 0.4
        x = ["Positive Tweets"]
        y = ["Negative Tweets"]
        utahPositive = [41]
        utahNegative = [34]

        plt.bar(x,utahPositive, w, label = "Positive Tweet")
        plt.bar(y,utahNegative, w, label = "Negative Tweet")

        
        plt.xlabel("Model Predicted Utah Electric Costs Trending: DOWN \n Electric Costs Actual Trend: DOWN \n SUCCESS")
        plt.ylabel("Number of Tweets")
        plt.title("Predicting Electric Trends With Tweet Sentiment")
        plt.legend()
        plt.show()

    # if california selected
    if clicked.get() == 'California':
        w = 0.4
        x = ["Positive Tweets"]
        y = ["Negative Tweets"]
        caliPositive = [3576]
        caliNegative = [4308]

        plt.bar(x,caliPositive, w, label = "Positive Tweet")
        plt.bar(y,caliNegative, w, label = "Negative Tweet")

        
        plt.xlabel("Model Predicted California Electric Costs Trending: UP \n Electric Costs Actual Trend: UP \n SUCCESS")
        plt.ylabel("Number of Tweets")
        plt.title("Predicting Electric Trends With Tweet Sentiment")
        plt.legend()
        plt.show()

    # if wisconsin selected
    if clicked.get() == 'Wisconsin':
        w = 0.4
        x = ["Positive Tweets"]
        y = ["Negative Tweets"]
        wPositive = [342]
        wNegative = [140]

        plt.bar(x,wPositive, w, label = "Positive Tweet")
        plt.bar(y,wNegative, w, label = "Negative Tweet")

        
        plt.xlabel("Model Predicted Wisconsin Electric Costs Trending: DOWN \n Electric Costs Actual Trend: DOWN \n SUCCESS")
        plt.ylabel("Number of Tweets")
        plt.title("Predicting Electric Trends With Tweet Sentiment")
        plt.legend()
        plt.show()
# Prints test data
def clicked1():
    w = 0.4
    x = ["Correctly Identified Tweets"]
    y = ["Wrongly Identified Tweets"]
    correct = [1991]
    error = [9]

    plt.bar(x,correct, w, label = "Correctly Identified Tweets")
    plt.bar(y,error, w, label = "Wrongly Identified Tweets")

    plt.xlabel("Correctly Identifed Sentiment of 1991 Tweets out of 2000")
    plt.ylabel("Number of Tweets")
    plt.title("Sentiment Analyis Model Test")
    plt.legend()
    plt.show()

# Displays success rate graph
def clicked2():
    labels = 'Success Rate', 'Error Rate'
    sizes = [1991, 9]
    explode = (0, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.xlabel("Naive Bayes Sentiment Analysis Success Rate")
    plt.show()

# displays predictions
def clicked3():
    labels = 'Success Rate', 'Error Rate'
    sizes = [7, 3]
    explode = (0, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.xlabel("Using Tweet Sentiment to Predict Electricty Cost Trends")
    plt.show()
# creates root to add all gui things to
root = tk.Tk()
root.title("Predicting Electric Trends With Tweet Sentiment")
# handles action control
tabControl = ttk.Notebook(root)
# creates model results tab
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = "Model Results")
tabControl.pack(expand=1, fill = "both")
# creates and adds button
btn = tk.Button(tab1, text = "Display Data", command=lambda:clicked1())
btn.pack()
# creates and adds button
btn1 = tk.Button(tab1, text = "Display Success Rate", command=lambda:clicked2())
btn1.pack()




        



tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = "Prediction Results")
tabControl.pack(expand=1, fill = "both")

options_list = ["Arizona", "California", "Hawaii", "Idaho", "Kansas", "Louisiana", "Massachusetts", "Texas", "Utah", "Wisconsin"]

#Variable to keep track of the option selected in OptionMenu
clicked = StringVar()
clicked.set(options_list[0])

dropDown = OptionMenu(tab2, clicked, *options_list, command = selected)
dropDown.pack()

btn2 = tk.Button(tab2, text = "Display Success Rate", command=lambda:clicked3())
btn2.pack()



root.mainloop()



