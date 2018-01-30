# Executable script for blender that exports all objects as separate files. Compatible for obj, fbx, 3ds, x3d file types.
# Written by Connor Glasgow, 1/30/18
# GitHub: https://github.com/SkeletalReality
# Twitter: https://twitter.com/SkeletalReality

# Simply hit "Run Script" once this file is opened in a Text Editor view.
# Expect freezing if your scene has 100+ objects, but it should do its job.

filetype = 'obj' # obj, fbx, 3ds, or x3d
outputfolder = 'C:\\outputfolder\\' # File redirectory you want the objects in
selectiononly = False # Will export only the selection into separate files rather the whole scene.

import bpy
selected = bpy.context.selected_objects

def exportobject(obj, filetype, outputfolder):
    bpy.ops.object.select_all(action='DESELECT')
    obj.select = True
    exportName = outputfolder + obj.name + '.' + filetype
    if filetype == 'obj':
        bpy.ops.export_scene.obj(filepath=exportName, use_selection=True)
    elif filetype == 'fbx':
        bpy.ops.export_scene.fbx(filepath=exportName, use_selection=True)
    elif filetype == '3ds':
        bpy.ops.export_scene.autodesk_3ds(filepath=exportName, use_selection=True)
    elif filetype == 'x3d':
        bpy.ops.export_scene.x3d(filepath=exportName, use_selection=True)
    else:
        print("Incorrect filetype input.")

def separateexport(filetype, outputfolder, selectiononly):
    if (selectiononly):
        for num,obj in enumerate(selected):
            exportobject(obj, filetype, outputfolder)
    else:
        for obj in bpy.data.objects:
            exportobject(obj, filetype, outputfolder)

separateexport(filetype, outputfolder, selectiononly)