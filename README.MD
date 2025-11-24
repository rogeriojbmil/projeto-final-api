# 💼 API de Folha de Pagamento - Projeto Final Módulo 1

> **Projeto de conclusão do Módulo 1 - IA Generativa com Python**  
> **Instituição:** IBMEC  
> **Disciplina:** Curso IA Generativa  
> **Data:** Novembro 2025

Sistema completo de cálculo de folha de pagamento desenvolvido com **FastAPI**, **Pydantic** e princípios sólidos de **Programação Orientada a Objetos (OOP)**, demonstrando a aplicação prática de conceitos fundamentais de arquitetura de software, testes automatizados e boas práticas de desenvolvimento.

---

## 👥 Equipe de Desenvolvimento

- **Renato Silva e Lira**
- **Reginaldo Toshiaki Tanno**
- **Rogério Alves da Conceição**

---

## 📚 Sobre o Projeto

Este projeto representa a culminação dos conhecimentos adquiridos no **Módulo 1** do curso de IA Generativa, com foco em:

### **Objetivos Principais:**
1. ✅ Aplicar conceitos fundamentais de **Programação Orientada a Objetos**
2. ✅ Desenvolver uma **API RESTful** profissional com FastAPI
3. ✅ Implementar **validação de dados** robusta com Pydantic
4. ✅ Criar **testes automatizados** com pytest
5. ✅ Aplicar **Clean Architecture** e separação de responsabilidades
6. ✅ Demonstrar **boas práticas** de engenharia de software
7. ✅ Implementar **sistema de logs** estruturado
8. ✅ Preparar projeto para **CI/CD** com GitHub Actions

### **Desafio Proposto:**
Criar um sistema de cálculo de folha de pagamento que suporte diferentes cargos, com regras de negócio específicas para bonificações, férias e 13º salário, aplicando os princípios de OOP e mantendo código testável, limpo e bem documentado.

---

## 🎓 Conceitos de Programação Orientada a Objetos Aplicados

Este projeto demonstra profundo entendimento e aplicação prática dos **4 pilares da OOP**:

### **1. 🧱 ABSTRAÇÃO**

Criamos uma **classe abstrata base** `Funcionario` que define o contrato que todas as classes concretas devem seguir:
```python
from abc import ABC, abstractmethod

class Funcionario(BaseModel, ABC):
    nome: str
    horas_trabalhadas: PositiveFloat
    
    @property
    @abstractmethod
    def valor_hora(self) -> float:
        """Cada cargo define seu próprio valor/hora"""
        pass
    
    @property
    @abstractmethod
    def percentual_bonus(self) -> float:
        """Cada cargo define seu próprio percentual de bônus"""
        pass
```

**Por que isso é importante?**
- ✅ Define um "contrato" que todas as subclasses devem cumprir
- ✅ Impossibilita criar instância de `Funcionario` diretamente
- ✅ Garante que todo funcionário tenha `valor_hora` e `percentual_bonus`

---

### **2. 🧬 HERANÇA**

Todas as classes de cargo **herdam** de `Funcionario`, reutilizando métodos comuns:
```python
class Gerente(Funcionario):
    @property
    def valor_hora(self) -> float:
        return 100.0
    
    @property
    def percentual_bonus(self) -> float:
        return 15.0  # Bônus diferenciado!
```


**Métodos herdados e reutilizados:**
- `calcular_salario_base()`
- `calcular_valor_bonus()`
- `calcular_salario_total()`
- `calcular_ferias()`
- `calcular_13_salario()`
- `obter_resumo()`

**Benefícios:**
- ✅ **DRY (Don't Repeat Yourself):** Código escrito uma vez, usado por todos
- ✅ **Facilidade de manutenção:** Mudar em um lugar afeta todos
- ✅ **Extensibilidade:** Adicionar novo cargo é simples

---

### **3. 🎭 POLIMORFISMO**

Diferentes cargos respondem de forma **diferente** aos mesmos métodos:
```python
# Mesmo método, comportamento diferente baseado no cargo
estagiario = Estagiario(nome="João", horas_trabalhadas=120)
diretor = Diretor(nome="Maria", horas_trabalhadas=120)

# Polimorfismo em ação:
print(estagiario.calcular_salario_base())  # 120 × 50 = 6.000
print(diretor.calcular_salario_base())     # 120 × 200 = 24.000
```

**Polimorfismo de Interface:**
```python
def calcular_para_funcionario(func: Funcionario):
    """Funciona para QUALQUER tipo de funcionário!"""
    return func.calcular_salario_total()

# Todos funcionam:
calcular_para_funcionario(Estagiario(...))
calcular_para_funcionario(Gerente(...))
calcular_para_funcionario(Diretor(...))
```

**Benefícios:**
- ✅ **Flexibilidade:** Código genérico funciona para tipos específicos
- ✅ **Extensibilidade:** Novos tipos funcionam automaticamente
- ✅ **Substituição de Liskov:** Subclasses podem substituir a classe base

---

### **4. 🔒 ENCAPSULAMENTO**

Protegemos dados e expusemos apenas o necessário através de **properties**:
```python
class Funcionario(BaseModel, ABC):
    # Dados protegidos pelo Pydantic
    nome: str = Field(..., min_length=2)
    horas_trabalhadas: PositiveFloat
    
    # Acesso controlado via properties
    @property
    def valor_hora(self) -> float:
        # Lógica interna protegida
        pass
    
    # Métodos públicos bem definidos
    def calcular_salario_base(self) -> float:
        return self.horas_trabalhadas * self.valor_hora
```

**Validações automáticas (Pydantic):**
- ✅ `nome` deve ter no mínimo 2 caracteres
- ✅ `horas_trabalhadas` deve ser positivo
- ✅ Tipos são validados automaticamente

**Benefícios:**
- ✅ **Proteção de dados:** Não pode criar estados inválidos
- ✅ **Interface clara:** Sabe exatamente o que pode usar
- ✅ **Mudanças seguras:** Alterar implementação interna não quebra código externo

---

## 🏗️ Arquitetura do Projeto

O projeto segue os princípios de **Clean Architecture** e **Separation of Concerns**:
```
projeto-final-api/
├── src/
│   ├── api/                    # Camada de Apresentação (API)
│   │   ├── models/             # Camada de Domínio (Entidades)
│   │   │   ├── funcionario_base.py   # Classe abstrata base
│   │   │   ├── gerente.py            # Implementação concreta
│   │   │   ├── diretor.py
│   │   │   ├── empregado.py
│   │   │   └── estagiario.py
│   │   ├── schemas/            # Camada de Validação (DTOs)
│   │   │   └── funcionario_schema.py # Request/Response schemas
│   │   └── main.py             # Controladores (Endpoints)
│   ├── data/                   # Camada de Aplicação (Services)
│   │   └── folha_service.py    # Lógica de negócio
│   └── config/                 # Configurações
│       └── config.py           # Settings centralizados
├── tests/                      # Testes Automatizados
│   └── test_models.py          # Testes unitários (11 testes)
├── logs/                       # Sistema de Logs
│   ├── app.log                 # Log geral
│   └── errors.log              # Log de erros
├── .gitignore                  # Arquivos ignorados pelo Git
├── pytest.ini                  # Configuração do pytest
├── requirements.txt            # Dependências
└── README.md                   # Documentação
```

### **Separação de Responsabilidades:**

| Camada | Responsabilidade | Exemplos |
|--------|------------------|----------|
| **Models** | Regras de negócio, cálculos | `Gerente.calcular_salario_base()` |
| **Schemas** | Validação de entrada/saída | `FuncionarioInput`, `ResumoOutput` |
| **Services** | Orquestração, lógica de aplicação | `criar_funcionario()`, `calcular_folha_completa()` |
| **API (main.py)** | Rotas HTTP, tratamento de erros | Endpoints FastAPI |
| **Config** | Configurações centralizadas | Valores parametrizados |

**Benefícios desta arquitetura:**
- ✅ **Testabilidade:** Cada camada pode ser testada isoladamente
- ✅ **Manutenibilidade:** Mudanças localizadas não afetam todo o sistema
- ✅ **Escalabilidade:** Fácil adicionar novos recursos
- ✅ **Reusabilidade:** Services podem ser usados por API, CLI, workers

---

## 💰 Regras de Negócio Implementadas

### **Valores por Hora (R$):**
| Cargo | Valor/Hora | Implementação |
|-------|------------|---------------|
| **Estagiário** | R$ 50,00 | `Estagiario.valor_hora` |
| **Empregado** | R$ 100,00 | `Empregado.valor_hora` |
| **Gerente** | R$ 100,00 | `Gerente.valor_hora` |
| **Diretor** | R$ 200,00 | `Diretor.valor_hora` |

### **Bonificações (%):**
| Cargo | Percentual | Observação |
|-------|------------|------------|
| **Padrão** | 10% | Estagiário, Empregado, Diretor |
| **Gerente** | 15% | **Diferenciado!** |

### **Fórmulas de Cálculo:**

#### **1. Salário Base:**
```
salario_base = horas_trabalhadas × valor_hora
```

#### **2. Bônus:**
```
valor_bonus = salario_base × (percentual_bonus ÷ 100)
```

#### **3. Salário Total:**
```
salario_total = salario_base + valor_bonus
```

#### **4. Férias (CLT):**
```
ferias = salario_total + (salario_base ÷ 3)
```
*Adicional de 1/3 constitucional sobre o salário base*

#### **5. 13º Salário:**
```
decimo_terceiro = salario_total
```
*Valor integral do salário mensal*

---

## 🛠️ Stack Tecnológica

### **Linguagem e Framework:**
- **Python 3.12** - Linguagem principal
- **FastAPI 0.115.0** - Framework web moderno, assíncrono e performático
- **Uvicorn 0.32.0** - Servidor ASGI de alta performance

### **Validação e Tipagem:**
- **Pydantic 2.9.2** - Validação de dados com type hints
- **Pydantic Settings 2.5.2** - Gerenciamento de configurações

### **Testes:**
- **Pytest 8.3.3** - Framework de testes
- **Pytest-cov 6.0.0** - Cobertura de código
- **Pytest-asyncio 0.24.0** - Testes assíncronos
- **HTTPX 0.27.0** - Cliente HTTP para testes de API

### **Documentação:**
- **Swagger UI** - Documentação interativa automática
- **ReDoc** - Documentação alternativa

---

## 📦 Instalação e Execução

### **Pré-requisitos:**
- Python 3.12+
- pip (gerenciador de pacotes)
- Git

### **1. Clonar o repositório:**
```bash
git clone https://github.com/seu-usuario/projeto-final-api.git
cd projeto-final-api
```

### **2. Criar e ativar ambiente virtual:**

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Instalar dependências:**
```bash
pip install -r requirements.txt
```

### **4. Executar a API:**
```bash
python -m uvicorn src.api.main:app --reload --port 8000
```

**Servidor iniciado em:** `http://localhost:8000`

**Documentação interativa:** `http://localhost:8000/docs`

---

## 🧪 Sistema de Testes

### **Cobertura de Testes:**

O projeto possui **11 testes automatizados** com **100% de aprovação**:
```bash
pytest -v
```

**Resultado:**
```
tests/test_models.py::test_estagiario_reginaldo_tanno_valores_base PASSED [ 9%]
tests/test_models.py::test_estagiario_reginaldo_tanno_calculos PASSED [18%]
tests/test_models.py::test_empregado_reginaldo_tanno_valores_base PASSED [27%]
tests/test_models.py::test_empregado_reginaldo_tanno_calculos PASSED [36%]
tests/test_models.py::test_gerente_renato_lira_valores_base PASSED [45%]
tests/test_models.py::test_gerente_renato_lira_calculos PASSED [54%]
tests/test_models.py::test_diretor_rogerio_alves_valores_base PASSED [63%]
tests/test_models.py::test_diretor_rogerio_alves_calculos PASSED [72%]
tests/test_models.py::test_resumo_comparativo_todos_cargos PASSED [81%]
tests/test_models.py::test_validacao_horas_negativas_deve_falhar PASSED [90%]
tests/test_models.py::test_validacao_nome_curto_deve_falhar PASSED [100%]

======================== 11 passed in 0.18s ==========================
```

### **Tipos de Testes Implementados:**

#### **1. Testes Unitários de Valores Base:**
- Verificam se cada cargo tem o `valor_hora` correto
- Verificam se cada cargo tem o `percentual_bonus` correto

#### **2. Testes de Cálculos Financeiros:**
- `calcular_salario_base()` - Validação da fórmula
- `calcular_valor_bonus()` - Validação do bônus
- `calcular_salario_total()` - Validação do total
- `calcular_ferias()` - Validação com 1/3 adicional
- `calcular_13_salario()` - Validação do 13º

#### **3. Testes de Validação (Pydantic):**
- Horas negativas devem falhar
- Nome com menos de 2 caracteres deve falhar
- Horas acima do máximo permitido devem falhar

#### **4. Testes de Hierarquia:**
- Verifica se a ordem salarial está correta:
```
  Estagiário < Empregado < Gerente < Diretor
```

### **Exemplo de Teste Profissional:**
```python
def test_gerente_renato_lira_calculos():
    """Testa cálculos financeiros do Gerente Renato Lira"""
    logger.info("Testando CÁLCULOS do Gerente")
    
    # Arrange (Preparar)
    ger = Gerente(nome="Renato Lira", horas_trabalhadas=160.0)
    
    # Act (Agir)
    resumo = ger.obter_resumo()
    
    # Valores esperados
    salario_base_esperado = 16000.0   # 160h × R$ 100
    bonus_esperado = 2400.0           # R$ 16.000 × 15%
    salario_total_esperado = 18400.0  # R$ 16.000 + R$ 2.400
    
    # Assert (Verificar)
    assert resumo['salario_base'] == salario_base_esperado
    assert resumo['valor_bonus'] == bonus_esperado
    assert resumo['salario_total'] == salario_total_esperado
    
    logger.info("✅ CÁLCULOS: CORRETOS!")
```

**Padrão AAA (Arrange, Act, Assert):**
- **Arrange:** Preparar dados de teste
- **Act:** Executar ação
- **Assert:** Verificar resultado

---

## 📡 API RESTful - Endpoints

### **POST /calcular-geral**
**Descrição:** Retorna resumo completo da folha de pagamento.

**Request Body:**
```json
{
  "nome": "Renato Silva e Lira",
  "cargo": "gerente",
  "horas_trabalhadas": 160.0
}
```

**Response (200 OK):**
```json
{
  "nome": "Renato Silva e Lira",
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
```

---

### **POST /calcular-bonus**
**Descrição:** Calcula apenas o bônus do funcionário.

**Request Body:**
```json
{
  "nome": "Rogério Alves da Conceição",
  "cargo": "diretor",
  "horas_trabalhadas": 160.0
}
```

**Response (200 OK):**
```json
{
  "nome": "Rogério Alves da Conceição",
  "cargo": "diretor",
  "valor_calculado": 3200.0,
  "tipo_calculo": "Bônus"
}
```

---

### **POST /calcular-ferias**
**Descrição:** Calcula férias (salário total + 1/3 adicional constitucional).

**Request Body:**
```json
{
  "nome": "Reginaldo Toshiaki Tanno",
  "cargo": "estagiario",
  "horas_trabalhadas": 120.0
}
```

**Response (200 OK):**
```json
{
  "nome": "Reginaldo Toshiaki Tanno",
  "cargo": "estagiario",
  "valor_calculado": 8800.0,
  "tipo_calculo": "Férias"
}
```

---

### **POST /calcular-13**
**Descrição:** Calcula 13º salário (salário total mensal).

**Request Body:**
```json
{
  "nome": "Renato Silva e Lira",
  "cargo": "empregado",
  "horas_trabalhadas": 160.0
}
```

**Response (200 OK):**
```json
{
  "nome": "Renato Silva e Lira",
  "cargo": "empregado",
  "valor_calculado": 17600.0,
  "tipo_calculo": "Décimo Terceiro"
}
```

---

### **GET /**
**Descrição:** Endpoint raiz com informações da API.

**Response (200 OK):**
```json
{
  "message": "API de Folha de Pagamento",
  "version": "1.0.0",
  "desenvolvido_por": [
    "Renato Silva e Lira",
    "Reginaldo Toshiaki Tanno",
    "Rogério Alves da Conceição"
  ],
  "endpoints": {
    "calcular_geral": "/calcular-geral",
    "calcular_bonus": "/calcular-bonus",
    "calcular_ferias": "/calcular-ferias",
    "calcular_13": "/calcular-13",
    "docs": "/docs"
  }
}
```

---

## 📝 Sistema de Logging

Sistema de logging estruturado implementado para rastreabilidade e debugging:

### **Níveis de Log:**
- **INFO:** Operações normais e fluxo da aplicação
- **WARNING:** Validações falhadas, dados incorretos
- **ERROR:** Erros internos com stack trace completo

### **Exemplo de Logs:**
```
2025-11-23 21:53:27,109 - src.api.main - INFO - ============================================================
2025-11-23 21:53:27,109 - src.api.main - INFO - API de Folha de Pagamento iniciada
2025-11-23 21:53:27,110 - src.api.main - INFO - Desenvolvido por: Renato Silva e Lira, Reginaldo Toshiaki Tanno, Rogério Alves da Conceição
2025-11-23 21:53:27,110 - src.api.main - INFO - ============================================================
2025-11-23 21:55:10,123 - src.api.main - INFO - POST /calcular-geral - Funcionário: Renato Silva e Lira, Cargo: gerente
2025-11-23 21:55:10,125 - src.data.folha_service - INFO - Calculando folha completa para Renato Silva e Lira
2025-11-23 21:55:10,126 - src.data.folha_service - INFO - Criando funcionário: Renato Silva e Lira - Cargo: gerente
2025-11-23 21:55:10,127 - src.data.folha_service - INFO - Folha completa calculada - Salário total: R$ 18400.00
2025-11-23 21:55:10,128 - src.api.main - INFO - Cálculo concluído - Salário total: R$ 18400.00
INFO:     127.0.0.1:54321 - "POST /calcular-geral HTTP/1.1" 200 OK
```

### **Configuração:**
```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

---

## 📊 Decisões Técnicas e Justificativas

### **1. Por que FastAPI?**
- ✅ Framework moderno e performático
- ✅ Documentação automática (Swagger/ReDoc)
- ✅ Validação integrada com Pydantic
- ✅ Suporte nativo a async/await
- ✅ Type hints obrigatórios (código mais seguro)

### **2. Por que Pydantic?**
- ✅ Validação de dados automática
- ✅ Serialização/deserialização JSON
- ✅ Integração perfeita com FastAPI
- ✅ Erros claros e descritivos
- ✅ Performance superior

### **3. Por que Classes Abstratas (ABC)?**
- ✅ Garante que todas as subclasses implementem métodos obrigatórios
- ✅ Previne erros em tempo de desenvolvimento
- ✅ Documenta o "contrato" da classe base
- ✅ Facilita manutenção e extensão

### **4. Por que Separar em Services?**
- ✅ API fica limpa (apenas roteamento)
- ✅ Lógica de negócio reutilizável
- ✅ Mais fácil de testar
- ✅ Pode ser usada por CLI, workers, etc.

### **5. Por que Pytest?**
- ✅ Sintaxe simples e pythônica
- ✅ Fixtures poderosas
- ✅ Parametrização de testes
- ✅ Plugins extensíveis
- ✅ Relatórios detalhados

---

## 🎓 Aprendizados e Desafios

### **Principais Aprendizados:**

1. **OOP na Prática:**
   - Aplicação real dos 4 pilares (Abstração, Herança, Polimorfismo, Encapsulamento)
   - Como estruturar hierarquia de classes
   - Quando usar classes abstratas vs concretas

2. **FastAPI + Pydantic:**
   - Integração poderosa entre framework e validação
   - Como criar APIs RESTful profissionais
   - Documentação automática é game-changer

3. **Testes Automatizados:**
   - Importância de testar desde o início
   - Como estruturar testes (AAA pattern)
   - Valor de ter 100% dos testes passando

4. **Clean Architecture:**
   - Separação de responsabilidades previne bagunça
   - Cada camada tem um propósito claro
   - Facilita manutenção e escalabilidade

5. **Logging:**
   - Logs estruturados facilitam debugging
   - Diferentes níveis para diferentes situações
   - Rastreabilidade é essencial

### **Equipe de Desenvolvimento:**

- **Renato Silva e Lira**
- **Reginaldo Toshiaki Tanno**
- **Rogério Alves da Conceição**

