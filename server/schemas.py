from pydantic import BaseModel, EmailStr, conint, constr


class ClienteBase(BaseModel):
    nome: constr(max_length=100)
    cpf: constr(min_length=11, max_length=11)


class ClienteCreate(ClienteBase):
    pass


class Cliente(ClienteBase):
    idcliente: int

    class Config:
        orm_mode = True
