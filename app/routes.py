#app/routes.py
import json

from flask import Blueprint, jsonify, render_template, request

from .utils import query_llms  # , scrape_website

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/ask', methods=['POST'])
def ask():
    print("helloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
    user_prompt = request.json.get('prompt')
    response = query_llms(user_prompt)#here was await
    print("byeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    print(response)
    # data=response.__str__
    print(response)
    return jsonify(response)