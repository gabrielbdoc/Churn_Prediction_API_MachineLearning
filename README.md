# ML Churn Prediction API

Este projeto implementa uma API de Machine Learning para previsão de *churn* (cancelamento de clientes), utilizando um modelo treinado em dados reais de comportamento de clientes. A API foi construída com **FastAPI**, e o modelo foi treinado com **scikit-learn**.

---

# Funcionalidades

- Previsão de churn (cliente irá ou não cancelar o serviço)
- Validação automática dos dados de entrada com Pydantic
- Estrutura de testes automatizados com `pytest`
- Pronto para deploy via containers ou serviços de nuvem

---

# Base de Dados

O modelo foi treinado usando o dataset **[Credit Card Churn Prediction](https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction)**, disponível publicamente no Kaggle.

A base contém informações demográficas e comportamentais de clientes, como:

- Tempo de permanência no serviço (`tenure`)
- Serviços contratados (internet, suporte técnico, backup, etc.)
- Informações de pagamento
- Perfil demográfico (gênero, idade, dependentes)

Essas variáveis foram processadas e utilizadas como base para treinar o modelo de classificação.

---

# Modelo

O modelo de machine learning utilizado é um **Random Forest Classifier**, treinado para prever a probabilidade de churn com base nas variáveis fornecidas.

---

# Tecnologias Utilizadas

- Python 3.12
- FastAPI
- Uvicorn
- scikit-learn
- Pandas / NumPy
- Pydantic
- Pytest

---

# Como Rodar Localmente

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/ML_Churn_Prediction.git
cd ML_Churn_Prediction
```

2. Crie e ative o ambiente virtual
```bash
python -m venv .venv
source .venv/Scripts/activate
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Execute a API localmente
```bash
uvicorn app.main:app --reload
```

5. Acesse a API
Acesse a documentação automática em: http://127.0.0.1:8000/docs

---
# Exemplo de Requisição
```json
POST /predict/
{
  "gender": 1.0,
  "SeniorCitizen": 0.0,
  "Partner": 1.0,
  "Dependents": 0.0,
  "tenure": 12.0,
  "PhoneService": 1.0,
  "MultipleLines": 0.0,
  "InternetService": 2.0,
  "OnlineSecurity": 1.0,
  "OnlineBackup": 1.0,
  "DeviceProtection": 1.0,
  "TechSupport": 0.0,
  "StreamingTV": 0.0,
  "StreamingMovies": 0.0,
  "Contract": 0.0,
  "PaperlessBilling": 1.0,
  "PaymentMethod": 1.0,
  "MonthlyCharges": 70.5,
  "TotalCharges": 845.3
}
```

Resposta Esperada
```json
{
  "churn": true
}
```

---
# Testes Automatizados
Os testes foram desenvolvidos utilizando pytest, com foco em garantir a integridade da API e do modelo de machine learning.

Cobertura dos testes atuais:

- test_root: Verifica se a API está online (GET /)
- test_docs: Verifica se a documentação automática está acessível (/docs)
- test_predict: Verifica se a rota /predict/ retorna resposta válida
- test_predict_churn_true: Testa o retorno churn=True com dados simulando cancelamento
- test_predict_churn_false: Testa o retorno churn=False com dados de cliente estável
- test_schema_validation: Garante que dados incompletos/disformes são rejeitados corretamente
- test_payload_structure: Garante que todos os campos obrigatórios estão presentes no payload

---
# Estrutura do Projeto
```graphql
ML_Churn_Prediction/
│
├── app/
│   ├── main.py          # Inicialização da API
│   ├── model.py         # Carregamento do modelo treinado e colunas
│   ├── predict.py       # Função de predição
│   └── schema.py        # Validação com Pydantic
│
├── tests/
│   └── test_api.py      # Testes automatizados com pytest
│
├── model/
│   └── churn_model.pkl  # Modelo treinado
│
├── requirements.txt
└── README.md
```

---

#Autor
Gabriel Cruz
