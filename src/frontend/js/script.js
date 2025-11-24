const calcularBtn = document.getElementById('calcular-btn');
const resultadoDiv = document.getElementById('resultado');

 async function fCalcular(tipo) {
    try {
        const dados = {
                cargo: document.getElementById('txtCargo').value,
                horas_trabalhadas: parseInt(document.getElementById('txtHorasTrabalhadas').value),
                nome: document.getElementById('txtNome').value
            };
        const response = await fetch('http://127.0.0.1:8001/calcular-geral',{
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(dados)
    });
        const data = await response.json();
        resultadoDiv.innerText = ""
         document.all.divResposta.style.display="none";
        
        if (typeof data.detail !== "undefined"){
            for (let i =0; i< data.detail.length; i++){
                if (data.detail[i].type == "string_too_short"){
                    resultadoDiv.innerText +=  "\n" + "Verificar preenchimento do campo Nome: " + data.detail[0].msg;      
                }
                if (data.detail[i].type == "enum"){
                    resultadoDiv.innerText +=  "\n" + "Verificar preenchimento do Cargo: " + data.detail[0].msg;      
                }
                if (data.detail[i].type == "float_type"  || (data.detail[i].type == "less_than_equal") || (data.detail[i].type == "greater_than")){
                    resultadoDiv.innerText +=  "\n" + "Verificar preenchimento do campo Horas Trabalhadas: " + data.detail[0].msg;      
                }
                
            }
            
            //resultadoDiv.innerText +=  "\n" + data.detail[0].msg;
            return 
        }
        
        document.all.trSalarioBase.style.display="none"
        document.all.trBonus.style.display="none"
        document.all.trSalarioTotal.style.display="none"
        document.all.trFerias.style.display="none"
        document.all.tr13.style.display="none"

        if (tipo == "GERAL") { 
            document.all.trSalarioBase.style.display="table-row"
            document.all.trBonus.style.display="table-row"
            document.all.trSalarioTotal.style.display="table-row"
            document.all.trFerias.style.display="table-row"
            document.all.tr13.style.display="table-row"

            document.all.spnSalarioBase.innerText = formatarMoeda(data.salario_base);
            document.all.spnBonus.innerText = data.percentual_bonus + "%";
            document.all.spnSalarioTotal.innerText = formatarMoeda(data.salario_total);
            document.all.spnFerias.innerText =formatarMoeda(data.ferias);
            document.all.spn13.innerText = formatarMoeda(data.decimo_terceiro);
        }
        if (tipo == "BONUS") {
            document.all.trBonus.style.display="table-row"
        }
        if (tipo == "FERIAS") {
            document.all.spnFerias.innerText =formatarMoeda(data.ferias);         
            document.all.trFerias.style.display="table-row"
        }
        if (tipo == "13") {
            document.all.spn13.innerText = formatarMoeda(data.decimo_terceiro);
            document.all.tr13.style.display="table-row"
        }
        document.all.divResposta.style.display="block";
        

    } catch (error) {
        resultadoDiv.innerText += `Erro: ${error.message}`;
    }
};


// Função para formatar moeda
function formatarMoeda(valor) {
    return valor.toLocaleString('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    });
}