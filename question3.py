import json
import csv

with open ('covid_cases.json','r') as json_file:
    ourjson = json.load(json_file)

covid_data = ourjson['records']
question_file = open ('question_file.csv','w')
csv_writer = csv.writer(question_file)

count = 0

for i in covid_data:
    if count == 0:
        header = i.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(i.values())
question_file.close()
