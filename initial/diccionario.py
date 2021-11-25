import csv
import json


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):

    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, mode="r", encoding="UTF-8") as csvf:
        csvReader = csv.DictReader(csvf, delimiter=";")

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # print(rows)
            # Assuming a column named 'No' to
            # be the primary key
            key = rows["id"]
            key = int(key)
            data[key] = rows["valor"]

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, "w", encoding="UTF-8") as jsonf:
        jsonf.write(json.dumps(data, indent=4, ensure_ascii=False))


# Driver Code

# Decide the two file paths according to your
# computer system
## csvFilePath = r"Names.csv"
## jsonFilePath = r"Names.json"

# Call the make_json function
# make_json(csvFilePath, jsonFilePath)
#
""" 
miDiccionario = {}

with open("../Diccionario.csv", mode="r") as file:
    reader = csv.reader(file)
    with open("../Diccionario.csv", mode="w") as outfile:
        writer = csv.writer(outfile)
        miDiccionario = {rows[0]: rows[1] for rows in reader}

with open("../Diccionario.csv", "w", newline="") as csv_file:
  cols = ["id","first_name","last_name","email","gender"] 
  writer = csv.DictWriter(csv_file, fieldnames=cols)
  writer.writeheader()
  writer.writerows(data)


print(miDiccionario)
 """
