from abaqus import *
from abaqusConstants import *
import displayGroupOdbToolset as dgo
# opening the ODB file
odb = session.openOdb(
    name='E:/AbaPy/channel/Lec6 - Writing the field report/odb_files/Stand_wcontact.odb')
# set this ODB file to the viewport
session.viewports['Viewport: 1'].setValues(displayedObject=odb)

# Field report command
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=17, outputPosition=NODAL, 
    variable=(('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'), (COMPONENT, 
    'S11'), (COMPONENT, 'S22'), (COMPONENT, 'S33'), (COMPONENT, 'S12'), (
    COMPONENT, 'S13'), (COMPONENT, 'S23'), )), ))

# Leaf object to put the nodes onto the viewport
leaf = dgo.LeafFromOdbNodePick(nodePick=(('STAND-1', 336, (
    '[#3000000 #3 #0:5 #ff000000 #f #c0000000 #ffffffff', 
    ' #3fffff #0:18 #ff000000 #ffffffff:8 ]', )), ), )
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)

# Field report command
session.writeFieldReport(fileName='abaqus_surface_nodes.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=17, outputPosition=NODAL, 
    variable=(('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'), (COMPONENT, 
    'S11'), (COMPONENT, 'S22'), (COMPONENT, 'S33'), (COMPONENT, 'S12'), (
    COMPONENT, 'S13'), (COMPONENT, 'S23'), )), ))
