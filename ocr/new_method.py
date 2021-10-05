import cv2
import json
import pytesseract
from collections import namedtuple
from modules.modules_myconstants import path, json_file_path
from ocr.align_images import align_images


def scanImage(document_name, face, img_src):
    text_dict = {}
    OCR_LOCATIONS = []
    OCRLocation = namedtuple("OCRLocation", ["id", "bbox", "filter_keywords"])
    
    with open(json_file_path, "r") as file:
        json_file = json.load(file)

    for doc in json_file:
        if doc["template_name"] == document_name + "_" + face:
            OCR_LOCATIONS_list = doc["OCR_LOCATIONS"]
            for key in OCR_LOCATIONS_list:
                print("key =", key)
                id = key["id"]
                bbox_instance = key["bbox"]
                bbox = (bbox_instance["x"], bbox_instance["y"], bbox_instance["w"], bbox_instance["h"])
                filter = key["filter"]
                ocr_instance = OCRLocation(id, bbox, filter)
                OCR_LOCATIONS.append(ocr_instance)

            template_image_endpoint = doc["template_image_name"]
            print("template_image_endpoint = ", template_image_endpoint)
            template_image = cv2.imread(f"{path}/ocr/template/" + template_image_endpoint)
            try:
                aligned = align_images(img_src, template_image)
            except Exception:
                print("exception in OCR new method : ", Exception)
                return {
                    "status":"fail",
                }

            for loc in OCR_LOCATIONS:
                (x, y, w, h) = loc.bbox
                roi = aligned[y:y + h, x:x + w]
                rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
                text = pytesseract.image_to_string(rgb, lang='ben+eng', config='--oem 3 --psm 6')
                str_text = str(text).strip()
                text_dict[loc.id] = str_text
                print(loc.id, " = ", text)
            print("text_dict = ", text_dict)
        else:
            print("template not found")

    return text_dict
