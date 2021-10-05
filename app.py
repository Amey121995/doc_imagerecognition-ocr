from flask import Flask, request
from flask_restful import Api
from modules.modules_api_method_ocr import DocumentScanner

app = Flask(__name__)
api = Api(app, prefix="/api/v1")


@app.route("/document_ocr", methods=["POST"])
def post():
    return DocumentScanner.post(request.json)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, threaded=False)
