import json
from database import mysqlUserDb

import csv_helper

typ = ""

fle = ""


config_obj = open('config.json')

a = json.load(config_obj)

print a["database"]

r = raw_input("Enter the file Name")

with open(r) as f:

    for i, l in enumerate(f):

        pass

    flen = i + 1

print flen


count= 0

for i in range (0,4):
    if r == a["files"]["types"][i]["name"]:

            typ = a["files"]["types"][i]["type"]


c = csv_helper.direct(typ)
print typ
parse_file = r

d=c.parse(parse_file)

ky = []

for key in d[0].keys():

    ky.append(key)

db_obj = mysqlUserDb(a["database"]["user"],a["database"]["host"],a["database"]["password"])

db_obj.createdb()


for i in range(0,len(d)) :

    countr = 0

    vl = []

    for j in ky :

        vl.append(d[i][j])

    db_obj.write_type(ky,vl)

    count += 1

    if flen == count :

        pass

    else :

        i = countr  + 1

db_obj.commit()


