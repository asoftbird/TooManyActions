import bpy

from . import configfile

colors = configfile["node_color_presets"]

class TooManyActions(bpy.types.Menu):
    bl_label = "TooManyActions"
    bl_idname = "WINDOW_MT_TooManyActions"

    def draw(self, context):
        layout = self.layout

        # Node color presets
        layout.menu(ColorMenu.bl_idname)
        layout.operator("node.remove_node_color", text="Remove node color")
        layout.operator("node.select_grouped_color", text="Select nodes with similar color")
        layout.operator("node.add_comment_reroute", text="Add comment")

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
    layout.menu(TooManyActions.bl_idname)