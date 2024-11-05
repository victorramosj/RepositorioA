#python -m venv venv
#.\venv\Scripts\activate


from flask import Flask, render_template

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

@app.route('/operacoes')
@app.route('/operacoes/<int:n1>/<int:n2>')
def somar(n1 = 0, n2 = 1):
  resultadosoma = n1 + n2
  resultadosub = n1 - n2
  resultadomult = n1 * n2
  resultadodiv = n1 / n2
  return render_template('operacoes.html', n1=n1, n2=n2, resultadosoma=resultadosoma, resultadosub=resultadosub, resultadomult=resultadomult, resultadodiv=resultadodiv)




if __name__ == '__main__':
    app.run()