import maya.cmds as cmds



def operatorButton() :
    print ("test panggil operator")



# replace window
if cmds.window( "id_window", exists=True ) :
    cmds.deleteUI( "id_window" )


# buat window dasar
cmds.window( "id_window", title="Judul", width =300, height=300 )

# buat layout
cmds.columnLayout( adjustableColumn=True, columnAlign="center" )

# tambah text
cmds.text( label="Ini Text" )

# operator button
cmds.button( command="operatorButton()" )


cmds.showWindow()