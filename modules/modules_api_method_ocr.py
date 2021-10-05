import base64
import binascii
import cv2
import numpy as np
from flask import Flask, request
from flask_restful import Resource, Api
# from modules.myconstants1 import path_resources
from ocr.new_method import scanImage

app = Flask(__name__)
api = Api(app)


class DocumentScanner(Resource):
    def post(self):
        data = request.get_json()
        retObj = ({
            "status": "success",
            "message": "All fields are mandatory"
        })

        try:
            document_name = data["doc_type"]
            face = data["face"]
            try:
                doc_image = base64.b64decode(data["front_image"])
                # doc_image = Image.open(io.BytesIO(doc_image))
                # im = doc_image.resize((200, 99), Image.ANTIALIAS)
                # im_path = path_resources + '/im.png'
                # im.save(im_path)
                # img_src = cv2.imread(im_path)
                # print('im_path=', im_path)
                # test_img = image.load_img(im_path, target_size=(200, 99))

                im_arr = np.fromstring(doc_image, dtype=np.uint8)
                img_src = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
            except binascii.Error:
                return {"status": "invalid",
                        "message": "Invalid base64 string"}

        except KeyError:
            return retObj

        scan_function = scanImage(document_name, face, img_src)
        json = ({"status": "success", "scanned_text": scan_function})
        return json


if __name__ == "__main__":
    app.run(debug=False)
