# -*- coding: utf-8 -*-
"""
Created on Sat May 22 12:51:26 2021

@author: srini
"""

def PrintPercentage(row):
    sum1 = int(row[1]) +int(row[2]) + int(row [3])
    wins = int(row[1])/sum1 *100
    loss = int(row[2])/sum1 *100
    draw = int(row[3])/sum1 *100
    
    print("Stats for ", row[0])
    print("Winning Percentage :", wins) 
    print("Losing Percentage :", loss)
    print("Draw Percentage :", draw)
    return
    
import csv

name_to_check = input("Enter the wrestler name: ")
with open('Resources/WWE-Data-2016.csv', encoding="utf8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)    
    for row in csv_reader:        
       # print(row[1])
        #print(name_to_check)
        if(name_to_check == row[0]):            
            PrintPercentage(row)


    