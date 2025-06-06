from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Cliente as DBCliente
from schemas import ClienteCreate, Cliente
from database import get_db, create_tables
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="API de Clientes")


@app.on_event("startup")
async def on_startup():
    await create_tables()
    print("✅ Banco de dados inicializado")


@app.post("/clientes/", response_model=Cliente, status_code=201)
async def criar_cliente(cliente: ClienteCreate, db: AsyncSession = Depends(get_db)):
    try:
        novo_cliente = DBCliente(**cliente.dict())
        db.add(novo_cliente)
        await db.commit()
        await db.refresh(novo_cliente)
        return novo_cliente
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Erro ao criar cliente: {str(e)}"
        )


@app.get("/clientes/", response_model=list[Cliente])
async def listar_clientes(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(DBCliente))
    return result.scalars().all()


@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def obter_cliente(cliente_id: int, db: AsyncSession = Depends(get_db)):
    cliente = await db.get(DBCliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente


@app.delete("/clientes/{cliente_id}", status_code=204)
async def deletar_cliente(cliente_id: int, db: AsyncSession = Depends(get_db)):
    cliente = await db.get(DBCliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    await db.delete(cliente)
    await db.commit()
    return

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
