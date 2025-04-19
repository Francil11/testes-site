from flask import Flask, render_template, request, redirect, url_for
from gerar_imagem import gerar_imagem_promocional
import os
import uuid
import csv

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/imagens'

@app.route("/", methods=["GET", "POST"])
def index():
    imagens = []
    if request.method == "POST":
        if 'csv_file' in request.files:
            file = request.files['csv_file']
            if file.filename.endswith('.csv'):
                rows = csv.DictReader(file.read().decode('utf-8').splitlines())
                for row in rows:
                    link = row.get("link")
                    titulo = row.get("titulo")
                    chamada = row.get("chamada")
                    nome_arquivo = f"{uuid.uuid4().hex}.jpg"
                    caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)
                    gerar_imagem_promocional(link, titulo, chamada, caminho_imagem)
                    imagens.append(nome_arquivo)
        else:
            link = request.form.get("link")
            titulo = request.form.get("titulo")
            chamada = request.form.get("chamada")
            nome_arquivo = f"{uuid.uuid4().hex}.jpg"
            caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)
            gerar_imagem_promocional(link, titulo, chamada, caminho_imagem)
            imagens.append(nome_arquivo)

        return render_template("resultado.html", imagens=imagens)

    return render_template("index.html")

@app.route("/politica-de-privacidade")
def politica():
    return render_template("politica.html")

if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
