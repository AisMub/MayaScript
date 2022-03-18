import maya.cmds as cmds

def operatorButton():
    sel = cmds.ls(selection=True)
    for i in sel:
        angka = cmds.getAttr(i+".scale")[0]
        if angka[0] > 1 and angka[1] > 1 and angka[2] > 1:
            cmds.delete(i)


if cmds.window( "id_window", exists=True ):
    cmds.deleteUI( "id_window" )


cmds.window( "id_window", title="Judul", width =300, height=300 )
cmds.columnLayout( adjustableColumn=True, columnAlign="center" )
cmds.text( label="Welcome" )


cmds.button(command="operatorButton()")
cmds.showWindow()



# buat control
controls = cmds.circle( name="Control", ch=False )



