from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/dump')
def hello():
    import os
    return jsonify(dict(request.headers))

@app.after_request
def add_header(response):
    response.headers['X-FOO'] = 'BAR'
    response.headers['X-Huga'] = 'hoge'
    return response

if __name__ == '__main__':
    app.run(debug=True)
