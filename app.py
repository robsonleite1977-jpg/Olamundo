# pip install flask

# → importa a ferramenta Flask para usar neste arquivo.
from flask import Flask

# → cria a "aplicação" (seu site).
app = Flask(__name__)

# → diz ao Flask: "quando alguém acessar a página principal (/), faça o que está abaixo".
@app.route("/")

# → define a função que será executada. O texto entre aspas é o que o navegador vai mostrar.
def ola_mundo():
    return "<h1>Olá, Mundo!</h1><p>Esta é minha primeira página em Python.</p>"

#  → diz: "se este arquivo for rodado diretamente, inicie o servidor".
if __name__ == "__main__":

    # → liga o site e o debug=True mostra erros detalhados enquanto você desenvolve.
    app.run(debug=True)