from sqlite3.dbapi2 import Cursor
from flask_cors import CORS
from flask import *
import sqlite3
import json

app = Flask(__name__)
con = sqlite3.connect("Tabela_Salario.db")
cur = con.cursor
CORS(app)

#INSS
Faixa_fim_2 = con.execute('select FAIXA_FIM from INSS where INSS_ID = 2').fetchone()[0]
Faixa_fim_1 = con.execute('select FAIXA_FIM from INSS where INSS_ID = 1').fetchone()[0]
Faixa_fim_3 = con.execute('select FAIXA_FIM from INSS where INSS_ID = 3').fetchone()[0]
Faixa_fim_4 = con.execute('select FAIXA_FIM from INSS where INSS_ID = 4').fetchone()[0]
Faixa_inicio_5 = con.execute('select FAIXA_INICIO from INSS where INSS_ID = 5').fetchone()[0]

Aliquota_1 = con.execute('select ALIQUOTA from INSS where INSS_ID = 1').fetchone()[0]
Aliquota_2 = con.execute('select ALIQUOTA from INSS where INSS_ID = 2').fetchone()[0]
Aliquota_3 = con.execute('select ALIQUOTA from INSS where INSS_ID = 3').fetchone()[0]
Aliquota_4 = con.execute('select ALIQUOTA from INSS where INSS_ID = 4').fetchone()[0]
Aliquota_5 = con.execute('select ALIQUOTA from INSS where INSS_ID = 5').fetchone()[0]

Deducao_1 = con.execute('select DEDUCAO from INSS where INSS_ID = 1').fetchone()[0]
Deducao_2 = con.execute('select DEDUCAO from INSS where INSS_ID = 2').fetchone()[0]
Deducao_3 = con.execute('select DEDUCAO from INSS where INSS_ID = 3').fetchone()[0]
Deducao_4 = con.execute('select DEDUCAO from INSS where INSS_ID = 4').fetchone()[0]
Deducao_5 = con.execute('select DEDUCAO from INSS where INSS_ID = 5').fetchone()[0]

#IRPF
IRPF_Faixa_fim_2 = con.execute('select FAIXA_FIM from IRPF where IRPF_ID = 2').fetchone()[0]
IRPF_Faixa_fim_1 = con.execute('select FAIXA_FIM from IRPF where IRPF_ID = 1').fetchone()[0]
IRPF_Faixa_fim_3 = con.execute('select FAIXA_FIM from IRPF where IRPF_ID = 3').fetchone()[0]
IRPF_Faixa_fim_4 = con.execute('select FAIXA_FIM from IRPF where IRPF_ID = 4').fetchone()[0]
IRPF_Faixa_inicio_5 = con.execute('select FAIXA_FIM from IRPF where IRPF_ID = 5').fetchone()[0]

IRPF_Aliquota_1 = con.execute('select ALIQUOTA from IRPF where IRPF_ID = 1').fetchone()[0]
IRPF_Aliquota_2 = con.execute('select ALIQUOTA from IRPF where IRPF_ID = 2').fetchone()[0]
IRPF_Aliquota_3 = con.execute('select ALIQUOTA from IRPF where IRPF_ID = 3').fetchone()[0]
IRPF_Aliquota_4 = con.execute('select ALIQUOTA from IRPF where IRPF_ID = 4').fetchone()[0]
IRPF_Aliquota_5 = con.execute('select ALIQUOTA from IRPF where IRPF_ID = 5').fetchone()[0]

IRPF_Deducao_1 = con.execute('select DEDUCAO from IRPF where IRPF_ID = 1').fetchone()[0]
IRPF_Deducao_2 = con.execute('select DEDUCAO from IRPF where IRPF_ID = 2').fetchone()[0]
IRPF_Deducao_3 = con.execute('select DEDUCAO from IRPF where IRPF_ID = 3').fetchone()[0]
IRPF_Deducao_4 = con.execute('select DEDUCAO from IRPF where IRPF_ID = 4').fetchone()[0]
IRPF_Deducao_5 = con.execute('select DEDUCAO from IRPF where IRPF_ID = 5').fetchone()[0]

@app.route('/calcular', methods=['POST'])
def calcular():
    if request.method =="POST":
   
        salarioBruto = float(request.json['salarioBruto'])
        desconto = float(request.json['desconto'])
        dependente = float(request.json['dependente'])
        print(salarioBruto,desconto,dependente)

        def calculaINSS(salarioBruto):
            if (salarioBruto <= Faixa_fim_1):
                inss = salarioBruto * Aliquota_1 - Deducao_1
            elif(salarioBruto <= Faixa_fim_2):
                inss = salarioBruto * Aliquota_2 - Deducao_2
            elif(salarioBruto <= Faixa_fim_3):
                inss = salarioBruto * Aliquota_3 - Deducao_3
            elif(salarioBruto <= Faixa_fim_4):
                inss = salarioBruto * Aliquota_4 - Deducao_4
            elif(salarioBruto >= Faixa_inicio_5):
                inss = float(Deducao_5)
            return inss

        def calculaIRPF(salarioBruto,dependente,inss):    
            salario2 = float(salarioBruto - inss - (dependente * 189.59))
            if(salario2 <= IRPF_Faixa_fim_1):
                irpf = 0
            elif(salario2 <= IRPF_Faixa_fim_2):
                irpf = salario2 * IRPF_Aliquota_2 - IRPF_Deducao_3
            elif(salario2 <= IRPF_Faixa_fim_3):
                irpf = salario2 * IRPF_Aliquota_3 - IRPF_Deducao_3
            elif(salario2 <= IRPF_Faixa_fim_4):
                irpf = salario2 * IRPF_Aliquota_4 - IRPF_Deducao_4
            elif(salario2 >= IRPF_Faixa_inicio_5):
                irpf = float(IRPF_Deducao_5)
            return irpf

        inss = calculaINSS(salarioBruto)
        irpf = calculaIRPF(salarioBruto,dependente,inss)
        salarioLiquido = salarioBruto - (abs(inss) + abs(irpf)) - abs(desconto)

        irpf = round(abs(irpf), 2)
        inss = round(abs(inss), 2)
        salarioLiquido = round(salarioLiquido, 2)
        desconto = round(desconto, 2)
        rs = 'R$'

        #return render_template('index.html', salarioLiquido=salarioLiquido, inss=inss,irpf=irpf, desconto=desconto, rs=rs)
        return {
            'salarioBruto':"{:.2f}".format(salarioBruto),
            'inss':"{:.2f}".format(inss),
            'irpf':"{:.2f}".format(irpf),
            'desconto':"{:.2f}".format(desconto),
            'salarioLiquido':"{:.2f}".format(salarioLiquido),
        }

if __name__ == '__main__':
    app.run()