import maya.mel

objs = maya.mel.eval("ls -sl")
print(objs)