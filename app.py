from flask import Flask, render_template, request
from decimal import Decimal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculadora.html', resultado="")

@app.route('/calcular', methods=['POST'])
def calcular():
    numero1 = Decimal(request.form['numero1'])
    numero2 = Decimal(request.form['numero2'])
    operacao = request.form['operacao']

    if operacao == 'IMC':
        resultado = numero1 / numero2 ** 2
        resultado = f'{resultado:.2f}'
        
        if float(resultado) >=25.00: 
             preobesidade = True
             str(preobesidade)
        else:
            preobesidade = False
            str(preobesidade)

        if float(resultado) >=30.00: 
             obesidade1 = True
             str(obesidade1)
        else:
            obesidade1 = False
            str(obesidade1)
        
        if float(resultado) >=35.00: 
             obesidade2 = True
             str(obesidade2)
        else:
            obesidade2 = False
            str(obesidade2)

        if float(resultado) <18.00: 
             desnutricao = True
             str(desnutricao)
        else:
            desnutricao = False
            str(desnutricao)

    if preobesidade and obesidade1 == True:
     preobesidade = False
    if obesidade1 and obesidade2 == True:
     obesidade1 = False;



    return render_template('calculadora.html', resultado=resultado, preobesidade=preobesidade, obesidade1 = obesidade1, obesidade2 = obesidade2, desnutricao = desnutricao)


if __name__ == '__main__':
    app.run(debug=True)