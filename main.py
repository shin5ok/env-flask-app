from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/dump')
def hello():
    import os
    foo = request.headers.get("x-foo")
    print("foo:", foo)
    return jsonify(dict(request.headers))

@app.route("/test")
def test():
    return "test"

@app.after_request
def add_header(response):
    response.headers['X-FOO'] = 'BAR'
    response.headers['X-Huga'] = 'hoge'
    return response

if __name__ == '__main__':
    app.run(debug=True)
