import maya.cmds as cmds


list_joint_selected = cmds.ls( selection=True, type="joint" )
qry_translate = cmds.xform( list_joint_selected[0], query=True, ws=True, t=True )
qry_rotate = cmds.xform( list_joint_selected[0], query=True, ws=True, ro=True )

controls = cmds.circle( name="Control", ch=False )
groups = cmds.group( controls, name="Group" )
cmds.xform( groups, ws=True, t=qry_translate, ro=qry_rotate )

cmds.parentConstraint( controls, list_joint_selected[0], maintainOffset=True )