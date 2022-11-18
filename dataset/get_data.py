import csv

import codecs

import json


def get_data_from_file(csv_file):
    data = []
    with open(csv_file, newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for rows in reader:
            rows = [[j.strip() for j in i.split(':')] for i in rows]
            data.append(dict(rows))
        return data


def get_data_from_json(file):
    with codecs.open(file, "r", "utf-8") as json_file:
        json_dict = json.load(json_file)
    return json_dict
