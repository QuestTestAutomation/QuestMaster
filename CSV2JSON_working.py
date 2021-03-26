import os,csv,json

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
def Covert_CSV_to_JSON(CSVpath,JSONpath):
    data = {}
    with open(CSVpath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for csvRow in csvReader:
            id = csvRow["ID"]
            data[id] = csvRow

    # write the data toa json file
    with open(JSONpath, "w") as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))


def Read_JSON_DataFile(JSONpath):
    # JSON file
    f = open(JSONpath, "r")

    # Reading from file
    data = json.loads(f.read())

    # Closing file
    f.close()
    return data
print(APP_ROOT)
QuestCSVpath = os.path.abspath(os.curdir) +  "\Files\QuestTestData.csv"
QuestJSONpath  = os.path.abspath(os.curdir) + "\Files\QuestTestData.json"
print(QuestCSVpath )
Covert_CSV_to_JSON(QuestCSVpath,QuestJSONpath)
QUESTTESTDATA = Read_JSON_DataFile(QuestJSONpath)
OICSVpath = os.path.abspath(os.curdir) +  "\Files\OITestData.csv"
OIJSONpath = os.path.abspath(os.curdir) +  "\Files\OITestData.JSON"
Covert_CSV_to_JSON(OICSVpath,OIJSONpath)
OITESTDATA = Read_JSON_DataFile(OIJSONpath)