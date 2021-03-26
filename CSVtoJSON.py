import csv
import json
import os

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
print(os.path.abspath(os.curdir))
csvpath = os.path.abspath(os.curdir) + '\Files\QuestTestData.csv'
jsonPath = os.path.abspath(os.curdir) + '\Files\QuestTestData.csv'
#csvFilePath = r'QuestTestData.csv'
#jsonFilePath = r'QuestTestData.json'
print(csvpath)
csvFilePath = r'csvpath'
jsonFilePath = r'jsonPath'
csv_to_json(csvFilePath, jsonFilePath)