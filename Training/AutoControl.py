import maya.cmds as cmds

def operatorButton():
    list_joint_selected = cmds.ls( selection=True, type="joint" )

    for i in list_joint_selected:
        
        qry_translate = cmds.xform( i, query=True, ws=True, t=True )
        qry_rotate = cmds.xform( i, query=True, ws=True, ro=True )

        controls = cmds.circle( name="{0}_CONTROL".format(i), ch=False )[0]
        groups = cmds.group( controls, name="{0}_GROUP".format(i) )

        cmds.xform( groups, ws=True, t=qry_translate, ro=qry_rotate )
        cmds.parentConstraint( controls, i, maintainOffset=True )
        
def rename():
    list = cmds.ls( selection=True )
    for i in list:
        nama_baru = i + "_MSH"
        cmds.rename( i, nama_baru )        


if cmds.window( "id_window", exists=True ) :
    cmds.deleteUI( "id_window" )

cmds.window( "id_window", title="Judul", width =300, height=300 )
cmds.columnLayout( adjustableColumn=True, columnAlign="center" )
cmds.text( label="Push This Button...!!!" )
cmds.button( label = "Tombol",command="operatorButton()" )

# ini buat baris kolom
cmds.rowColumnLayout( numberOfColumns=2 )
cmds.button( label='Rename', command= 'rename()', width=150 )

# kayak pilihan combo box
cmds.optionMenu(width=150)
cmds.menuItem( label="satu" )
cmds.menuItem( label="dua" )
cmds.menuItem( label="tiga" )

# keluar dari baris kolom layout
cmds.setParent('..')

cmds.button( label="satu kolom lagi" )
cmds.button( label="satu kolom lagi deh" )


cmds.showWindow()