from sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

db = SQLAlchemy()


# Создаем таблицу для Юзера
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    phone_number = Column(Integer, unique=True)
    level = Column(String, default='None')
    datetime = Column(DateTime, default=datetime.now())

# Class for the Questions
class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, autoincrement=True, primary_key=True)
    main_questions = Column(String, unique=True, nullable=False)
    answer1 = Column(String)
    answer2 = Column(String)
    answer3 = Column(String)
    answer4 = Column(String)
    correct_answer = Column(Integer, nullable=False)
    timer = Column(Integer)

class Result(Base):
    __tablename__ = 'results'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user_answer = Column(String, ForeignKey("questions.correct_answers"), nullable=False)


class UserAnswers(Base):
    __tablename__ = 'user_answers'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    q_id = Column(Integer, ForeignKey('questions.id'))
    level = Column(String, ForeignKey("users.level"))
    user_answer = Column(String)
    correctness = Column(Boolean, default=False)