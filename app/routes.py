from flask import Blueprint, render_template, request, redirect, url_for
import requests
from .forms import AtivoForm
from config import Config

bp = Blueprint('main', __name__, template_folder='../templates')


@bp.route('/')
def home():
    return render_template('home.html')


@bp.route('/ativos_cadastrados')
def ativos_cadastrados():
    response = requests.get(Config.FIREBASE_URL)
    ativos = response.json()
    return render_template('ativos.html', ativos=ativos)


@bp.route('/insert', methods=['GET', 'POST'])
def insert():
    form = AtivoForm()
    if form.validate_on_submit():
        novo_ativo = {
            "nome": form.nome.data,
            "anv_PRJ": form.anv_PRJ.data,
            "descricao": form.descricao.data,
            "etiqueta": form.etiqueta.data,
            "imageURL": form.imageURL.data,
            "local": form.local.data,
            "numero_ativo": form.numero_ativo.data,
            "subclasse": form.subclasse.data,
            "sublocalizacao": form.sublocalizacao.data
        }
        response = requests.post(Config.FIREBASE_URL.replace('.json', ''), json=novo_ativo)
        return redirect(url_for('main.ativos_cadastrados'))
    return render_template('insert.html', form=form)


@bp.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    form = AtivoForm()
    if request.method == 'GET':
        response = requests.get(f"{Config.FIREBASE_URL.replace('.json', '')}/{id}.json")
        ativo = response.json()
        form.nome.data = ativo.get('nome')
        form.anv_PRJ.data = ativo.get('anv_PRJ')
        form.descricao.data = ativo.get('descricao')
        form.etiqueta.data = ativo.get('etiqueta')
        form.imageURL.data = ativo.get('imageURL')
        form.local.data = ativo.get('local')
        form.numero_ativo.data = ativo.get('numero_ativo')
        form.subclasse.data = ativo.get('subclasse')
        form.sublocalizacao.data = ativo.get('sublocalizacao')
    elif form.validate_on_submit():
        ativo_atualizado = {
            "nome": form.nome.data,
            "anv_PRJ": form.anv_PRJ.data,
            "descricao": form.descricao.data,
            "etiqueta": form.etiqueta.data,
            "imageURL": form.imageURL.data,
            "local": form.local.data,
            "numero_ativo": form.numero_ativo.data,
            "subclasse": form.subclasse.data,
            "sublocalizacao": form.sublocalizacao.data
        }
        requests.put(f"{Config.FIREBASE_URL.replace('.json', '')}/{id}.json", json=ativo_atualizado)
        return redirect(url_for('main.ativos_cadastrados'))
    return render_template('insert.html', form=form)


@bp.route('/delete/<id>', methods=['POST'])
def delete(id):
    requests.delete(f"{Config.FIREBASE_URL.replace('.json', '')}/{id}.json")
    return redirect(url_for('main.ativos_cadastrados'))
