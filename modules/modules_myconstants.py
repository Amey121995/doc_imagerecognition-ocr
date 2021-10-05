# file consists of constants path variables
import json
import os
from pathlib import Path

# from modules import countryDictionary

path = Path(__file__).parent.parent
# print("path = ", path)
path_resources = os.path.join(path, "resources")
# print("path_resources=", path_resources)
path_modules = os.path.join(path, "modules")
# print("path_modules = ", path_modules)
path_logs = os.path.join(path, "logs//")

full_file_path = f'{path_modules}/countryDictionary.json'
# print("full_file_path = ", full_file_path)


json_file_path = os.path.join(path, 'ocr/template/ocr_location_template.json')


class Documents():
    documentType = str()
    isStatewise = bool()

    def __init__(self, documentType, isStatewise):
        self.documentType = documentType
        self.isStatewise = isStatewise


class Country:
    country = str()
    documentList = [Documents]

    def __init__(self, country, documents):
        self.country = country
        self.documentList = documents


class Value:
    def getCountryList(self):

        full_file_path = f'{path_modules}/countryDictionary.json'
        with open(full_file_path, 'r', encoding='utf-8', errors='ignore') as inputFile:

            try:
                json_list = json.load(inputFile)
            except Exception as e:
                print("e3:", e)
                json3 = ({"status": "Invalid", "message": "Incorrect data in json file"})
                return json3

        country_list = []
        for value in json_list:
            country_name = value['country']
            documents = value['documents']
            doc_list = []

            for doc in documents:
                doc_type = doc['doc_type']
                isStatewise = doc['isStatewise']
                doc_object = Documents(doc_type, isStatewise)
                doc_list.append(doc_object)

            country_obj = Country(country_name, doc_list)
            country_list.append(country_obj)

        return country_list


value = Value()
