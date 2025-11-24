from .funcionario_base import Funcionario

class Diretor(Funcionario):
    
    @property
    def valor_hora(self) -> float:
        return 200.0
    
    @property
    def percentual_bonus(self) -> float:
        return 10.0