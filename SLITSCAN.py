#!/usr/bin/env python3
import cv2
import time
import glob
import plac
from pathlib import Path

@plac.pos("width", "Width of the resulting image.", type=int)
@plac.pos("height", "Height of each slice", type=int)
@plac.pos("input_dir", "input folder", type=Path)
@plac.flg("reverse")
@plac.opt("output_dir", "Optional output directory", type=Path)
def main(input_dir, width, height, reverse, output_dir="."):
    files = sorted(glob.glob(f"{input_dir}/*.png"), reverse=reverse)
    print(f"found {len(files)} PNG images.")

    start = time.perf_counter()
    cropped = []
    for filename in files:
        img = cv2.imread(filename)
        crop_img = img[0:height, 0:width] #y:y+d; x:x+d
        cropped.append(crop_img)
        im_v = cv2.vconcat(cropped)
        cv2.imwrite(f"{output_dir}/SLITSCAN.png", im_v)
    end = time.perf_counter()
    print(f"Operation took: {round(end - start, 5)}s")

if __name__ == '__main__':
    plac.call(main)