from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)   #sudo fuser -k xxxx/tcp

filmes = [
    {"titulo": "Shrek", "ano": "2001", "nota": "5,0", "id": "0" },
    {"titulo": "Duna", "ano": "2021", "nota": "4,1", "id": "1" },
    {"titulo": "Free Guy", "ano": "2021", "nota": "4,5", "id": "2" },
    {"titulo": "Jungle Cruise", "ano": "2021", "nota": "3,8", "id": "3" },
    {"titulo": "O Grande Gatsby", "ano": "2013", "nota": "4,3", "id": "4" },
]

@app.route('/')
def index():
    return render_template("index.html", filmes=filmes)

@app.route('/adicionar')
def adicionar():
    return render_template("adicionar.html")

@app.route('/salvar', methods=['POST'])
def save():
    titulo = request.form['titulo']
    ano = request.form['ano']
    nota = request.form['nota']
    id = request.form['id']
    if titulo == '' or ano == '' or nota == '' or id == '':
        return render_template('erro.html')
    elif id.isnumeric():
        filme = { "titulo": titulo, "ano": ano, "nota": nota, "id": id}
        filmes.append(filme)
        return redirect('https://5000-rose-horse-b26oq6qa.ws-us17.gitpod.io/')
    else:
        return render_template('erro.html')
    #return render_template("index.html", lista=filmes)

@app.route('/deletar', methods=['POST'])
def deletar():
    id = request.form['id']
    if id == '':
        return redirect('https://5000-rose-horse-b26oq6qa.ws-us17.gitpod.io/')
    if id.isnumeric():
        for i in filmes:
            if int(id) == int(i['id']):
                filmes.pop(int(id))
                break
        else:
            return render_template("erro.html")
    else:
        return render_template("erro.html")
    return redirect('https://5000-rose-horse-b26oq6qa.ws-us17.gitpod.io/')
    #return render_template("index.html", lista=filmes)

@app.route('/pesquisar', methods=['POST'])
def pesquisar():
    filmes_pesquisa=[]
    pesquisa = request.form['pesquisa']
    if pesquisa > '':
        for filme in filmes:
            if pesquisa.lower() in filme['titulo'].lower() or pesquisa == filme['ano']:
                filmes_pesquisa.append(filme)
        return render_template("pesquisar.html", filmes_pesquisa=filmes_pesquisa)
    else:
        return render_template("erro.html")



app.run(debug=True)
