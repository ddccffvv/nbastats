import json, datetime, os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Player, Base, Statline

engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

for filename in os.listdir("jsons"):
    f = open("jsons/" + filename)

    j = json.load(f)

    date = j["resultSets"][0]["rowSet"][0][0]
    gamedate =  datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    gamedate = datetime.datetime.strftime(gamedate, '%Y-%m-%d')

    homecode = j["resultSets"][1]["rowSet"][0][4]
    awaycode = j["resultSets"][1]["rowSet"][1][4]

    playerlines = j["resultSets"][4]["rowSet"]

    for line in playerlines:
        bla = [gamedate, homecode, awaycode] + line[2:]
        player =  session.query(Player).filter(Player.nba_id == bla[5]).all()
        if not player:
            player = Player(name=bla[6], nba_id=int(bla[5]))
            session.add(player)
        #statline = Statline(

session.commit()

for player in session.query(Player).all():
    print player.name
