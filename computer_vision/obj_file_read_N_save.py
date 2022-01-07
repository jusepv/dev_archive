import pywavefront
import numpy as np
import shutil

obj_path = "./Scissor_test.obj"
scene = pywavefront.Wavefront(obj_path)

vertices_array = np.array(scene.vertices)
vertices_array = vertices_array[:, :3]
print(vertices_array.shape)
print(vertices_array[0])

vertices_array_mean = np.mean(vertices_array, axis=0)
print(vertices_array_mean)
vertices_array_moved = vertices_array - vertices_array_mean


print(vertices_array.shape)

filepath_read = "./Scissor_test.obj"
filepath_out = "./Scissor_test_mod.obj"
shutil.copyfile(filepath_read, filepath_out)


with open(filepath_out, 'w+') as writefile:
    with open(filepath_read, 'r') as ofile:
        v_start = 0
        for iii, line in enumerate(ofile) :
            # writefile.write(line)
            # if "mtllib" in line :
            #     save_point = iii
            
            if ("v" in line) and ("vt" not in line) and ("vn" not in line) and ("#" not in line) :
                # print(v_start)
                # print(line)
                a, b, c = vertices_array_moved[v_start][0], vertices_array_moved[v_start][1], vertices_array_moved[v_start][2]
                mod_line = "v {:.4f} {:.4f} {:.4f}\n".format(a,b,c)
                # print(mod_line)
                writefile.write(mod_line)
                v_start += 1
            else :
                # print(line)
                writefile.write(line)
ofile.close()
writefile.close()