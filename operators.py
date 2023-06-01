import bpy

from . import configfile

class NODE_OT_set_node_color(bpy.types.Operator):
    bl_label = "Set node color"
    bl_idname = "node.set_node_color"

    col_r: bpy.props.FloatProperty(default=0.5)
    col_g: bpy.props.FloatProperty(default=0.5)
    col_b: bpy.props.FloatProperty(default=0.5)

    @classmethod
    def poll(cls, context):
        return True if hasattr(context, 'selected_nodes') else False

    def execute(self, context):
        for node in context.selected_nodes:
            node.color = (self.col_r, self.col_g, self.col_b)
            node.use_custom_color = True
        return {'FINISHED'}

class NODE_OT_remove_node_color(bpy.types.Operator):
    bl_label = "Remove node color"
    bl_idname = "node.remove_node_color"

    @classmethod
    def poll(cls, context):
        return True if hasattr(context, 'selected_nodes') else False

    def execute(self, context):
        for node in context.selected_nodes:
            node.use_custom_color = False
        return {'FINISHED'}
