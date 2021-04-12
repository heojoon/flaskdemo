# file name : index.py
# pwd : /project_name/app/main/index.py

from flask import Blueprint, request, render_template, flash, redirect, url_for
from datetime import date
from flask import current_app as app


main= Blueprint('main', __name__, url_prefix='/')
 
@main.route('/main', methods=['GET'])

def index():
    testData = date.today()
    return render_template('/main/index.html', testDataHtml=testData)