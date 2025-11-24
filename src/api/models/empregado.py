from .funcionario_base import Funcionario

class Empregado(Funcionario):
    
    @property
    def valor_hora(self) -> float:
        return 100.0 
    
    @property
    def percentual_bonus(self) -> float:
        return 10.0