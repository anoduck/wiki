```text
#   ___                    ______     __
#  / _ \ _ __   ___ _ __  / ___\ \   / /
# | | | | '_ \ / _ \ '_ \| |    \ \ / /
# | |_| | |_) |  __/ | | | |___  \ V /
#  \___/| .__/ \___|_| |_|\____|  \_/
#       |_|
#
```

## OpenCV

OpenCV is a python library comprised of several hundred algorithms dealing with computational vision and
artificial intelligence. Computational vision is a fancy way of saying photos, video, and informational
visiualizations, but it is important to remember it encapsulates more than that. Computatational vision is how
an electronic device can see, visualize, manipulate, and comprehend visual data.

(Thought I had written more on this)

### Working with image coordinates
> And not having too much fun with it.

Image coordinates are four values that represent the corners of a box that specifies our region of interest. The values are x, y, H, and W. They are represented as `[y:y+H, x:x+W]` or `(x, y, H, W)`. An example of such a value is `[0:860, 1400:400]`.

The matrix is: `[Linear Values, Horizontal Values]`

So, since we want to remove 500 pixels from all corners, and the image dimensions are 2592x4608. That would make our ROI: `(500, 500, 1592, 3609)`
