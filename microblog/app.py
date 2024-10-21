from flask import Flask
app = Flask(__name__)
@app.route('/')
def contato():
    return "email@mail.com"
@app.route('/')
def index():
    return 'Olá mundo!'



if __name__ == '__main__':
    app.run()