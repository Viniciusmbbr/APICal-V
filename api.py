from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import matplotlib.pyplot as plt
import io
 
app = FastAPI()
 
# Permite a interface HTML se comunicar com a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
 
historico = []
 
class Numeros(BaseModel):
    numero1: float
    numero2: float
 
# Serve a interface visual
@app.get('/')
def root():
    return FileResponse('index.html')
 
@app.post('/soma')
def soma(dados: Numeros):
    resultado = dados.numero1 + dados.numero2
    historico.append({"operacao": "soma", "resultado": resultado})
    return {"operacao": "soma", "resultado": resultado}
 
@app.post('/subtracao')
def subtracao(dados: Numeros):
    resultado = dados.numero1 - dados.numero2
    historico.append({"operacao": "subtração", "resultado": resultado})
    return {"operacao": "subtração", "resultado": resultado}
 
@app.post('/multiplicacao')
def multiplicacao(dados: Numeros):
    resultado = dados.numero1 * dados.numero2
    historico.append({"operacao": "multiplicação", "resultado": resultado})
    return {"operacao": "multiplicação", "resultado": resultado}
 
@app.post('/divisao')
def divisao(dados: Numeros):
    if dados.numero2 == 0:
        raise HTTPException(status_code=400, detail="Erro: divisão por zero!")
    resultado = dados.numero1 / dados.numero2
    historico.append({"operacao": "divisão", "resultado": resultado})
    return {"operacao": "divisão", "resultado": resultado}
 
@app.get('/historico')
def ver_historico():
    return historico
 
@app.get('/grafico')
def gerar_grafico():
    if not historico:
        raise HTTPException(status_code=400, detail="Nenhum cálculo realizado ainda!")
 
    operacoes = [f"{i+1}. {h['operacao']}" for i, h in enumerate(historico)]
    resultados = [h['resultado'] for h in historico]
 
    plt.figure(figsize=(10, 5))
    plt.bar(operacoes, resultados, color='#00f5a0')
    plt.title('Histórico de Cálculos', fontsize=14)
    plt.xlabel('Operações')
    plt.ylabel('Resultado')
    plt.xticks(rotation=15)
    plt.tight_layout()
 
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
 
    return StreamingResponse(buffer, media_type="image/png")
 