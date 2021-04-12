# file name : registerConform.py
# pwd : /project_name/app/registerData/registerConform.py

from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

from app.module import forms

registerData = Blueprint('registerData', __name__, url_prefix='/register')

#@registerData.route('/', methods=['GET','POST'])
#def home():
#    return render_template('/registerData/layout.html')

@registerData.route('/', methods=['GET','POST'])
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        flash(f'{form.username.data} 님 가입 완료!', 'success')
        #return redirect(url_for('home'))
    return render_template('/registerData/register.html', form=form)