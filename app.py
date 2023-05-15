from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
<<<<<<< HEAD
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/sobre")
def about():
    return render_template('about.html')

@app.route("/experiencia")
def experience():
    return render_template('experience.html')

@app.route("/formacao")
def training():
    return render_template('training.html')

@app.route("/contato")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run()
=======

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
>>>>>>> 2cc089f (Upload da lista 4 pweb)
