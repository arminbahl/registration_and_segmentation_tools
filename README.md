# Registration and segmentation tools
Some important pieces of code needed for volumetric registrations and planer cell segmentation.

## Registration tools
### Converting manual landmarks into an ANTs transformation file
What you'll need is a functional installation of [ANTs](http://stnava.github.io/ANTs/), [Fiji's Bigwarp](https://imagej.net/BigWarp), and [Python](https://www.anaconda.com/distribution/).

1. Create a list of manual landmarks for the reference and moving stack with BigWarp. It does not matter which stack is reference and which one is moving.
2. Save this list as a csv file from BigWarp. Naming can be like this: <em>bigwarp_landmarks_\<moving\>_to_\<reference\>.csv</em>.
3. Use the script <em>invert_bigwarp_landmarks.py</em> to switch landmarks between moving and reference. Naming of the output can be like this <em>bigwarp_landmarks_\<moving\>to_\<moving\>.csv</em>.
4. Use BigWarp to load reference and moving stacks and the landmark points export the Warp field. You can (should?) ignore the affine part.
5. Save the result as a tiff stack as <em>\<moving\>_to_\<reference\>_bigwarp_dfield.tif</em>.
6. Use the script <em>convert_bigwarp_dfield_to_ants_dfield.py</em>.
7. Repeat steps 3 to 6, but for reference and moving stack switched, so you get the inverse transforms.

You should end up with two ANTs transformation matrices that can now be used to transform any stack and point lists from the moving to the reference coordinate system or the other way around.

## Segmentation tools

TODO, but check out [CaImAn](https://github.com/flatironinstitute/CaImAn) for segmentation of cells based on functional properties and [cellpose](http://www.cellpose.org/static/docs/index.html) for segmentation of cells based on structure.






