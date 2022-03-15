# render-slitscan

### Notes
1. This app only supports PNG-images as input. Therefore it should be at the very end of your post-processing workflow.
2. Normally, the file will be built from the bottom. This means, that frames early in the animation will be part of the lower image, while the later frames will result in the top of the output image. To reverse this use the `--invert` flag
