from flask import Flask, jsonify,request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    return "<h1>This is flask application </h1>" \
           "<h2> I can run sucessfully </h1>"


if __name__ == "__main__":
    app.run()