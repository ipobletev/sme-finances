import pandas as pd
import json
import uuid

# def lee_datos_excel(archivo):
#     # Leer el archivo excel
#     df = pd.read_excel(archivo)
    
#     # Convertir el DataFrame a JSON
#     datos_json = df.to_json(orient='records')

#     return datos_json

# # Usar la función para leer un archivo excel
# datos = lee_datos_excel(f'./data/2023.xlsx')
# print(datos)

with open('data/2021.json') as file:
    data = json.load(file)

new_data = []
for element in data:
    category = element["Mes"]
    for month in element:
        if month == "Mes" or month == '-':
            continue
        new_dict = {
            "uuid" : str(uuid.uuid4()), # Esto genera un UUID aleatorio
            "datetime": "",
            "date_month": month,
            "date_year": 2021, # Cambia este año si es necesario
            "description": category,
            "type_transaction": "Expense", # Asumiendo que es una venta. Cambia esto según sea necesario
            "type_value": [category],
            "value": element[month]
        }
        new_data.append(new_dict)

#####################

with open('data/2022.json') as file:
    data = json.load(file)

for element in data:
    category = element["Mes"]
    for month in element:
        if month == "Mes" or month == '-':
            continue
        new_dict = {
            "uuid" : str(uuid.uuid4()), # Esto genera un UUID aleatorio
            "datetime": "",
            "date_month": month,
            "date_year": 2022, # Cambia este año si es necesario
            "description": category,
            "type_transaction": "Expense", # Asumiendo que es una venta. Cambia esto según sea necesario
            "type_value": [category],
            "value": element[month]
        }
        new_data.append(new_dict)
  
  
###################

with open('data/2023.json') as file:
    data = json.load(file)

for element in data:
    category = element["Mes"]
    for month in element:
        if month == "Mes" or month == '-':
            continue
        new_dict = {
            "uuid" : str(uuid.uuid4()), # Esto genera un UUID aleatorio
            "datetime": "",
            "date_month": month,
            "date_year": 2023, # Cambia este año si es necesario
            "description": category,
            "type_transaction": "Expense", # Asumiendo que es una venta. Cambia esto según sea necesario
            "type_value": [category],
            "value": element[month]
        }
        new_data.append(new_dict)
        
###################

with open('data/new_data.json', 'w') as f:
  json.dump(new_data, f)