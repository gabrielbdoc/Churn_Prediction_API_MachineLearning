from pydantic import BaseModel, Field


class CustomerData(BaseModel):
    gender: float = Field(..., ge=0, le=1)  # 0 ou 1
    SeniorCitizen: float = Field(..., ge=0, le=1)  # 0 ou 1
    Partner: float = Field(..., ge=0, le=1)  # 0 ou 1
    Dependents: float = Field(..., ge=0, le=1)  # 0 ou 1
    tenure: float = Field(..., ge=0)  # >=0, meses
    PhoneService: float = Field(..., ge=0, le=1)  # 0 ou 1
    MultipleLines: float = Field(..., ge=0, le=1)  # 0 ou 1 (pode ajustar se valores diferentes)
    InternetService: float = Field(..., ge=0, le=3)  # supondo que vai de 0 a 3 (ex: None, DSL, Fiber, Outro)
    OnlineSecurity: float = Field(..., ge=0, le=1)  # 0 ou 1
    OnlineBackup: float = Field(..., ge=0, le=1)  # 0 ou 1
    DeviceProtection: float = Field(..., ge=0, le=1)  # 0 ou 1
    TechSupport: float = Field(..., ge=0, le=1)  # 0 ou 1
    StreamingTV: float = Field(..., ge=0, le=1)  # 0 ou 1
    StreamingMovies: float = Field(..., ge=0, le=1)  # 0 ou 1
    Contract: float = Field(..., ge=0, le=2)  # ex: 0,1,2 (ex: mensal, anual, etc)
    PaperlessBilling: float = Field(..., ge=0, le=1)  # 0 ou 1
    PaymentMethod: float = Field(..., ge=0, le=3)  # 0 a 3 (depende das categorias do seu dataset)
    MonthlyCharges: float = Field(..., ge=0)  # valores positivos
    TotalCharges: float = Field(..., ge=0)  # valores positivos
