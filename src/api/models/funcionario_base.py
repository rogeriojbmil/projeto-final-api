from abc import ABC, abstractmethod
from pydantic import BaseModel, Field, PositiveFloat

class Funcionario(BaseModel, ABC):
    nome: str = Field(..., min_length=2)
    horas_trabalhadas: PositiveFloat = Field(...)

    model_config = {
        "validate_assignment": True,
        "ignored_types": (property,)
    }

    @property
    @abstractmethod
    def valor_hora(self) -> float:
        pass
    
    @property
    @abstractmethod
    def percentual_bonus(self) -> float:
        pass
    
    def calcular_salario_base(self) -> float:
        return self.horas_trabalhadas * self.valor_hora
    
    def calcular_valor_bonus(self) -> float:
        salario_base = self.calcular_salario_base()
        return salario_base * (self.percentual_bonus / 100)
    
    def calcular_salario_total(self) -> float:
        salario_base = self.calcular_salario_base()
        bonus = self.calcular_valor_bonus()
        return salario_base + bonus
    
    def calcular_ferias(self) -> float:
        salario_total = self.calcular_salario_total()
        adicional_terco = self.calcular_salario_base() / 3
        return salario_total + adicional_terco
    
    def calcular_13_salario(self) -> float:
        return self.calcular_salario_total()
    
    def obter_resumo(self) -> dict:
        return {
            "nome": self.nome,
            "cargo": self.__class__.__name__,
            "horas_trabalhadas": self.horas_trabalhadas,
            "valor_hora": self.valor_hora,
            "salario_base": round(self.calcular_salario_base(), 2),
            "percentual_bonus": self.percentual_bonus,
            "valor_bonus": round(self.calcular_valor_bonus(), 2),
            "salario_total": round(self.calcular_salario_total(), 2),
            "ferias": round(self.calcular_ferias(), 2),
            "decimo_terceiro": round(self.calcular_13_salario(), 2)
        }