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

def getModelFromSelection():
    """"""
    try:
        sel = cmds.ls(sl=1, ap=1)
        if len(sel) < 2:
            om.MGlobal.displayError("Please select joints first, then mesh.")
            return
        else:
            mesh = sel.pop()
            dagPath1 = getDagPath(mesh)
            skeleton = sel.pop()
            dagPath2 = getDagPath(skeleton)
            if dagPath1.hasFn(om.MFn.kMesh) and dagPath2.hasFn(om.MFn.kJoint):
                return mesh, skeleton
            else:
                om.MGlobal.displayError("\"%s\" isn't mesh type, \"%s\" isn't skeleton type." % mesh % skeleton)
    except:
        return ""


mesh, skeleton = getModelFromSelection()
cmds.bbwSolver(tm=mesh, tb=skeleton, res=128)