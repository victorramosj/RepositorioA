#ython -m venv venvp
#.\venv\Scripts\activate


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/contato')
def contato():
  return render_template('contato.html', tel='(81) 98888-0000')

@app.route('/sobrenos')
def aobrenos():
  return render_template('sobrenos.html' )

@app.route('/loja')
def loja():
  return render_template('loja.html', )
@app.route('/usuario')
@app.route('/usuario/<nome>')
def usuario(nome="usuario comum"):
    return  "olá "+ nome + "!"

@app.route('/operacoes', methods=['GET', 'POST'])
def operacoes():
    resultado = None

    if request.method == 'POST':
        # Pegando os números e a operação escolhida do formulário
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])
        operacao = request.form['operacao']
        
        # Realizando a operação com base na escolha
        if operacao == 'soma':
            resultado = f'{n1} + {n2} = {n1 + n2}'
        elif operacao == 'subtracao':
            resultado = f'{n1} - {n2} = {n1 - n2}'
        elif operacao == 'multiplicacao':
            resultado = f'{n1} * {n2} = {n1 * n2}'
        elif operacao == 'divisao':
            # Verificando se o divisor é 0 para evitar erro de divisão por zero
            if n2 != 0:
                resultado = f'{n1} / {n2} = {n1 / n2}'
            else:
                resultado = 'Erro: Divisão por zero!'
    
    return render_template('operacoes.html', resultado=resultado)


if __name__ == '__main__':
    app.run()