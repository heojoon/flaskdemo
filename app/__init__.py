# file name : __init__.py
# pwd : /project_name/app/__init__.py
 
from flask import Flask
from flask import Blueprint, request, render_template, flash, redirect, url_for

# 추가할 모듈이 있다면 추가

app = Flask(__name__)
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'

# 파일 이름이 index.py이므로
from app.main.index import main as main
from app.test.test import test as test
from app.registerData.registerConform import registerData as registerData

# 위에서 추가한 파일을 연동해주는 역할
app.register_blueprint(main)
app.register_blueprint(test)
app.register_blueprint(registerData)

# 시작 페이지
@app.route('/')
def home():
    return redirect('/main')