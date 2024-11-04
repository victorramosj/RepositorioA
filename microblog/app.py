#python -m venv venv
#.\venv\Scripts\activate


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/contato')
def contato():
  return render_template('contato.html', tel='(87) 99898-9898')


if __name__ == '__main__':
    app.run()