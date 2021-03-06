import json, datetime, os
import re

for filename in os.listdir("jsons"):
    print filename
    f = open("jsons/" + filename)

    j = json.load(f)

    date = j["resultSets"][0]["rowSet"][0][0]
    gamedate =  datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    gamedate = datetime.datetime.strftime(gamedate, '%Y-%m-%d')

    homecode = j["resultSets"][1]["rowSet"][0][4]
    awaycode = j["resultSets"][1]["rowSet"][1][4]

    playerlines = j["resultSets"][4]["rowSet"]

    for line in playerlines:
        #print line[2:]
        if re.match(".*den.*", line[2:][3]):
            print [gamedate, homecode, awaycode] + line[2:]
