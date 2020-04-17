# -*- coding: utf-8 -*-
# Copyright 2020 Armin Bahl <arbahl@gmail.com>

import numpy as np
import nibabel as nib
from tifffile import imread
from pathlib import Path
import gzip
import shutil

root_path = Path(r"/Users/arminbahl/Desktop")

# For example, we map EM landmarks to z-brain landmarks
moving = "EM_overview"
reference = "z_brain"
dx_reference = 0.798
dy_reference = 0.798
dz_reference = 2

bigwarp_dfield = imread(str(root_path / f"{moving}_to_{reference}_bigwarp_dfield.tif"))

dfield_x = bigwarp_dfield[:, 0]
dfield_y = bigwarp_dfield[:, 1]
dfield_z = bigwarp_dfield[:, 2]

ants_dfield = np.array([[dfield_x, dfield_y, dfield_z]]).swapaxes(1, 2).swapaxes(2, 3).swapaxes(3, 4)
ants_dfield = ants_dfield.swapaxes(0, 1).swapaxes(1, 2).swapaxes(2, 3)
ants_dfield = ants_dfield.swapaxes(0, 1).swapaxes(1,2)
ants_dfield = ants_dfield.swapaxes(0, 1)

# float 32 is precise enough and makes the file much smaller
ants_dfield = ants_dfield.astype(np.float32)

# not really sure if ants actually really cares about the affine matrix, but this is what comes out after an ants-transform
ants_dfield = nib.Nifti1Image(ants_dfield, affine=[[-dx_reference,  0.,  0., -0.],
                                                   [0., -dy_reference,  0., -0.],
                                                   [0.,  0.,  dz_reference,  0.],
                                                   [0.,  0.,  0.,  1.]])

ants_dfield.header["srow_x"] = [0., 0., 0., 0.]
ants_dfield.header["srow_y"] = [0., 0., 0., 0.]
ants_dfield.header["srow_z"] = [0., 0., 0., 0.]
ants_dfield.header["pixdim"] = [1., dx_reference, dy_reference, dz_reference, 0., 0., 0., 0.]
ants_dfield.header["regular"] = b'r'
ants_dfield.header["intent_code"] = 1007
ants_dfield.header["qform_code"] = 1
ants_dfield.header["sform_code"] = 0
ants_dfield.header["xyzt_units"] = 2
ants_dfield.header["quatern_d"] = 1

# DO NOT USE .nii.gz. This renders the transform useless. Ants can work with .nii files as well.
# One should compress the nii files after, using gzip
nib.save(ants_dfield, str(root_path / f"{moving}_to_{reference}_ants_dfield.nii"))

# Compress the nii file
f_in = open(root_path / f"{moving}_to_{reference}_ants_dfield.nii", 'rb')
f_out = gzip.open(root_path / f"{moving}_to_{reference}_ants_dfield.nii.gz", 'wb')

shutil.copyfileobj(f_in, f_out)
f_in.close()
f_out.close()

# Remove the original nii file
(root_path / f"{moving}_to_{reference}_ants_dfield.nii").unlink()
