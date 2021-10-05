from alignment.align_images import align_images
import numpy as np
import imutils
import cv2

 
image = cv2.imread(r"E:\document_ocr\ocr_images\frontside1.jpg")
template = cv2.imread(r"E:\document_ocr\templatefront1.jpg")

print("[INFO] aligning images...")
aligned = align_images(image, template, debug=True)
aligned = imutils.resize(aligned, width=700)
template = imutils.resize(template, width=700)

stacked = np.hstack([aligned, template])

overlay = template.copy()
output = aligned.copy()
cv2.addWeighted(overlay, 0.5, output, 0.5, 0, output)

cv2.imshow("Image Alignment Stacked", stacked)
cv2.imshow("Image Alignment Overlay", output)
cv2.waitKey(0)


