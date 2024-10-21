from flask import Flask
app = Flask(__name__)

@app.route('/contato')
def index():
    return "email@mail.com"

@app.route('/')
def contato():
    
    return 'Olá mundo!'

if __name__ == '__main__':
    app.run()