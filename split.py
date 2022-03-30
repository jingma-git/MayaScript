import os
import open3d as o3d
import shutil

dir = "D:\Dataset\ModelResource_RigNetv1_preproccessed"
outdir = "D:\Dataset\ModelsResource-RigNetv1-fbx"
A = []
B = []
for fname in os.listdir(os.path.join(dir, "obj")):
    if fname[len(fname)-4:] == ".obj":
        path = os.path.join(dir, "obj/{}".format(fname))
        obj = o3d.io.read_triangle_mesh(path)
        in_path = os.path.join(outdir, "fbx/{}.fbx".format(fname[:-4]))
        if len(obj.vertices) > 1000:
            a_path = os.path.join(outdir, "A/{}.fbx".format(fname[:-4]))
            shutil.copy(in_path, a_path)
            A.append(a_path)
        else:
            print(fname)
            b_path = os.path.join(outdir, "B/{}.fbx".format(fname[:-4]))
            shutil.copy(in_path, b_path)
            B.append(b_path)

print("A={}, B={}".format(len(A), len(B))) # A=1155, B=1548