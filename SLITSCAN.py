import cv2
import os
import time
import glob

user_x_res = int(input("Desired width in px: "))
user_y_res = int(input("How tall should each slice be? In px: "))

input_dir = "./0_RENDER_FILES/"
output_dir = "./1_CROPPED_FILES/"

"""
def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=dir_path)
args = parser.parse_args()
"""

if __name__ == '__main__':
    # GETTING FILES
    files = sorted(glob.glob(f"{input_dir}*.png"), reverse=False)
    #print(f"found {len(files)} PNG images. Any other files were ignored.")

    #CROP
    start = time.perf_counter()
    cropped = []
    for filename in filter(lambda f: f.lower().endswith(('.jpg', '.jpeg', '.png')), os.listdir(input_dir)):
        path = input_dir+filename
        img = cv2.imread(path)
        crop_img = img[0:user_y_res, 0:user_x_res] #y:y+d; x:x+d
        cropped.append(crop_img)
        im_v = cv2.vconcat(cropped)
        cv2.imwrite('./output2.png', im_v)
    end = time.perf_counter()
    print(f"Operation took: {round(end - start, 5)}s")