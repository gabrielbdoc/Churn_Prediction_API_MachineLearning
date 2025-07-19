import os
import joblib

# Caminho absoluto baseado na raiz do projeto
base_path = os.path.dirname(os.path.dirname(__file__))

model = joblib.load(os.path.join(base_path, "models", "model.pkl"))
columns = joblib.load(os.path.join(base_path, "models", "columns.pkl"))
