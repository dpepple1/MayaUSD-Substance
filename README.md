# MayaUSD-Substance
A plugin for Autodesk Maya that enables easy importing of texture files into materials. 

## Installation:

1. Download the repostitory files onto your computer. The location of the files is not important.   
2. Open Maya and change to the shelf tab where you would like the plugin icon to appear.  
3. Drag and drop the ```install.mel``` file into your Maya viewport.  
4. Make sure you have the official MayaUSD plugin enabled on your device.  
5. If you move the location of the downloaded repository after installing, the plug-in will need to be reinstalled.

## Usage Instructions: 

1. After installation the plug-in will appear as an icon in your shelf bar:   
![The Installed Icon](/images/icon_screenshot.png)

2. Clicking this icon will open the plug-in's user interface: 
![The User Interface](/images/ui_screenshot.png)

3. First select the type of material you would like to generate and the stage you would like to add the materials to by using the dropdowns at the top.

4. Next, give the material a name by entering it into the textbox at the top of the material settings.

5. Add the file paths to the textures you would like to use for the material. You may upload files one at a time using the seperate "Browse..." buttons or you may upload multiple files at once and have them automatically sorted by using the "Browse All" button. If you only select one material when using "Browse All," all other texture files with the same matching prefix name will be automatically detected and added.

6. Select any objects in your viewport you would like to add the new material to. Click "Add Selected Object" to queue them for texture application. This step is optional. 

7. Finally, click "Save to New Layer." This will create a new anonymous layer in your USD scene that contains the materials and any overrides you requested to apply the materials to geometry.

