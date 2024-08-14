import os
from flask import Flask, request

from api.generate import generate

app = Flask(__name__)

@app.route('/')
def index():
    return "Final Phrase"

@app.route('/create_role', methods=['post', 'get'])
def create_role():
    role_name = request.values.get('role_name')
    generate()
    return role_name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8005)
