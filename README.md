# 🧮 API Calculadora

> API de operações matemáticas com interface visual, histórico de cálculos e geração de gráficos — construída com **FastAPI** + **Python**

---

## 🚀 Tecnologias

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-gráficos-orange?style=for-the-badge&logo=python&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-purple?style=for-the-badge)

---

## 📋 Sobre o Projeto

API REST que recebe dois números e realiza as quatro operações matemáticas básicas. Conta com uma **interface web** integrada, **histórico de cálculos** e **geração de gráficos** com os resultados.

---

## 🖥️ Interface

> Acesse `http://localhost:8000` com o servidor rodando para ver a interface

A interface conta com:
- Campo para inserir os dois números
- Botões para cada operação matemática
- Exibição do resultado em tempo real
- Histórico de todos os cálculos realizados
- Botão para gerar gráfico do histórico

---

## ✨ Funcionalidades

- ➕ Soma
- ➖ Subtração
- ✖️ Multiplicação
- ➗ Divisão
- 📋 Histórico de cálculos realizados
- 📊 Geração de gráfico com os resultados
- 🖥️ Interface web integrada

---

## ⚙️ Como Instalar

**1. Clone o repositório:**
```bash
git clone https://github.com/SEU_USUARIO/api-calculadora.git
cd api-calculadora
```

**2. Instale as dependências:**
```bash
pip install fastapi uvicorn matplotlib python-multipart
```

---

## ▶️ Como Rodar

```bash
python -m uvicorn api:app --reload
```

Acesse a interface no navegador:
```
http://localhost:8000
```

---

## 🔗 Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/` | Interface visual da calculadora |
| `POST` | `/soma` | Soma dois números |
| `POST` | `/subtracao` | Subtrai dois números |
| `POST` | `/multiplicacao` | Multiplica dois números |
| `POST` | `/divisao` | Divide dois números |
| `GET` | `/historico` | Retorna histórico de cálculos |
| `GET` | `/grafico` | Retorna gráfico do histórico |

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

**Interface visual:**
```
http://localhost:8000
```

**Documentação interativa do FastAPI:**
```
http://localhost:8000/docs
```

---

## 📁 Estrutura do Projeto

```
api-calculadora/
├── api.py            # Código principal da API
├── index.html        # Interface web
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação
```

---

## 👨‍💻 Autor

Feito com por ViniciusMB
