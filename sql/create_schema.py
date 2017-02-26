#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base

Column = sqlalchemy.Column
Integer = sqlalchemy.Integer
String = sqlalchemy.String
Sequence = sqlalchemy.Sequence

engine = sqlalchemy.create_engine("sqlite:////tmp/test.db", echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=50))
    fullname = Column(String(length=50))
    password = Column(String(length=20))
    
    def __repr__(self):
        return \
            "<User(name={0}, fullname={1}, password={2})>".format(self.name,
                                                                  self.fullname,
                                                                  self.password,
                                                                  )
def main():
    Base.metadata.create_all(engine) 
    
if __name__ == '__main__':
    main()