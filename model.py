from sqlalchemy import Column, Integer, String
from db import Base

class WikiData(Base):
    __tablename__ = "wiki_data"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)

