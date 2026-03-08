from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
class Numeros(BaseModel):
    numero1: float
    numero2: float

@app.get('/')
def root():
    return {"message": "API de Calculadora."}

@app.post('/soma')
def soma(dados: Numeros):
    resultado = dados.numero1 + dados.numero2
    return {"operacao": "soma", "resultado": resultado}

@app.post('/subtracao')
def subtracao(dados: Numeros):
    resultado = dados.numero1 - dados.numero2
    return {"operacao": "subtração", "resultado": resultado}

@app.post('/multiplicacao')
def multiplicacao(dados: Numeros):
    resultado = dados.numero1 * dados.numero2
    return {"operacao": "multiplicação", "resultado": resultado}

@app.post('/divisao')
def divisao(dados: Numeros):
    if dados.numero2 == 0:
        raise HTTPException(status_code=400, detail="Erro: divisão por zero!")
    resultado = dados.numero1 / dados.numero2
    return {"operacao": "divisão", "resultado": resultado}