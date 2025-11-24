from enum import Enum
from pydantic import BaseModel, Field, field_validator, PositiveFloat


class CargoEnum(str, Enum):
    diretor = "diretor"
    gerente = "gerente"
    empregado = "empregado"
    estagiario = "estagiario"


class FuncionarioInput(BaseModel):
    nome: str = Field(
        ...,
        min_length=3,
        max_length=100,
        examples=["Rogério Alves"]
    )
    
    cargo: CargoEnum = Field(...)
    
    horas_trabalhadas: PositiveFloat = Field(
        ...,
        le=300,
        examples=[160.0]
    )
    
    @field_validator("nome")
    @classmethod
    def validar_nome(cls, v: str) -> str:
        if not v.replace(" ", "").replace("-", "").isalpha():
            raise ValueError("Nome deve conter apenas letras, espaços e hífens")
        return v.title()
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Rogério Alves",
                    "cargo": "gerente",
                    "horas_trabalhadas": 160.0
                }
            ]
        }
    }


class ResumoOutput(BaseModel):
    nome: str
    cargo: str
    horas_trabalhadas: float
    valor_hora: float
    salario_base: float
    percentual_bonus: float
    valor_bonus: float
    salario_total: float
    ferias: float
    decimo_terceiro: float
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Rogério Alves",
                    "cargo": "Gerente",
                    "horas_trabalhadas": 160.0,
                    "valor_hora": 100.0,
                    "salario_base": 16000.0,
                    "percentual_bonus": 15.0,
                    "valor_bonus": 2400.0,
                    "salario_total": 18400.0,
                    "ferias": 23733.33,
                    "decimo_terceiro": 18400.0
                }
            ]
        }
    }


class CalculoSimplesOutput(BaseModel):
    nome: str
    cargo: str
    valor_calculado: float
    tipo_calculo: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nome": "Rogério Alves",
                    "cargo": "gerente",
                    "valor_calculado": 2400.0,
                    "tipo_calculo": "Bônus"
                }
            ]
        }
    }