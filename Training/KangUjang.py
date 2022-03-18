import maya.cmds as cmds

list_selected = cmds.ls( selection=True )
for i in list_selected:
    cmds.select( clear=True ) 
    Joint = cmds.joint(name="Joint", position=[0, 0, 0])

    # buat control
    Kontrol = cmds.circle( name="KONTrol".format(i), constructionHistory=True )

    # buat group
    group_kosong = cmds.group( name="RIG".format(i), empty=True )
    group_object = cmds.group( Kontrol,Joint, name="Whatever".format(i) )

    # buat contraint
    parent_constraint = cmds.parentConstraint( Kontrol, Joint, i ,maintainOffset=True )
    scale_constraint = cmds.scaleConstraint( Kontrol, Joint, i , maintainOffset=True )

    # buat ganti warna
    cmds.setAttr( "{0}.overrideEnabled".format(Kontrol[0]), True ) # aktifin enable offerides
    cmds.setAttr( "{0}.overrideColor".format(Kontrol[0]), 13 ) # masukin index colornya berapa

    # parent / buat gabungin
    cmds.parent( Joint, Kontrol[0] )
    cmds.parent( group_object, group_kosong )




sel = cmds.ls( sl=True )[0]
controls = sel

cmds.select( "{}.cv[:]".format(controls) )
cmds.scale( 5, 5, 5 )


