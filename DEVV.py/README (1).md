# 🧮 API Calculadora

> API de operações matemáticas construída com **FastAPI** + **Python**

---

## 🚀 Tecnologias

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-purple?style=for-the-badge)

---

## 📋 Sobre o Projeto

API REST simples que recebe dois números e realiza as quatro operações matemáticas básicas: **soma**, **subtração**, **multiplicação** e **divisão**.

---

## ⚙️ Como Instalar

**1. Clone o repositório:**
```bash
git clone https://github.com/Viniciusmbbr/api-calculadora.git
cd api-calculadora
```

**2. Instale as dependências:**
```bash
pip install fastapi uvicorn
```

---

## ▶️ Como Rodar

```bash
python -m uvicorn api:app --reload
```

O servidor estará disponível em: `http://localhost:8000`

---

## 🔗 Endpoints

| Método | Endpoint | Operação |
|--------|----------|----------|
| `POST` | `/soma` | ➕ Soma |
| `POST` | `/subtracao` | ➖ Subtração |
| `POST` | `/multiplicacao` | ✖️ Multiplicação |
| `POST` | `/divisao` | ➗ Divisão |

---

## 📨 Exemplo de Requisição

**Body (JSON):**
```json
{
  "numero1": 10,
  "numero2": 5
}
```

**Resposta:**
```json
{
  "operacao": "soma",
  "resultado": 15.0
}
```

---

## ⚠️ Tratamento de Erros

Divisão por zero retorna erro `400`:
```json
{
  "detail": "Erro: divisão por zero!"
}
```

---

## 🧪 Como Testar

Acesse a documentação interativa automática do FastAPI:

```
http://localhost:8000/docs
```

---

## 📁 Estrutura do Projeto

```
api-calculadora/
├── api.py            # Código principal da API
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação
```

---

## 👨‍💻 Autor

Feito por **ViniciusMB**
