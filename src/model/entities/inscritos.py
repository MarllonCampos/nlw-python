"""
    Create a entity Inscritos
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from src.model.configs.base import Base

class Inscritos(Base):
    """
        Specify the columns of table eventos
    """
    __tablename__ = "Inscritos" 

    id = Column(Integer,primary_key=True, autoincrement=True)
    nome = Column(String,nullable=False)
    email = Column(String,nullable=False)
    link = Column(String,nullable=True)
    evento_id = Column(Integer,nullable=False, ForeignKey=["Eventos.id"])
