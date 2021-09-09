
import random
import os
random.seed(2020)
mask_dir  = '/home/aistudio/work/seg/Train/masks'
img_dir = '/home/aistudio/work/seg/Train/fundus_image'
path_list = list()
for img in os.listdir(img_dir):
    img_path = os.path.join(img_dir,img)
    mask_path = os.path.join(mask_dir,img.replace('jpg', 'png'))
    path_list.append((img_path, mask_path))
random.shuffle(path_list)
ratio = 0.8
train_f = open('/home/aistudio/work/seg/Train/train.txt','w') 
val_f = open('/home/aistudio/work/seg/Train/val.txt' ,'w')

for i ,content in enumerate(path_list):
    img, mask = content
    text = img + ' ' + mask + '\n'
    if i < len(path_list) * ratio:
        train_f.write(text)
    else:
        val_f.write(text)
train_f.close()
val_f.close()


    
    
