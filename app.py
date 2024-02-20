from flask import Flask, render_template, jsonify, request
import config
import openai
import aiapi
import json


def page_not_found(e):
    return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        prompt = request.form['prompt']

        res = {}

        res['answer'] = aiapi.generateChatResponse(prompt)

        return jsonify(res)

    return render_template('index.html', **locals())


@app.route('/expand', methods=['POST'])
def expand():
    if request.method == 'POST':
        prompt = request.form['prompt']

        res = {}

        res['answer'] = aiapi.generateExpandResponse(prompt)

        return jsonify(res)

    return render_template('index.html', **locals())


@app.route('/rg/', methods=['POST', 'GET'])
def rg():

    if request.method == 'POST':
        prompt = request.form['prompt']

        res = {}

        res['answer'] = aiapi.generateChatResponse(prompt)

        return jsonify(res)

    return render_template('rg.html', **locals())


@app.route('/ds/', methods=['POST', 'GET'])
def ds():

    if request.method == 'POST':
        prompt = request.form['prompt']

        res = {}

        res['answer'] = aiapi.generateChatResponse(prompt)

        return jsonify(res)

    return render_template('ds.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
