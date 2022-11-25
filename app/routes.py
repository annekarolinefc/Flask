from app import app 
from flask import render_template

#rota inicial 
@app.route('/')
@app.route('/index')
def index():
    dados = {"profissao": "Estudante", "linguagem": "Python"}
    return render_template('index.html', nome="Anne", dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')
    
@app.route('/teste')
def indexteste():
    nome = "Anne"
    return """
    <html>
        <head>
            <title>Página Inicial</title>
        </head>
        <body>
            <h2>Hello """+nome+"""</h2>
        </body>
    </html>
"""
