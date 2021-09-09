
import os 
import cv2
result_path = 'F:/a/vscode/result'
dist_path = 'F:/a/vscode/seg'
for img_name in os.listdir(result_path):
    img_path = os.path.join(result_path, img_name)
    img = cv2.imread(img_path)
    g  = img[:,:,1]
    ret, result = cv2.threshold(g, 127,255, cv2.THRESH_BINARY_INV)
    cv2.imwrite(os.path.join(dist_path,img_name), result)
