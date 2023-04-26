import bpy

bl_info = {
    "name": "Select Points on Layer",
    "author": "Gary Carse",
    "version": (1, 0),
    "blender": (3, 50, 0),
    "location": "View3D > Object > Remove Empty Groups",
    "description": "Selects all the points drawn on the selected layer",
    "warning": "",
    "doc_url": "",
    "category": "Grease Pencil",
}

# THIS IS THE MAIN OPERATOR
def select_points():
    # Get the active Grease Pencil object
    obj = bpy.context.active_object
    
    # Deselect all points in all layers
    for layer in obj.data.layers:
        for frame in layer.frames:
            for stroke in frame.strokes:
                stroke.select = False
                for point in stroke.points:
                    point.select = False

    # Get the active layer
    layer = obj.data.layers.active

    # Iterate over all the frames in the layer
    for frame in layer.frames:
        # Iterate over all the strokes in each frame
        for stroke in frame.strokes:
            # Select the stroke
            stroke.select = True
            # Iterate over all the points in each stroke
            for point in stroke.points:
                # Select the point
                point.select = True


# THIS IS THE CLASS
class SelectPointsOnLayer(bpy.types.Operator):
    """Select Points On Layer"""
    bl_idname = "dopesheet.select_points_on_layer"
    bl_label = "Select Points on Layer"
  
    # THIS SAYS THE BUTTON WILL EXECUTE THE OPERATOR
    def execute(self, context):
        select_points()
        return {'FINISHED'}

# This function adds the button to a menu (referenced in the below code)
def add_to_layer_specials_menu(self, context):
    self.layout.operator("dopesheet.select_points_on_layer")
    
# This is the menu the button is being added to.
bpy.types.GPENCIL_MT_layer_context_menu.append(add_to_layer_specials_menu)

#This is the visual description of the menu button
def menu_draw(self, context):
    self.layout.operator("dopesheet.select_points_on_layer", text="Select Points On Layer")

def register():
    bpy.utils.register_class(SelectPointsOnLayer)
    bpy.types.DOPESHEET_MT_channel_context_menu.append(menu_draw)

def unregister():
    bpy.utils.unregister_class(SelectPointsOnLayer)
    bpy.types.DOPESHEET_MT_channel_context_menu.remove(menu_draw)

if __name__ == "__main__":
    register()
