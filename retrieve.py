import requests, json, datetime

f = open("latest", "r")

lines = f.readlines()

i_identifier = int(lines[0].strip())
s_identifier = str(i_identifier).rjust(10, "0")
f.close()

r = requests.get("http://stats.nba.com/stats/boxscore?GameID=" + s_identifier + "&RangeType=0&StartPeriod=0&EndPeriod=0&StartRange=0&EndRange=0")

while True:
    print "Downloading: " + s_identifier
    j = json.loads(r.text)
    date = j["resultSets"][0]["rowSet"][0][0]
    gamedate =  datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    if not datetime.datetime.now() > (gamedate + datetime.timedelta(1)):
        break
    gamefile = open("jsons/" + s_identifier, "w")
    json.dump(r.json(), gamefile)
    gamefile.close()

    i_identifier = i_identifier + 1
    s_identifier = str(i_identifier).rjust(10, "0")
    r = requests.get("http://stats.nba.com/stats/boxscore?GameID=" + s_identifier + "&RangeType=0&StartPeriod=0&EndPeriod=0&StartRange=0&EndRange=0")

print "gotten to the end"
print s_identifier
f = open("latest", "w")
f.write(s_identifier)
f.close()
