import plotly.express as px 
import csv 
import pandas as pd 
import statistics 
import random 
import plotly.graph_objects as go 
import plotly.figure_factory as ff 

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()
mean1 = statistics.mean(data)
std_deviation = statistics.stdev(data)
#fig = ff.create_distplot([data],["temp"],show_hist = False)
#fig.add_trace(go.Scatter(x = [mean1, mean1],y = [0,1],mode="lines",name = "MEAN"))
#fig.show()
#print(mean1, std_deviation)

dataset = []
for i in range(0,100):
    randomindex = random.randint(0,len(data))
    value = data[randomindex]
    dataset.append(value)
mean2 = statistics.mean(dataset)
std_deviation1 = statistics.stdev(dataset)
print(mean2,std_deviation1)

def randomsetofmeans(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean3 = statistics.mean(dataset)
    return mean3

def showfig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["claps"],show_hist = False)
    fig.show()

def standard_deviation():
    mean_list = []
    for i in range(0,100):
        setofmeans = randomsetofmeans(100)
        mean_list.append(setofmeans)
    standard_deviation = statistics.stdev(mean_list)
    print(standard_deviation)
standard_deviation()

def settup():
    mean_list = []
    for i in range(0,47000):
        setofmeans= randomsetofmeans(100)
        mean_list.append(setofmeans)
    showfig(mean_list)
settup()