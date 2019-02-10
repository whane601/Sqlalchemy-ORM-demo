from src.common import util

from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime


engine = create_engine(util.get_config_value("DB", "POSTGRESQL"))
Base = declarative_base()
Session = sessionmaker(bind=engine)

# 定義所需的table結構
class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    phone = Column(String(20), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())


class Transcripts(Base):

    __tablename__ = "transcripts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    score = Column(Integer, nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())


def insertDB(record):
    s = Session()
    s.add(record)
    s.commit()
    s.close()

# 創建table，若已存在會被忽略
Base.metadata.create_all(engine)