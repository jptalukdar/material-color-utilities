# /**
#  * @license
#  * Copyright 2021 Google LLC
#  *
#  * Licensed under the Apache License, Version 2.0 (the "License");
#  * you may not use this file except in compliance with the License.
#  * You may obtain a copy of the License at
#  *
#  *      http://www.apache.org/licenses/LICENSE-2.0
#  *
#  * Unless required by applicable law or agreed to in writing, software
#  * distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.
#  */

from quantize.quantizer_wsmeans import *
from quantize.quantizer_wu import *

# /**
#  * An image quantizer that improves on the quality of a standard K-Means
#  * algorithm by setting the K-Means initial state to the output of a Wu
#  * quantizer, instead of random centroids. Improves on speed by several
#  * optimizations, as implemented in Wsmeans, or Weighted Square Means, K-Means
#  * with those optimizations.
#  *
#  * This algorithm was designed by M. Emre Celebi, and was found in their 2011
#  * paper, Improving the Performance of K-Means for Color Quantization.
#  * https://arxiv.org/abs/1101.0395
#  */
# // libmonet is designed to have a consistent API across platforms
# // and modular components that can be moved around easily. Using a class as a
# // namespace facilitates this.
# //
# // tslint:disable-next-line:class-as-namespace
class QuantizerCelebi:
    # /**
    #  * @param pixels Colors in ARGB format.
    #  * @param maxColors The number of colors to divide the image into. A lower
    #  *     number of colors may be returned.
    #  * @return Map with keys of colors in ARGB format, and values of number of
    #  *     pixels in the original image that correspond to the color in the
    #  *     quantized image.
    #  */
    @staticmethod
    def quantize(pixels, maxColors):
        wu = QuantizerWu()
        wuResult = wu.quantize(pixels, maxColors)
        return QuantizerWsmeans.quantize(pixels, wuResult, maxColors)