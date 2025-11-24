
import pytest
import logging
from src.api.models.estagiario import Estagiario
from src.api.models.empregado import Empregado
from src.api.models.gerente import Gerente
from src.api.models.diretor import Diretor

logger = logging.getLogger(__name__)


# ==================== TESTES DE ESTAGIÁRIO ====================

def test_estagiario_reginaldo_tanno_valores_base():
    """Testa valores base do Estagiário Reginaldo TANNO"""
    logger.info("=" * 60)
    logger.info("TESTANDO: Estagiário - Reginaldo TANNO")
    logger.info("=" * 60)
    
    # Arrange (Preparar)
    est = Estagiario(nome="Reginaldo TANNO", horas_trabalhadas=160.0)
    
    # Act (Agir)
    resumo = est.obter_resumo()
    
    # Log dos valores obtidos
    logger.info(f"Nome: {resumo['nome']}")
    logger.info(f"Cargo: {resumo['cargo']}")
    logger.info(f"Horas Trabalhadas: {resumo['horas_trabalhadas']}")
    logger.info(f"Valor/Hora: R$ {resumo['valor_hora']:.2f}")
    logger.info(f"Percentual Bônus: {resumo['percentual_bonus']}%")
    
    # Assert (Validar)
    assert resumo['nome'] == "Reginaldo TANNO", "Nome incorreto"
    assert resumo['cargo'] == "Estagiario", "Cargo incorreto"
    assert resumo['valor_hora'] == 50.0, "Valor/hora deve ser R$ 50,00"
    assert resumo['percentual_bonus'] == 10.0, "Bônus deve ser 10%"
    
    logger.info("✅ VALORES BASE: CORRETOS!")


def test_estagiario_reginaldo_tanno_calculos():
    """Testa cálculos financeiros do Estagiário Reginaldo TANNO"""
    logger.info("Testando CÁLCULOS do Estagiário")
    
    # Arrange
    est = Estagiario(nome="Reginaldo TANNO", horas_trabalhadas=160.0)
    
    # Act
    resumo = est.obter_resumo()
    
    # Valores esperados
    salario_base_esperado = 8000.0   # 160h × R$ 50
    bonus_esperado = 800.0           # R$ 8.000 × 10%
    salario_total_esperado = 8800.0  # R$ 8.000 + R$ 800
    
    # Log dos cálculos
    logger.info(f"Salário Base: R$ {resumo['salario_base']:,.2f}")
    logger.info(f"Valor Bônus: R$ {resumo['valor_bonus']:,.2f}")
    logger.info(f"Salário Total: R$ {resumo['salario_total']:,.2f}")
    logger.info(f"Férias: R$ {resumo['ferias']:,.2f}")
    logger.info(f"13º Salário: R$ {resumo['decimo_terceiro']:,.2f}")
    
    # Assert
    assert resumo['salario_base'] == salario_base_esperado, \
        f"Salário base incorreto! Esperado: {salario_base_esperado}, Obtido: {resumo['salario_base']}"
    
    assert resumo['valor_bonus'] == bonus_esperado, \
        f"Bônus incorreto! Esperado: {bonus_esperado}, Obtido: {resumo['valor_bonus']}"
    
    assert resumo['salario_total'] == salario_total_esperado, \
        f"Salário total incorreto! Esperado: {salario_total_esperado}, Obtido: {resumo['salario_total']}"
    
    assert resumo['decimo_terceiro'] == salario_total_esperado, \
        "13º salário deve ser igual ao salário total"
    
    logger.info("✅ CÁLCULOS: CORRETOS!")


# ==================== TESTES DE EMPREGADO ====================

def test_empregado_reginaldo_tanno_valores_base():
    """Testa valores base do Empregado Reginaldo TANNO"""
    logger.info("=" * 60)
    logger.info("TESTANDO: Empregado (Funcionário Comum) - Reginaldo TANNO")
    logger.info("=" * 60)
    
    # Arrange
    emp = Empregado(nome="Reginaldo TANNO", horas_trabalhadas=160.0)
    
    # Act
    resumo = emp.obter_resumo()
    
    # Log
    logger.info(f"Nome: {resumo['nome']}")
    logger.info(f"Cargo: {resumo['cargo']}")
    logger.info(f"Valor/Hora: R$ {resumo['valor_hora']:.2f}")
    logger.info(f"Percentual Bônus: {resumo['percentual_bonus']}%")
    
    # Assert
    assert resumo['nome'] == "Reginaldo TANNO"
    assert resumo['valor_hora'] == 100.0, "Empregado deve ganhar R$ 100/hora"
    assert resumo['percentual_bonus'] == 10.0, "Empregado deve ter bônus de 10%"
    
    logger.info("✅ VALORES BASE: CORRETOS!")


def test_empregado_reginaldo_tanno_calculos():
    """Testa cálculos financeiros do Empregado Reginaldo TANNO"""
    logger.info("Testando CÁLCULOS do Empregado")
    
    # Arrange
    emp = Empregado(nome="Reginaldo TANNO", horas_trabalhadas=160.0)
    
    # Act
    resumo = emp.obter_resumo()
    
    # Valores esperados
    salario_base_esperado = 16000.0   # 160h × R$ 100
    bonus_esperado = 1600.0           # R$ 16.000 × 10%
    salario_total_esperado = 17600.0  # R$ 16.000 + R$ 1.600
    
    # Log
    logger.info(f"Salário Base: R$ {resumo['salario_base']:,.2f}")
    logger.info(f"Valor Bônus: R$ {resumo['valor_bonus']:,.2f}")
    logger.info(f"Salário Total: R$ {resumo['salario_total']:,.2f}")
    
    # Assert
    assert resumo['salario_base'] == salario_base_esperado
    assert resumo['valor_bonus'] == bonus_esperado
    assert resumo['salario_total'] == salario_total_esperado
    
    logger.info("✅ CÁLCULOS: CORRETOS!")


# ==================== TESTES DE GERENTE ====================

def test_gerente_renato_lira_valores_base():
    """Testa valores base do Gerente Renato Lira"""
    logger.info("=" * 60)
    logger.info("TESTANDO: Gerente - Renato Lira")
    logger.info("=" * 60)
    
    # Arrange
    ger = Gerente(nome="Renato Lira", horas_trabalhadas=160.0)
    
    # Act
    resumo = ger.obter_resumo()
    
    # Log
    logger.info(f"Nome: {resumo['nome']}")
    logger.info(f"Cargo: {resumo['cargo']}")
    logger.info(f"Valor/Hora: R$ {resumo['valor_hora']:.2f}")
    logger.info(f"Percentual Bônus: {resumo['percentual_bonus']}%")
    
    # Assert
    assert resumo['nome'] == "Renato Lira"
    assert resumo['valor_hora'] == 100.0, "Gerente deve ganhar R$ 100/hora"
    assert resumo['percentual_bonus'] == 15.0, "Gerente deve ter bônus DIFERENCIADO de 15%!"
    
    logger.info("✅ VALORES BASE: CORRETOS! (Bônus diferenciado confirmado)")


def test_gerente_renato_lira_calculos():
    """Testa cálculos financeiros do Gerente Renato Lira"""
    logger.info("Testando CÁLCULOS do Gerente")
    
    # Arrange
    ger = Gerente(nome="Renato Lira", horas_trabalhadas=160.0)
    
    # Act
    resumo = ger.obter_resumo()
    
    # Valores esperados
    salario_base_esperado = 16000.0   # 160h × R$ 100
    bonus_esperado = 2400.0           # R$ 16.000 × 15% (DIFERENCIADO!)
    salario_total_esperado = 18400.0  # R$ 16.000 + R$ 2.400
    
    # Log
    logger.info(f"Salário Base: R$ {resumo['salario_base']:,.2f}")
    logger.info(f"Valor Bônus: R$ {resumo['valor_bonus']:,.2f} (15% - DIFERENCIADO)")
    logger.info(f"Salário Total: R$ {resumo['salario_total']:,.2f}")
    logger.info(f"Férias: R$ {resumo['ferias']:,.2f}")
    logger.info(f"13º Salário: R$ {resumo['decimo_terceiro']:,.2f}")
    
    # Assert
    assert resumo['salario_base'] == salario_base_esperado
    assert resumo['valor_bonus'] == bonus_esperado, \
        "Gerente deve ter bônus de 15%, não 10%!"
    assert resumo['salario_total'] == salario_total_esperado
    
    logger.info("✅ CÁLCULOS: CORRETOS!")


# ==================== TESTES DE DIRETOR ====================

def test_diretor_rogerio_alves_valores_base():
    """Testa valores base do Diretor Rogério Alves"""
    logger.info("=" * 60)
    logger.info("TESTANDO: Diretor - Rogério Alves")
    logger.info("=" * 60)
    
    # Arrange
    dir = Diretor(nome="Rogério Alves", horas_trabalhadas=120.0)
    
    # Act
    resumo = dir.obter_resumo()
    
    # Log
    logger.info(f"Nome: {resumo['nome']}")
    logger.info(f"Cargo: {resumo['cargo']}")
    logger.info(f"Valor/Hora: R$ {resumo['valor_hora']:.2f}")
    logger.info(f"Percentual Bônus: {resumo['percentual_bonus']}%")
    
    # Assert
    assert resumo['nome'] == "Rogério Alves"
    assert resumo['valor_hora'] == 200.0, "Diretor deve ganhar R$ 200/hora!"
    assert resumo['percentual_bonus'] == 10.0, "Diretor deve ter bônus padrão de 10%"
    
    logger.info("✅ VALORES BASE: CORRETOS!")


def test_diretor_rogerio_alves_calculos():
    """Testa cálculos financeiros do Diretor Rogério Alves"""
    logger.info("Testando CÁLCULOS do Diretor")
    
    # Arrange
    dir = Diretor(nome="Rogério Alves", horas_trabalhadas=120.0)
    
    # Act
    resumo = dir.obter_resumo()
    
    # Valores esperados
    salario_base_esperado = 24000.0   # 120h × R$ 200
    bonus_esperado = 2400.0           # R$ 24.000 × 10%
    salario_total_esperado = 26400.0  # R$ 24.000 + R$ 2.400
    
    # Log
    logger.info(f"Salário Base: R$ {resumo['salario_base']:,.2f}")
    logger.info(f"Valor Bônus: R$ {resumo['valor_bonus']:,.2f}")
    logger.info(f"Salário Total: R$ {resumo['salario_total']:,.2f}")
    logger.info(f"Férias: R$ {resumo['ferias']:,.2f}")
    logger.info(f"13º Salário: R$ {resumo['decimo_terceiro']:,.2f}")
    
    # Assert
    assert resumo['salario_base'] == salario_base_esperado
    assert resumo['valor_bonus'] == bonus_esperado
    assert resumo['salario_total'] == salario_total_esperado
    
    logger.info("✅ CÁLCULOS: CORRETOS!")


# ==================== TESTE RESUMO FINAL ====================

def test_resumo_comparativo_todos_cargos():
    """Teste comparativo entre todos os cargos"""
    logger.info("=" * 60)
    logger.info("TESTE COMPARATIVO - TODOS OS CARGOS")
    logger.info("=" * 60)
    
    # Arrange - Criar todos com 160h para comparar
    estagiario = Estagiario(nome="Reginaldo TANNO", horas_trabalhadas=160.0)
    empregado = Empregado(nome="Reginaldo TANNO", horas_trabalhadas=160.0)
    gerente = Gerente(nome="Renato Lira", horas_trabalhadas=160.0)
    diretor = Diretor(nome="Rogério Alves", horas_trabalhadas=160.0)
    
    # Log comparativo
    logger.info("\n📊 COMPARAÇÃO DE SALÁRIOS (160 horas):")
    logger.info(f"Estagiário:  R$ {estagiario.calcular_salario_total():>10,.2f}")
    logger.info(f"Empregado:   R$ {empregado.calcular_salario_total():>10,.2f}")
    logger.info(f"Gerente:     R$ {gerente.calcular_salario_total():>10,.2f} (bônus 15%)")
    logger.info(f"Diretor:     R$ {diretor.calcular_salario_total():>10,.2f}")
    
    # Assert - Validar ordem de salários
    assert estagiario.calcular_salario_total() < empregado.calcular_salario_total(), \
        "Empregado deve ganhar mais que Estagiário"
    
    assert empregado.calcular_salario_total() < gerente.calcular_salario_total(), \
        "Gerente deve ganhar mais que Empregado (por causa do bônus de 15%)"
    
    assert gerente.calcular_salario_total() < diretor.calcular_salario_total(), \
        "Diretor deve ganhar mais que Gerente"
    
    logger.info("\n✅ HIERARQUIA SALARIAL: CORRETA!")


# ==================== TESTE DE VALIDAÇÃO PYDANTIC ====================

def test_validacao_horas_negativas_deve_falhar():
    """Testa se horas negativas são rejeitadas pelo Pydantic"""
    logger.info("Testando VALIDAÇÃO: horas negativas devem falhar")
    
    from pydantic import ValidationError
    
    with pytest.raises(ValidationError) as exc_info:
        Empregado(nome="Teste", horas_trabalhadas=-10.0)
    
    logger.info(f"✅ Validação funcionou! Erro: {exc_info.value.errors()[0]['type']}")
    assert "greater_than" in str(exc_info.value)


def test_validacao_nome_curto_deve_falhar():
    """Testa se nome muito curto é rejeitado pelo Pydantic"""
    logger.info("Testando VALIDAÇÃO: nome muito curto deve falhar")
    
    from pydantic import ValidationError
    
    with pytest.raises(ValidationError) as exc_info:
        Gerente(nome="A", horas_trabalhadas=160.0)
    
    logger.info(f"✅ Validação funcionou! Erro: {exc_info.value.errors()[0]['type']}")
    assert "string_too_short" in str(exc_info.value)