from flask import Flask, render_template
import pandas as pd

# Cria uma aplicação Flask
app = Flask(__name__)

# Rota para a página inicial "/"
@app.route("/")
def index():
    # Lê a planilha diretamente do Google Planilha via CSV 
    tabela = pd.read_csv(
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vROVBEZA7XzTLax9RrjV0TT_3sCKCUaFg8C-lfZsqVpTymO2y-jbiV_WNz9ItnHC63y0AT2KoDkRJvw/pub?output=csv"
    )
    
    # Cria uma lista de dicionários contendo o id (posição+1) e o título de cada linha da planilha
    # Essa lista será usada para gerar a lista de materiais no template index.html
    dados = [
        {
            "id": n + 1,           # id para acesso via URL, começa em 1
            "titulo": tabela['título'][n]  # título do material na linha n
        }
        for n in range(len(tabela))  # percorre todas as linhas da tabela
    ]
    
    # Renderiza o template 'index.html' e envia a lista 'dados' para a página
    return render_template("index.html", paginas=dados)

# Rota para exibir a página de um material específico, com ID numérico
@app.route("/material/<int:pagina_id>")
def mostrar_pagina(pagina_id):
    # Lê novamente a planilha para garantir dados atualizados
    tabela = pd.read_csv(
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vROVBEZA7XzTLax9RrjV0TT_3sCKCUaFg8C-lfZsqVpTymO2y-jbiV_WNz9ItnHC63y0AT2KoDkRJvw/pub?output=csv"
    )
    
    # Converte o ID recebido na URL para índice da lista (começa em zero)
    n = pagina_id - 1
    
    # Verifica se o índice está dentro dos limites da tabela
    if 0 <= n < len(tabela):
        # Obtém as informações para passar ao template
        titulo = tabela['título'][n]
        imagem = tabela['img'][n]
        texto1 = tabela['texto1'][n]
        
        # Renderiza o template 'material.html' com os dados do material selecionado
        return render_template("material.html", titulo=titulo, imagem=imagem, texto1=texto1)
    else:
        # Se o ID for inválido, retorna uma mensagem de erro e status 404 (não encontrado)
        return "Calma lá amigo(a)!, você está querendo encontrar um material muito raro para a gente", 404

# Atualiza automaticamente o site
if __name__ == "__main__":
    app.run(debug=True)
