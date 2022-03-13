import maya.cmds as cmds
import maya.OpenMaya as om


def getDagPath(name):
    """
    Args:
      name (str)

    Returns:
      MDagPath
    """
    selList = om.MSelectionList()
    selList.add (name)
    dagPath = om.MDagPath()
    selList.getDagPath(0, dagPath)
    return dagPath

def num_vertices():
    mesh = cmds.ls(sl=True)[0]
    dagPath = getDagPath(mesh)
    meshFn = om.MFnMesh(dagPath)
    print(mesh, meshFn.numVertices())


num_vertices()