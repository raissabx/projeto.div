from flask import Flask
from flask import render_template
from flask import url_for, redirect
from flask import request
import pandas as pd


app = Flask(__name__)

serie = pd.read_csv('produtosCarrinho.csv', header=None, names=['produtos', 'valores'])
serie = serie.set_index('produtos')
serie = serie['valores']
print(serie)

carrinho = {}

@app.route('/')
def carrinhoDeCompras():
    return 'Carrinho de Compras'

'''@app.route('/compras/<produto>/<qtd>')
def compras(produto, qtd):
    carrinho[produto] = int(qtd)
    return 'Produto Adicionado ao Carrinho' '''

@app.route('/excluir/<produto>')
def excluir(produto):
    serie = serie.drop([produto])
    return 'Item excluído do carrinho'


@app.route('/listar')
def listar():
    return serie.to_dict()
    #return carrinho
    
@app.route('/comprar')
def comprar():
    argumentos = request.args.to_dict()
    qtd = argumentos['qtd']
    nome = argumentos['produto']
    serie[nome] = qtd
    serie.to_csv('produtosCarrinho.csv', header=False)
    print()
    return argumentos

if __name__ == "__main__":
    app.run(debug=True)