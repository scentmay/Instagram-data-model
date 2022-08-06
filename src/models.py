import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class user(Base):
    __tablename__= 'usuarios'
    userID = Column (Integer, primary_key = True)
    name = Column (String(50), nullable = False)
    lastname = Column (String(50), nullable = False)
    email = Column (String(50), nullable = False, unique = True)
    password = Column (String(250), nullable = False)

class follower(Base):
    __tablename__= 'followers'
    followerID = Column (Integer, ForeignKey('usuarios.userID'), primary_key = True, nullable=False)
    user_ID = Column (Integer, ForeignKey('usuarios.userID'), primary_key = True, nullable=False)


class post(Base):
    __tablename__= 'posts'
    postID = Column (Integer, primary_key = True, nullable=False)
    user_ID = Column (Integer, ForeignKey('usuarios.userID'), nullable=False)


class media(Base):
    __tablename__= 'media'
    mediaID = Column (Integer, primary_key = True)
    type = Column (Enum, nullable=False)
    url = Column (String(250), nullable=False)
    post_ID = Column (Integer, ForeignKey('posts.postID'), nullable=False)   


class comment(Base):
    __tablename__= 'comments'
    commentID = Column (Integer, primary_key = True)
    author_ID = Column (Integer, ForeignKey('usuarios.userID'))
    post_ID = Column (Integer, ForeignKey('posts.postID'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e