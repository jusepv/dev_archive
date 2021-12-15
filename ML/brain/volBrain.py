import numpy as np
import nibabel as nib

structure = nib.load(vol2_list[0]).get_fdata()
struct_vol = np.unique(structure, return_counts=True)
res_vol = struct_vol[0]