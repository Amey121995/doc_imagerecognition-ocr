from ocr.align_images import align_images
import numpy as np
import imutils
import cv2
from modules.myconstants import path_resources

def align_documents(image, template):
    # # load the input image and template from disk
    # print("[INFO] loading images...")
    # image = cv2.imread(args["image"])
    # template = cv2.imread(args["template"])
    # align the images
    print("[INFO] aligning images...")
    aligned_new = align_images(image, template)

    # resize both the aligned and template images so we can easily
    # visualize them on our screen
    aligned = imutils.resize(aligned_new, width=700)
    template = imutils.resize(template, width=700)
    # our first output visualization of the image alignment will be a
    # side-by-side comparison of the output aligned image and the
    # template
    stacked = np.hstack([aligned, template])

    # our second image alignment visualization will be *overlaying* the
    # aligned image on the template, that way we can obtain an idea of
    # how good our image alignment is
    overlay = template.copy()
    output = aligned.copy()
    cv2.addWeighted(overlay, 0.5, output, 0.5, 0, output)
    # show the two output image alignment visualizations
    cv2.imwrite(path_resources+"/OCR Image Alignment Stacked.png", stacked)
    cv2.imwrite(path_resources+"/OCR Image Alignment Overlay.png", output)
    cv2.waitKey(0)

    return aligned_new
