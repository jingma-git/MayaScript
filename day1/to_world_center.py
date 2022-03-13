import maya.cmds as cmd
import sys

def checkSelect():
    list_select = []
    if cmd.ls(sl=True) != []:
        list_select = cmd.ls(sl=True)
        return list_select
    else:
        return []

def centerPivot():
    for i in checkSelect():
        cmd.xform(i, centerPivots=True)

def meshMoveToWorldPositionAndClean():
    centerPivot()
    for i in checkSelect():
        cmd.move(0, 0, 0, i, rpr=True)
        cmd.makeIdentity(i, a=True)

def mainGui():
    windowName = 'CC_Tool'
    windowTitle = 'CC_Tool1.0'

    try:
        cmd.deleteUI(windowName)
    except:
        pass

    cmd.window(windowName, title=windowTitle)
    cmd.columnLayout(adj=True)
    explain = "move mesh to world center"
    cmd.button(l='zeroMeshClean', ann=explain, h=60, w=20, c='meshMoveToWorldPositionAndClean()')
    cmd.showWindow(windowName)


mainGui()