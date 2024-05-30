from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class AtivoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    anv_PRJ = StringField('Projeto', validators=[DataRequired()])
    descricao = StringField('Descrição', validators=[DataRequired()])
    etiqueta = StringField('Etiqueta', validators=[DataRequired()])
    imageURL = StringField('URL da Imagem', validators=[DataRequired(), URL()])
    local = StringField('Local', validators=[DataRequired()])
    numero_ativo = StringField('Número do Ativo')
    subclasse = StringField('Subclasse', validators=[DataRequired()])
    sublocalizacao = StringField('Sublocalização', validators=[DataRequired()])
    submit = SubmitField('Enviar')
