import numpy as np
import csv
import pandas as pd
import ast

aux_count_red_wine = 0 
aux_count_white_wine = 0 
alcohol_sum_red_wine = 0
alcohol_sum_white_wine = 0

# Dataset red wine
with open('data/original/winequality-red.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    row_count = 0       

    for row in csv_reader:      
        if row_count != 0:
            alcohol = float(row[10])
            alcohol_sum_red_wine += alcohol
            aux_count_red_wine += 1

        row_count += 1


# Dataset white wine
with open('data/original/winequality-white.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    row_count = 0       

    for row in csv_reader:      
        if row_count != 0:
            alcohol = float(row[10])
            alcohol_sum_white_wine += alcohol
            aux_count_white_wine += 1

        row_count += 1


# Means values for alcohol variable
alcohol_mean_red_wine = alcohol_sum_red_wine / aux_count_red_wine
alcohol_mean_white_wine = alcohol_sum_white_wine / aux_count_white_wine

print("RED ALCOHOL MEAN {} {} result: {}".format(alcohol_sum_red_wine, aux_count_red_wine, alcohol_mean_red_wine))
print("WHITE ALCOHOL MEAN {} {} result: {}".format(alcohol_sum_white_wine, aux_count_white_wine, alcohol_mean_white_wine))



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
            if float(alcohol) <= float(alcohol_mean_red_wine):
                alcohol_content = 'low'
            else:
                alcohol_content = 'high'

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
            #'alcohol': alcohol,
            #'quality': quality,
            'alcohol content': alcohol_content}
            
            df.append(data)

        row_count += 1

df = pd.DataFrame(df)
df.to_csv('data/new_format/winequality-red-alcohol-content.csv', encoding='utf-8', index=False)


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
            if float(alcohol) <= float(alcohol_mean_white_wine):
                alcohol_content = 'low'
            else:
                alcohol_content = 'high'

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
            #'alcohol': alcohol,
            #'quality': quality,
            'alcohol content': alcohol_content}
            
            df.append(data)            

        row_count += 1
      
df = pd.DataFrame(df)
df.to_csv('data/new_format/winequality-white-alcohol-content.csv', encoding='utf-8', index=False)
            














