import bpy

from . import configfile

colors = configfile["node_color_presets"]

class TooManyColors(bpy.types.Menu):
    bl_label = "TooManyColors"
    bl_idname = "WINDOW_MT_TooManyColors"

    def draw(self, context):
        layout = self.layout

        # Node color presets
        layout.menu(ColorMenu.bl_idname)
        layout.operator("node.remove_node_color", text="Remove node color")

class ColorMenu(bpy.types.Menu):
    bl_label = "Set node color"
    bl_idname = "WINDOW_MT_NodeColorMenu"

    def draw(self, context):
        layout = self.layout
        for key, value in colors.items():
            setcol = layout.operator("node.set_node_color", text=str(key))
            setcol.col_r = value["r"]; setcol.col_g = value["g"]; setcol.col_b = value["b"]

def draw_item(self, context):
    layout = self.layout
    layout.menu(TooManyColors.bl_idname)