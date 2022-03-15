import cv2
import os
import time

user_x_res = int(input("Desired width in px: "))
user_y_res = int(input("How tall should each slice be? In px: "))

def execution_time(start, end, function):
    print(function + " took: " + str(end - start) + "s")

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

def CROP(path_to_img, filename):
    img = cv2.imread(path_to_img)
    export_path = ("./1_CROPPED_FILES/")
    crop_img = img[0:user_y_res, 0:user_x_res] #y:y+d; x:x+d
    cv2.imwrite(export_path + "/" + filename+"_cropped.png", crop_img)

def MERGE():
    files = load_images_from_folder("./1_CROPPED_FILES/")
    files = files[::-1]
    im_v = cv2.vconcat(files)
    cv2.imwrite('./output.png', im_v)

if __name__ == '__main__':
    # COUTING FILES
    start = time.time()
    i = 0
    for filename in os.listdir("./0_RENDER_FILES"):
        i = i + 1
    end = time.time()
    print("found " + str(i) + " files in " + str(end - start) + "s")

    #CROP
    start = time.time()
    for filename in os.listdir("./0_RENDER_FILES"):
        CROP("./0_RENDER_FILES/"+filename,filename)
    end = time.time()
    execution_time(start,end,"CROP")

    #MERGE
    start = time.time()
    MERGE()
    end = time.time()
    execution_time(start,end,"MERGE")

    #CLEANUP
    start = time.time()
    for f in os.listdir("./1_CROPPED_FILES/"):
        os.remove(os.path.join("./1_CROPPED_FILES/", f))
    end = time.time()
    execution_time(start,end,"CLEANUP")
