# render-slitscan
Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

## Requirements

##Usage
```
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

The full license text can be found [LICENSE.md](here).