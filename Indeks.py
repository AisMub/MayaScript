import maya.cmds as cmds

# buat tanya angkanya berapa, kita bisa ambil angkanya pake
sel = cmds.ls(selection=True)
for i in sel:
    angka = cmds.getAttr(i+".scale")[0]
    if angka[0] > 1 and angka[1] > 1 and angka[2] > 1:
        cmds.delete(i)


# import maya.cmds as cmds

# "mesh"

# sel = cmds.ls( type="locator" )
# cmds.select( sel )

#sel = cmds.ls(Selection=True)

''''def atur(list_object, kali):
    for i in list_object:
        get_transform = cmds.listRelatives( i, parent=True )
        for axis in ("X", "Y", "Z") :
            getAttr_Scale = cmds.getAttr( "{0}.translate{1}".format(get_transform[0], axis) )
            cmds.setAttr("{0}.translate{1}".format(get_transform[0], axis), getAttr_Scale*kali)
            
            getAttr_Scale = cmds.getAttr( "{0}.scale{1}".format(get_transform[0], axis) )
            cmds.setAttr("{0}.scale{1}".format(get_transform[0], axis), getAttr_Scale*kali)

            getAttr_Scale = cmds.getAttr( "{0}.rotate{1}".format(get_transform[0], axis) )
            cmds.setAttr("{0}.rotate{1}".format(get_transform[0], axis), getAttr_Scale*kali)
        
select = cmds.ls(type="mesh")
atur(select, 5)


list_loc = cmds.ls( type="locator" )
atur(list_loc, 7)'''


# buat list untuk selected object 
# ambil tiap nilai attribute setiap object yang di select
# buat locator untuk masing-masing object yang di select
# pasang nilai yang di dapat ke locator

# buat locator nya ;
#loc = cmds.shapeLocator() # ini itu hasilnya transform dalam list, jadi loc[0] udah bisa dipake ke setAttr misalnya

# loc = cmds.spaceLocator()

# sel = cmds.ls(sl=True)
# for i in sel:
#     position_object = cmds.xform( i, q=True, ws=True, t=True )
#     rotation_object = cmds.xform(i, q=True, ws=True, ro=True)

#     print (position_object)
#     print (rotation_object)
#     loc = cmds.spaceLocator()

#     cmds.xform( loc[0], ws=True, t = position_object, ro = rotation_object)


