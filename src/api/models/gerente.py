from .funcionario_base import Funcionario
from src.config import settings

class Gerente(Funcionario):
   
    @property
    def valor_hora(self) -> float:
        return settings.VALOR_HORA_GERENTE
   
    @property
    def percentual_bonus(self) -> float:
        return settings.BONUS_GERENTE
