import maya.cmds as cmds
import maya.mel as mel

out_dir = 'D:/Dataset/AutoRS'
idx = "13"
# cmds.select(clear=True)
# cmds.select('Hips')
# jointHier = cmds.select(cmds.ls(dag=1,sl=1,type='joint'))
fbx_name = out_dir + '/fbx/' + idx + '.fbx'
mel.eval('FBXExport -f "{}" -s'.format(fbx_name))