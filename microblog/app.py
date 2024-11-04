#python -m venv venv
#.\venv\Scripts\activate


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/contato')
def contato():
  return render_template('contato.html', )

@app.route('/sobrenos')
def aobrenos():
  return render_template('sobrenos.html', )

@app.route('/loja')
def loja():
  return render_template('loja.html', )


if __name__ == '__main__':
    app.run()