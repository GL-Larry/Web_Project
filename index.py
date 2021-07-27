from flask import Blueprint, render_template, jsonify

from irrelevant.myorm import Users

index = Blueprint('index', __name__)


@index.route('/index')
def turn_index():
    # result = Users().field("name,url").select()
    # print(type(result))
    return render_template('index.html')


@index.route('/recommend')
def recommend():
    result = Users().field("name,url").select()
    print(type(result))
    return jsonify(result)

# @index.route('/index')
# def turn_index():
#     return render_template('index.html')
