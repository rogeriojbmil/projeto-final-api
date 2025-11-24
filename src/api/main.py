import uvicorn
import logging
from fastapi import FastAPI, HTTPException, status

from src.api.schemas.funcionario_schema import FuncionarioInput, ResumoOutput, CalculoSimplesOutput
from src.data.folha_service import (
    calcular_folha_completa,
    calcular_bonus,
    calcular_ferias,
    calcular_decimo_terceiro
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="API Folha de Pagamento",
    description="Sistema de cálculo de folha de pagamento desenvolvido pelos alunos Reginaldo Tanno, Renato Lira e Rogério Alves",
    version="1.0.0"
)


@app.on_event("startup")
async def startup_event():
    logger.info("=" * 60)
    logger.info("API de Folha de Pagamento iniciada")
    logger.info("Desenvolvido por: Reginaldo Tanno, Renato Lira, Rogério Alves")
    logger.info("=" * 60)


@app.post("/calcular-geral", response_model=ResumoOutput, tags=["Cálculos"])
def calcular_tudo(dados: FuncionarioInput):
    logger.info(f"POST /calcular-geral - Funcionário: {dados.nome}, Cargo: {dados.cargo.value}")
    try:
        resultado = calcular_folha_completa(dados)
        logger.info(f"Cálculo concluído - Salário total: R$ {resultado['salario_total']:.2f}")
        return resultado
    except ValueError as e:
        logger.warning(f"Erro de validação: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Erro interno: {str(e)}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro interno: {str(e)}")


@app.post("/calcular-bonus", response_model=CalculoSimplesOutput, tags=["Cálculos"])
def calcular_apenas_bonus(dados: FuncionarioInput):
    logger.info(f"POST /calcular-bonus - Funcionário: {dados.nome}")
    try:
        resultado = calcular_bonus(dados)
        logger.info(f"Bônus calculado: R$ {resultado['valor_calculado']:.2f}")
        return resultado
    except ValueError as e:
        logger.warning(f"Erro de validação: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Erro interno: {str(e)}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro interno: {str(e)}")


@app.post("/calcular-ferias", response_model=CalculoSimplesOutput, tags=["Cálculos"])
def calcular_apenas_ferias(dados: FuncionarioInput):
    logger.info(f"POST /calcular-ferias - Funcionário: {dados.nome}")
    try:
        resultado = calcular_ferias(dados)
        logger.info(f"Férias calculadas: R$ {resultado['valor_calculado']:.2f}")
        return resultado
    except ValueError as e:
        logger.warning(f"Erro de validação: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Erro interno: {str(e)}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro interno: {str(e)}")


@app.post("/calcular-13", response_model=CalculoSimplesOutput, tags=["Cálculos"])
def calcular_apenas_13(dados: FuncionarioInput):
    logger.info(f"POST /calcular-13 - Funcionário: {dados.nome}")
    try:
        resultado = calcular_decimo_terceiro(dados)
        logger.info(f"13º salário calculado: R$ {resultado['valor_calculado']:.2f}")
        return resultado
    except ValueError as e:
        logger.warning(f"Erro de validação: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Erro interno: {str(e)}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro interno: {str(e)}")


@app.get("/", tags=["Info"])
def root():
    logger.info("GET / - Endpoint raiz acessado")
    return {
        "message": "API de Folha de Pagamento",
        "version": "1.0.0",
        "desenvolvido_por": ["Reginaldo Tanno", "Renato Lira", "Rogério Alves"],
        "endpoints": {
            "calcular_geral": "/calcular-geral",
            "calcular_bonus": "/calcular-bonus",
            "calcular_ferias": "/calcular-ferias",
            "calcular_13": "/calcular-13",
            "docs": "/docs"
        }
    }


if __name__ == "__main__":
    logger.info("Iniciando servidor uvicorn...")
    uvicorn.run("src.api.main:app", host="127.0.0.1", port=8015)