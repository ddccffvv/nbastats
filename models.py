import os, sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Player(Base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    nba_id = Column(Integer, nullable=False)

class Statline(Base):
    __tablename__ = 'statline'
    id = Column(Integer, primary_key=True)
    GAME_ID = Column(String(10))
    TEAM_ID = Column(String(10))
    TEAM_ABBREVIATION = Column(String(10))
    TEAM_CITY = Column(String(10))
    PLAYER_ID = Column(String(10))
    PLAYER_NAME = Column(String(10))
    START_POSITION = Column(String(10))
    COMMENT = Column(String(10))
    MIN = Column(String(10))
    FGM = Column(String(10))
    FGA = Column(String(10))
    FG_PCT = Column(String(10))
    FG3M = Column(String(10))
    FG3A = Column(String(10))
    FG3_PCT = Column(String(10))
    FTM = Column(String(10))
    FTA = Column(String(10))
    FT_PCT = Column(String(10))
    OREB = Column(String(10))
    DREB = Column(String(10))
    REB = Column(String(10))
    AST = Column(String(10))
    STL = Column(String(10))
    BLK = Column(String(10))
    TO = Column(String(10))
    PF = Column(String(10))
    PTS = Column(String(10))
    PLUS_MINUS = Column(String(10))

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.create_all(engine)
