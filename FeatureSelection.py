# -*- coding: utf-8 -*-
"""
Created on Wed May 11 19:13:58 2022

@author: Johanna Damaris
"""

import numpy as np
import pandas as pd

name = ["time","ax","ay","az","at"]


daten = pd.read_csv("C:/Users/jojo9/Desktop/Projekt/DatenJohanna.csv",sep=";",names=name,header=0)

window = 2

xmin = []
xmax = []
xmean = []
xmedian = []
xstd = []
xdiff = []

ymin = []
ymax = []
ymean = []
ymedian = []
ystd = []
ydiff = []

zmin = []
zmax = []
zmean = []
zmedian = []
zstd = []
zdiff = []

classification=[]


def klassifikation(t):

    if t <121:
        classification.append("laufen")
    elif t >=121 and t < 241:
        classification.append("gehen")
    elif t >=241 and t < 361:
        classification.append("sitzen")
    elif t >=361 and t < 481:
        classification.append("liegen")     
    elif t >=481:
        classification.append("stehen")

for i in range(0,len(daten["ax"]),window):
    #deskription ax
    xmin.append(daten["ax"][i:i+window].min())
    xmax.append(daten["ax"][i:i+window].max())
    xmean.append(daten["ax"][i:i+window].mean())
    xmedian.append(daten["ax"][i:i+window].median())
    xstd.append(daten["ax"][i:i+window].std())
    xdiff.append(daten["ax"][i:i+window].max()-daten["ax"][i:i+window].min()) 
          
    #deskription ay
    ymin.append(daten["ay"][i:i+window].min())
    ymax.append(daten["ay"][i:i+window].max())
    ymean.append(daten["ay"][i:i+window].mean())
    ymedian.append(daten["ay"][i:i+window].median())
    ystd.append(daten["ay"][i:i+window].std())
    ydiff.append(daten["ay"][i:i+window].max()-daten["ay"][i:i+window].min())
    
    #dekription az
    zmin.append(daten["az"][i:i+window].min())
    zmax.append(daten["az"][i:i+window].max())
    zmean.append(daten["az"][i:i+window].mean())
    zmedian.append(daten["az"][i:i+window].median())
    zstd.append(daten["az"][i:i+window].std())
    zdiff.append(daten["az"][i:i+window].max()-daten["az"][i:i+window].min())  

    t = daten["time"][i:i+window].mean()
    
    klassifikation(t)

#print(zmin)
#print(len(xmean))
#print(len(classification))


df = pd.DataFrame(zip(xmin, xmax, xmean, xmedian, xstd, xdiff, ymin, ymax, ymean, ymedian, ystd, ydiff, zmin, zmax, zmean, zmedian, zstd, zdiff, classification))

col = ["xmin", "xmax", "xmean", "xmedian", "xstd", "xdiff", "yxmin", "ymax", "ymean", "ymedian", "ystd", "ydiff", "zmin", "zmax", "zmean", "zmedian", "zstd", "zdiff", "classification"]

df.to_csv("C:/Users/jojo9/Desktop/Projekt/features.csv",sep=",",index=False,header=col)