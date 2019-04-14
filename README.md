# SIGBACK
This is a very simple python library to blend signature images with given
background images, it is heavily inspired in the code available
[here](http://www.gpds.ulpgc.es/) and uses the
blending process described in [1].

## Testing
To make sure all the available functions are working properly on your system
run all the test functions available with the `make` command.

## Modules
The library is composed of three modules, two for processing the signature
images and one for blending it with background images.
* [color module](##the-color-module)
* [transform module](##the-transform-module)
* [blend module](##the-blend-module)
* [measure module](##the-measure-module)

## The color module
the color module contains functions to binarize and remove the background of a
signature image with a whitish background. To binarize it uses posterization just
like describe in [1].

### binarize
<hr/>

`sigback.processing.color.binarize` (img, nl, method='postarization')

Binarizes an image.

<strong>Parameters</strong>

<strong>sig (M, N)ndarray</strong><br>
Grayscale image representing the signature. The pixel values must be between
0 and 1.

<strong>nl int</strong><br>
Posterization level used.

<strong>method str</strong><br>
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

`sigback.processing.color.remove_background`(img, nl=3, method='posterization')

Removes the background of a grayscale signature image. This method makes a call
to the binarize method described above.

<strong>Parameters</strong>

<strong>sig (M, N)ndarray</strong><br>
Grayscale image representing the signature. The pixel values must be between
0 and 1.

<strong>nl int</strong><br>
Posterization level used to threshold the image.

<strong>method str</strong><br>
Thresholding method to be used, so far only the 'posterization' option is
implemented.

<strong>Use example</strong>

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
that <strong>to this functions work correctly the signature image must have a
perfectly white background</strong>, this can be achieved by calling the
functions of the color module or making your own background removal functions.

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

Calculates the barycenter of an image with a white background.

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

signature_barycenter = transform.barycenter(signature)
```

## the blend module
The blend module contains functions to blend a signature image to a background
image and to blend all signatures from one directory into all backgrounds on
another directory.

### blend
<hr>

`sigback.blend.blend.blend`(sig, sig_barycenter, doc, doc_center)

Blends a signature image to a background image.

<strong>Parameters</strong><br>

<strong>sig (N, M)ndarray</strong><br>
Grayscale image with pixel values between 0 and 1 and whitish background.

<strong>sig_barycenter tuple</strong><br>
The barycenter of the signature image, if the barycenter is not known (and the
method described above cannot be used) it is possible to pass `(0, 0)`, with
this the signatures will be blent together, but the position of the signature
in the background will be the top left.

<strong>doc (N, M)ndarray</strong><br>
Grayscale image with pixel values between 0 and 1. This will be used as the
background of the blended image.

<strong>doc_center tuple</strong><br>
Center of the area reserved for the signature in the document. This is useful
if the background image is of a document, otherwise `(0, 0)` can be passed to
this parameter and the images will be blended ignoring the position of the
signature on the background.

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

### blend_dirs
<hr>

`sigback.blend.blend.blend_dirs`(sigs_dir, docs_dir, doc_centers, save_dir,
seed=None)

Blends all signatures from a directory with the backgrounds on another directory.

<strong>Parameters</strong>

<strong>sigs_dir str</strong><br>
The path to the directory containing all the signatures.

<strong>docs_dir str</strong><br>
The path to the directory containing all the documents (or any other kind of
background).

<strong>doc_centers list</strong><br>
List of tuples containing the centers of the documents, if the center is not
known `(0, 0)` can be passed. The list must be in the same order as the
documents would be if they were sorted alphabetically

<strong>save_dir str</strong><br>
The path to the directory in which the blended images will be saved.

<strong>seed int</strong><br>
Used to randomly shuffle the signatures, should be only used for testing or
reproducibility.

<strong>Use example</strong><br>
``` python
import os

from sigback.blend.blend import blend_dirs

cx = [
    1800, # 1,png
    2164, # 10.png
    2890, # 11.png
    2264, # 12.png
    2300, # 13.png
    2055, # 14.png
    2785, # 15.png
    2586, # 16.png
    1286, # 17.png
    1285, # 18.png
    2472, # 19.png
    2602, # 2.png
    699, # 20.png
    2067, # 3.png
    2713, # 4.png
    2077, # 5.png
    2638, # 6.png
    2287, # 7.png
    2195, # 8.png
    2071 # 9.png
]
cy = [
    1215, # 1.png
    836, # 10.png
    1189, # 11.png
    1140, # 12.png
    783, # 13.png
    1807, # 14.png
    1479, # 15.png
    452, # 16.png
    393, # 17.png
    376, # 18.png
    1877, # 19.png
    659, # 2.png
    683, # 20.png
    979, # 3.png
    1269, # 4.png
    834, # 5.png
    1087, # 6.png
    965, # 7.png
    767, # 8.png
    805 # 9.png
]

sigs_dir = '/home/heitor/data/ic/sigver/data/UTSig_Crop/'
docs_dir = '/home/heitor/data/ic/image-blender/checks/all_checks'
doc_centers = list(zip(cy, cx))
save_dir = '/home/heitor/data/ic/sigver/data/background_utsig/'

blend_dirs(sigs_dir, docs_dir, doc_centers, save_dir)
```

## the measure module
The measure module contains functions to measure properties of images, like
maximum and minimum size.

### minmax
<hr>

`sigback.processing.measure.minmax`(directory)

Gets the maximum and the minimum number of rows of the images in a given
directory.

<strong>Parameters</strong><br>

<strong>directory str</strong><br>
The path to the directory that contains the images. The directory must contain
only the images.

<strong>use example</strong>
```python
from skimage import img_as_float64

from sigback.processing import measure


directory = '/tmp/images'
result = measure.minmax(directory) # result = (150, 300, 100, 200)
```

## References
[1] Miguel A. Ferrer, Francisco Vargas, Aythami Morales, Aaron Ordo\F1ez,
"Robustness of Off-line Signature Verification based on Gray Level Features",
IEEE Transactions on Information Forensics and Security, vol. 7, no. 3, pp.
966-977, June 2012.