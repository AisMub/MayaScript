import maya.cmds as cmds


# list
list_controls = []
list_groups = []

# buat list selected ovject
list_selected = cmds.ls( selection=True )

# buat joint
cmds.select( clear=True ) 
Joint = cmds.joint(name="namanya", position=[0, 0, 0])

# buat control
control = cmds.circle( name="namanya", constructionHistory=True )[0]
list_controls.append( control )

# buat group
group_kosong = cmds.group( name="namanya", empty=True )
group_object = cmds.group( variable_object_nya, name="Grup Keluarga pak haji" )

# buat contraint
parent_constraint = cmds.parentConstraint( object_pertama, object_kedua, maintainOffset=True )
scale_constraint = cmds.scaleConstraint( object_pertama, object_kedua, maintainOffset=True )

# buat ganti warna
cmds.setAttr( "variabelObject.overrideEnabled", True ) # aktifin enable offerides
cmds.setAttr( "variabelObject.overrideColor", 13 ) # masukin index colornya berapa

ctr = cmds.circle()
grp = cmds.group()

# parent / buat gabungin
cmds.parent( ctr, grp )

# parent hierarchy



