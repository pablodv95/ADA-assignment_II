import numpy as np
import csv
import pandas as pd
import ast

# Dataset red wine
with open('data/original/winequality-red.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    df = list()    
    row_count = 0
    for row in csv_reader:        

        if row_count != 0:
            fixed_acidity = row[0]               
            volatile_acidity = row[1] 
            citric_acid = row[2]
            residual_sugar = row[3]
            chlorides = row[4]
            free_sulfur_dioxide = row[5]
            total_sulfur_dioxide = row[6]
            density = row[7]
            pH = row[8]
            sulphates= row[9]
            alcohol = row[10]
            #quality = row[11]
            if int(row[11]) <= 4:
                class_name = 'low'
            if int(int(row[11])) >= 5 and int(int(row[11])) <= 7:
                class_name = 'medium'
            if int(int(row[11])) > 7:
                class_name = 'high'

            data = {'fixed acidity': fixed_acidity,
            'volatile acidity': volatile_acidity,
            'citric acid': citric_acid,
            'residual sugar': residual_sugar,
            'chlorides': chlorides,
            'free sulfur dioxide': free_sulfur_dioxide,
            'total sulfur dioxide': total_sulfur_dioxide,
            'density': density,
            'pH': pH,
            'sulphates': sulphates,
            'alcohol': alcohol,
            #'quality': quality,
            'class': class_name}
            
            df.append(data)

        row_count += 1

df = pd.DataFrame(df)
df.to_csv('data/new_format/winequality-red-classes.csv', encoding='utf-8', index=False)


# Dataset white wine
with open('data/original/winequality-white.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    df = list()    
    row_count = 0
    for row in csv_reader:        

        if row_count != 0:
            fixed_acidity = row[0]               
            volatile_acidity = row[1] 
            citric_acid = row[2]
            residual_sugar = row[3]
            chlorides = row[4]
            free_sulfur_dioxide = row[5]
            total_sulfur_dioxide = row[6]
            density = row[7]
            pH = row[8]
            sulphates= row[9]
            alcohol = row[10]
            #quality = row[11]
            if int(row[11]) <= 4:
                class_name = 'low'
            if int(int(row[11])) >= 5 and int(int(row[11])) <= 7:
                class_name = 'medium'
            if int(int(row[11])) > 7:
                class_name = 'high'

            data = {'fixed acidity': fixed_acidity,
            'volatile acidity': volatile_acidity,
            'citric acid': citric_acid,
            'residual sugar': residual_sugar,
            'chlorides': chlorides,
            'free sulfur dioxide': free_sulfur_dioxide,
            'total sulfur dioxide': total_sulfur_dioxide,
            'density': density,
            'pH': pH,
            'sulphates': sulphates,
            'alcohol': alcohol,
            #'quality': quality,
            'class': class_name}
            
            df.append(data)            

        row_count += 1
      
df = pd.DataFrame(df)
df.to_csv('data/new_format/winequality-white-classes.csv', encoding='utf-8', index=False)
            














