# -*- coding: utf-8 -*-
"""
Created on Fri May 21 21:46:28 2021

@author: srini
"""

import csv
import os

outputPath = os.path.join("new.csv")
title =[]
price=[]
sCount=[]
revCount=[]
cLength=[]

with open('Resources/web_starter.csv', encoding="utf8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    #csv_header = next(csv_reader)
        
    x = 1
    for row in csv_reader:
        title.append(row[1])
        price.append(row[4])
        sCount.append(row[5])
        revCount.append(row[6])
        cLength.append(row[9])
content = zip(title, price, sCount,revCount, cLength)

with open(outputPath, 'w', newline='') as file:
    csvWriter = csv.writer(file,delimiter=',')
    csvWriter.writerow(['Title', 'Price', 'Subscriber Count', 'Number of Reviews', 'Content Length'])
    csvWriter.writerows(content)
    
       
     