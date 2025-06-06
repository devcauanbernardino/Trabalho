from sqlalchemy import Column, Integer, String, CheckConstraint
from database import Base


class Cliente(Base):
    __tablename__ = "cliente"

    idcliente = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)


    __table_args__ = (
        CheckConstraint('idade >= 0', name='idade_positiva'),
        CheckConstraint("email LIKE '%@%'", name='email_valido')
    )
