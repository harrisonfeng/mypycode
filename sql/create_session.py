#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy

from sqlalchemy.orm import sessionmaker
from create_schema import User


Column = sqlalchemy.Column
Integer = sqlalchemy.Integer
String = sqlalchemy.String
Sequence = sqlalchemy.Sequence


engine = sqlalchemy.create_engine("sqlite:////tmp/test.db", echo=True)
Session = sessionmaker(bind=engine)


def main():
    session = Session() 
    auser = User(name='Bar', fullname='Fuck Bar', password='edspassword')
    quser = session.query(User).filter(User.name == 'Bar').first()
    if not quser:
        session.add(auser)
    print session.dirty
    print session.new
    session.commit()
    for s in session:
        print s
    
if __name__ == '__main__':
    main()