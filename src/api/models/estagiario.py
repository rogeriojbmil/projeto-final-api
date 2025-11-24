from .funcionario_base import Funcionario

class Estagiario(Funcionario):
    
    @property
    def valor_hora(self) -> float:
        return 50.0
    
    @property
    def percentual_bonus(self) -> float:
        return 10.0