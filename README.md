# render-slitscan
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa] [![status: hibernate](https://github.com/GIScience/badges/raw/master/status/hibernate.svg)](https://github.com/GIScience/badges#hibernate)

A python script to generate a [slit-scan](https://en.wikipedia.org/wiki/Slit-scan_photography) animation from a PNG sequence.

## Usage
```python
>>> python3 SLITSCAN.py -h
usage: SLITSCAN.py [-h] [-r] [-o .] input_dir width height

positional arguments:
  input_dir             input folder
  width                 Width of the resulting image.
  height                Height of each slice

options:
  -h, --help            show this help message and exit
  -r, --reverse
  -o ., --output-dir .  Optional output directory
```

- `input` is the path to the folder containing the PNG sequence
- `width` will be the width of the finished image. Normally this is the same as all your source image's width
- `height` is the height of each slice. The lower this value is, the better the "resolution" of the finished image will be.
- `reverse` will reverse the building direction of the image
- `output-dir` is used to set a different output path than the project folder
Example: `python3 SLITSCAN.py -h`

## Notes
- This app only supports PNG-images as input. Therefore it should be at the very end of your post-processing workflow.

## Roadmap
- Different orders (left-to-right, right-to-left, top-to-bottom, bottom-to-top)
- example scenes for common render engines

## License
This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg