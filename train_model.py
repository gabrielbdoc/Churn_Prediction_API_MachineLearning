import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Carrega o dataset real
df = pd.read_csv("data/churn.csv")

# Remove colunas irrelevantes ou que causam problemas
df.drop(['customerID'], axis=1, inplace=True)

# Trata valores nulos
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')
df.dropna(inplace=True)

# Codifica variáveis categóricas
cat_cols = df.select_dtypes(include='object').columns
le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# Divide em X e y
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Split e treino
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Salva o modelo
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")

# Salva também as colunas para futura entrada na API
joblib.dump(X.columns.tolist(), "models/columns.pkl")

print("Modelo e colunas salvos com sucesso.")