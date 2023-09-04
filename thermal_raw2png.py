import cv2 as cv
import numpy as np
import os

test 

base_path = "/home/ali/Desktop/haziran_termal_calb/raw_topng/test1"
save_path = "/home/ali/Desktop/haziran_termal_calb/raw_topng/png/"
folder_list = os.listdir(base_path)  # 1, 1-panorama, 2, 2-panorama
rows, cols = (480, 640)
for folder in folder_list:
    folder_path = os.path.join(base_path, folder)
    if os.path.isdir(os.path.join(folder, folder_path)):
        for filename in os.listdir(folder_path):
            with open(os.path.join(folder_path, filename), 'rb') as f:
                img_16_bit = np.fromfile(f, dtype=np.uint16, count=rows*cols).reshape((rows, cols))
            img_8_bit = np.uint8((img_16_bit-img_16_bit.min()) / (img_16_bit.max()-img_16_bit.min()) * 255)
            clahe_applier = cv.createCLAHE(2, tileGridSize=(2, 2))
            img = clahe_applier.apply(img_8_bit)
            if not os.path.exists(save_path + folder):
                os.makedirs(save_path + folder)
            cv.imwrite(f"{save_path}/{folder}/{filename}.png", img)
        
