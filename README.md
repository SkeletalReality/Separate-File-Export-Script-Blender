# Separate File Export (Blender)

This is an executable python script for Blender that exports all objects of the scene, or your selection, into separate files of your format choice (obj, fbx, 3ds, x3d).

## How to Use:
### 1) Open up a Text Editor view in Blender
### 2) Go to Text>Open Text Block or Alt+O and open separateexport.py
### 3) Change the variables 9 through 11 to your liking:
```
-filetype: type of file the objects are exported as (obj, fbx, 3ds, x3d)

-outputfolder: File redirectory you want the objects in (i.e. C:\\output\\)

-selectiononly: If True, will only export the selection into separate files rather the whole scene.
```
### 4) Click 'Run Script', and you're done!

Expect freezing if your scene has 100+ objects, but it should do its job.

```
| Written by Connor Glasgow, 1/30/18
| GitHub: https://github.com/SkeletalReality
| Twitter: https://twitter.com/SkeletalReality
```
