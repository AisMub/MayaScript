import maya.cmds as cmds
from functools import partial


# varibel global
type_control = 0
def cc(item):
    global type_control
    if item == 'Circle':
        type_control = 0
    elif item == 'Square':
        type_control = 1
    elif item == 'Cube':
        type_control = 2


def makeControl( typecontrol, nameControl ):
    if typecontrol == 0 :
        # circle
        ctrl = cmds.circle( name=nameControl, ch=False )[0]

    elif typecontrol == 1 :
        # square
        ctrl = cmds.curve( name=nameControl, d=1, p=[[-1, 0, -1], [-1, 0, 1], [1, 0, 1], [1, 0, -1], [-1, 0, -1]] )

    elif typecontrol == 2 :
        # cube
        ctrl = cmds.curve( name=nameControl, d=1,  p = [[-0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, -0.5, 0.5], [ -0.5, -0.5, 0.5], [-0.5, 0.5, 0.5], [-0.5, 0.5, -0.5], [ -0.5, -0.5, -0.5], [-0.5, -0.5, 0.5], [-0.5, 0.5, 0.5], [ 0.5, 0.5, 0.5 ], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5], [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5,], [0.5, 0.5, -0.5], [0.5, 0.5, 0.5], [0.5, -0.5, 0.5], [0.5, -0.5, -0.5], [0.5, -0.5, 0.5], [-0.5, -0.5, 0.5], [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5]])
    return ctrl


def color():
    pass


# check colors
color_control = 6
def colors_Cmd( id_color, list_color_id, *args ):
    global color_control
    Q = cmds.checkBox( id_color, query=True, value=True )
    if Q == True :
        for clr in list_color_id :
            cmds.checkBox( clr, edit=True, value=False )

    if id_color == "red_CB" :
        color_control = 13

    elif id_color == "pink_CB":
        color_control = 20

    elif id_color == "green_CB":
        color_control = 14
    
    elif id_color == "blue_CB":
        color_control = 6
    
    elif id_color == "yellow_CB":
        color_control = 17

def operatorButton(*args):

    # list
    list_control = []
    list_grup = []

    list_joint_selected = cmds.ls( selection=True, type="joint" )
    for i in list_joint_selected:
        
        qry_translate = cmds.xform( i, query=True, ws=True, t=True )
        qry_rotate = cmds.xform( i, query=True, ws=True, ro=True )

        controls = makeControl(type_control, i+"_CONTROLS")
        list_control.append(controls)


        cmds.setAttr( "{0}.overrideEnabled".format(controls), True ) # aktifin enable offerides
        cmds.setAttr( "{0}.overrideColor".format(controls), color_control ) # masukin index colornya berapa
        groups = cmds.group( controls, name="{0}_GROUP".format(i) )
        list_grup.append(groups)


        cmds.xform( groups, ws=True, t=qry_translate, ro=qry_rotate )
        cmds.parentConstraint( controls, i, maintainOffset=True )

    for i in zip(list_control, list_grup[1:]) :
        c = i[0]
        g = i[1]
        cmds.parent(g, c)

import maya.cmds as cmds 



if cmds.window( "id_window", exists=True ) :
    cmds.deleteUI( "id_window" )

cmds.window( "id_window", title="-Welcome-", width =300, height=300 )
cmds.columnLayout( adjustableColumn=True, columnAlign="center" )
cmds.separator(style='none',height=8)

#-----ComboBox-----#
polygonSelectMenu = cmds.optionMenu(w = 250, label = "Type Controller:",changeCommand = cc)
cmds.menuItem(label = "Circle")
cmds.menuItem(label = "Square")
cmds.menuItem(label = "Cube")

#-----CheckButton-----#
cmds.frameLayout(label="Select Color")
cmds.rowColumnLayout(numberOfColumns = 5)

cmds.checkBox("red_CB", label='Red', align='center', value=True, changeCommand=partial(colors_Cmd, "red_CB", ["pink_CB", "green_CB", "blue_CB", "yellow_CB"]))
cmds.checkBox("pink_CB",label='Pink', align= 'center',  changeCommand=partial(colors_Cmd, "pink_CB", ["red_CB", "green_CB", "blue_CB", "yellow_CB"]))
cmds.checkBox("green_CB",label='Green',  changeCommand=partial(colors_Cmd, "green_CB", ["pink_CB", "red_CB", "blue_CB", "yellow_CB"]))
cmds.checkBox("blue_CB",label='Blue' ,changeCommand=partial(colors_Cmd, "blue_CB", ["pink_CB", "green_CB", "red_CB", "yellow_CB"]))
cmds.checkBox("yellow_CB",label='Yellow', changeCommand=partial(colors_Cmd, "yellow_CB", ["pink_CB", "green_CB", "blue_CB","red_CB",]))

#-----Button-----#
cmds.setParent('..')
cmds.button( label = 'Build Final',command = operatorButton)

cmds.showWindow() 