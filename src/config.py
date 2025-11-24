"""
Configurações centralizadas da API de Folha de Pagamento.

Este módulo usa Pydantic Settings para:
- Carregar variáveis de ambiente do arquivo .env
- Validar tipos automaticamente
- Fornecer valores padrão seguros
- Centralizar todas as configurações do sistema
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """
    Classe de configurações da aplicação.
    
    Atributos são carregados automaticamente do arquivo .env ou
    podem ser sobrescritos por variáveis de ambiente do sistema.
    """
    
    # Informações da Aplicação
    APP_NAME: str = "API Folha de Pagamento"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Sistema de cálculo de folha de pagamento com FastAPI"
    DEBUG: bool = True
    
    # Configurações do Servidor
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True
    
    # Regras de Negócio - Folha de Pagamento
    MAX_HORAS_MES: int = 300
    MIN_HORAS_MES: float = 0.0
    
    # Valores por Hora (em Reais)
    VALOR_HORA_ESTAGIARIO: float = 50.0
    VALOR_HORA_EMPREGADO: float = 100.0
    VALOR_HORA_GERENTE: float = 100.0
    VALOR_HORA_DIRETOR: float = 200.0
    
    # Bonificações (em percentual 0-100)
    BONUS_PADRAO: float = 10.0
    BONUS_GERENTE: float = 15.0
    BONUS_DIRETOR: float = 10.0
    BONUS_ESTAGIARIO: float = 10.0
    
    # Regras de Férias e 13º
    ADICIONAL_FERIAS_FATOR: float = 1/3  # 1/3 adicional sobre salário base
    DECIMO_TERCEIRO_INTEGRAL: bool = True  # Se False, calcular proporcional
    
    # Configurações de Logging
    LOG_LEVEL: str = "DEBUG"
    LOG_FILE: str = "logs/app.log"
    LOG_MAX_BYTES: int = 5_000_000  # 5MB
    LOG_BACKUP_COUNT: int = 3
    
    # Configurações do Pydantic
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"  # Ignora variáveis extras no .env
    )


# Instância global de configurações
# Use esta instância em todo o projeto
settings = Settings()


# Função helper para debug
def print_settings():
    """Imprime configurações atuais (útil para debug)"""
    print("=" * 50)
    print("CONFIGURAÇÕES DA APLICAÇÃO")
    print("=" * 50)
    print(f"App: {settings.APP_NAME} v{settings.APP_VERSION}")
    print(f"Debug: {settings.DEBUG}")
    print(f"Host: {settings.HOST}:{settings.PORT}")
    print(f"Max Horas/Mês: {settings.MAX_HORAS_MES}")
    print(f"Bonus Gerente: {settings.BONUS_GERENTE}%")
    print("=" * 50)


if __name__ == "__main__":
    # Teste do módulo
    print_settings()
