'''
Created on Jul 19, 2015

@author: pygeek
'''
import sqlalchemy as sql
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper


Integer = sql.Integer

String = sql.String

Table = sql.Table
MetaData = sql.MetaData
Column = sql.Column

ForeignKey = sql.ForeignKey

metadata = MetaData()
engine = create_engine('sqlite:///:memory:', echo=True)

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('fullname', String(50)),
             Column('password', String(30))
             )


class User(object):
    '''
    User class represents a user 
    '''
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password
        
        
mapper(User, user)

metadata.create_all(engine)

