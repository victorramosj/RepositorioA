from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return 'Essa é minha primeira aplicação em Flask!'

@app.route('/contato')
def contato():
  return render_template('contato.html')


if __name__ == '__main__':
    app.run()