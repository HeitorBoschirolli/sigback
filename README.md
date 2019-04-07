# SIGBACK
This is a very simple python library to blend signature images with given
background images, it is heavly inspired in the code available
[here](lskdjfalj) and uses the blending process described in [1].

## Testing
To make sure all the available functions are working properly on your system
run all the test functions available with the `make` command.

## Modules
The library is composed of three modules, two for processing the signature
images and one for blending it with background images.
* [color module](###the-color-module)
* [transform module](###the-transform-module)
* [blend module](###the-blend-module)

## The color module
the color module contains functions to binarize and remove the background of a
signature image with white background. To binarize it uses posterization just
like describe in [1] and to remove the background it just convert the white
pixels in a binary image to white in the original image. It is important to
notice that the background removal function uses the binarizing function.

### binarize
<hr/>

`sigback.processing.color.binarize` (img, nl, method='postarization')

Binarizes an image

<strong>Parameters</strong>

<strong>sig (M, N)ndarray</strong><br>
Grayscale image representing the signature. The pixel values must be between
0 and 1.

<strong>nl int</strong><br>
Posterization level used to threshold the image.

<strong>method</strong><br>
Thresholding method to be used, so far only the 'posterization' option is
implemented.

<strong>example</strong><br>
``` python
from skimage.io import imread
from skimage import img_as_float64

from sigback.processing import color


signature = imread('some_signature.png', as_gray=True)
signature = img_as_float64(signature)

bin_signature = color.binarize(signature)
```

### remove_background
<hr>

`sigback.processing.color.remove_background`()

Removes the background of a grayscale signature image. This method makes a call
to the binarize method described above.

<strong>Parameters</strong>

<strong>sig (M, N)ndarray</strong><br>
Grayscale image representing the signature. The pixel values must be between
0 and 1.

<strong>nl int</strong><br>
Posterization level used to threshold the image.

<strong>method</strong><br>
Thresholding method to be used, so far only the 'posterization' option is
implemented.

<strong>Example</strong>

``` python
from skimage.io import imread
from skimage import img_as_float64

from sigback.processing import color


signature = imread('some_signature.png', as_gray=True)
signature = img_as_float64(signature)

no_bg_signature = color.remove_background(signature)
```

## The transform module
The transform module contains functions to remove the borders of a signature
image and to calculate the barycenter of a signature. It is important to notice
that <strong>to this functions work correctly the signature image must have no
background</strong>, this can be achieved by calling the functions of the color
module or making your own background removal functions.

### remove_border
<hr>

`sigback.processing.transform.remove_border`(img)

Removes the border of an image with white background.

<strong>Parameters</strong><br>

<strong>img (N, M)ndarray</strong><br>
Grayscale image with pixel values between 0 and 1.


<strong>use example</strong>
``` python
from skimage.io import imread
from skimage import img_as_float64

from sigback.processing import transform  


signature = imread('other_signature.png', as_gray=True)
signature = img_as_float64(sisgnature)

no_border_signature = transform.remove_border(signature)
```

### barycenter
<hr>

`sigback.processing.transform.barycenter`(img)

Calculates the barycenter of an image with white background.

<strong>Parameters</strong><br>

<strong>img (N, M)ndarray</strong><br>
Grayscale image with pixel values between 0 and 1

<strong>use example</strong>
``` python
from skimage.io import imread
from skimage import img_as_float64

from sigback.processing import transform  


signature = imread('other_signature.png', as_gray=True)
signature = img_as_float64(sisgnature)

signature_barycenter = transform.barycenter(signature)
```

## the blend module
The blend module contains functions to blend an signature image to a background
image and to blend all signature from one directory to all background on other
directory.

To blend a signature image to a background image the function requires the
signature barycenter (that can be calculated with the functions described
above) and the background's signing area's center, the latter is done because
the background files are originally documents with a signing area, passing
`(0, 0)` to both this values will allow the function to perform the blending
ignoring the position of the signature in the background.

### barycenter
<hr>

`sigback.blend.blend.blend`(img)

Blends a signature image to a background image.

<strong>Parameters</strong><br>

<strong>img (N, M)ndarray</strong><br>
Grayscale image with pixel values between 0 and 1

<strong>use example</strong>
``` python
from skimage.io import imread
from skimage import img_as_float64

from sigback.blend import blend


background = imread('background.png', as_gray=True)
background = img_as_float64(background)

signature = imread('third_signature.png', as_gray=True)
signature = img_as_float64(signature)

blended = blend.blend(sig, (200, 100), background, (800, 900))
blended_no_placement = blend.blend(sig, (0, 0), background, (0, 0))
```


``` python
from skimage.io import imread
from skimage import img_as_float64

from sigback.blend import blend


signatures_dir = './signatures/'
backgrounds_dir = './backgrounds/'
background_centers = [(1215, 1800), (659, 2602)]

blend.blend_dirs(
    signatures_dir,
    backgrounds_dir,
    background_centers, # passing [(0, 0), (0, 0)] is also an option
    './result/',
    1
)
```