from src.api.models.estagiario import Estagiario
from src.api.models.empregado import Empregado
from src.api.models.gerente import Gerente
from src.api.models.diretor import Diretor
from src.api.schemas.funcionario_schema import FuncionarioInput, CargoEnum


def criar_funcionario(dados: FuncionarioInput):
    if dados.cargo == CargoEnum.estagiario:
        return Estagiario(nome=dados.nome, horas_trabalhadas=dados.horas_trabalhadas)
    elif dados.cargo == CargoEnum.empregado:
        return Empregado(nome=dados.nome, horas_trabalhadas=dados.horas_trabalhadas)
    elif dados.cargo == CargoEnum.gerente:
        return Gerente(nome=dados.nome, horas_trabalhadas=dados.horas_trabalhadas)
    elif dados.cargo == CargoEnum.diretor:
        return Diretor(nome=dados.nome, horas_trabalhadas=dados.horas_trabalhadas)
    else:
        raise ValueError(f"Cargo inválido: {dados.cargo}")


def calcular_folha_completa(dados: FuncionarioInput) -> dict:
    funcionario = criar_funcionario(dados)
    return funcionario.obter_resumo()


def calcular_bonus(dados: FuncionarioInput) -> dict:
    funcionario = criar_funcionario(dados)
    return {
        "nome": funcionario.nome,
        "cargo": dados.cargo.value,
        "valor_calculado": round(funcionario.calcular_valor_bonus(), 2),
        "tipo_calculo": "Bônus"
    }


def calcular_ferias(dados: FuncionarioInput) -> dict:
    funcionario = criar_funcionario(dados)
    return {
        "nome": funcionario.nome,
        "cargo": dados.cargo.value,
        "valor_calculado": round(funcionario.calcular_ferias(), 2),
        "tipo_calculo": "Férias"
    }


def calcular_decimo_terceiro(dados: FuncionarioInput) -> dict:
    funcionario = criar_funcionario(dados)
    return {
        "nome": funcionario.nome,
        "cargo": dados.cargo.value,
        "valor_calculado": round(funcionario.calcular_13_salario(), 2),
        "tipo_calculo": "Décimo Terceiro"
    }