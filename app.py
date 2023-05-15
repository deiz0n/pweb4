from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template("paginas/index.html")

@app.route('/carrinho')
def carinho():
    return render_template("paginas/carrinho.html", item="Carrinho vazio")

@app.route('/carrinho/<item>')
def carinhoItem(item):
    return render_template("paginas/carrinho.html", item=item)

@app.route('/sobre')
def sobre():
    return render_template('paginas/sobre.html')

@app.route('/contato')
def contato():
    return render_template('paginas/contato.html')

if __name__ == '__main__':
    app.run(port=5055, debug=True)

