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

class NODE_OT_add_comment_reroute(bpy.types.Operator):
    bl_label = "Add comment (reroute)"
    bl_idname = "node.add_comment_reroute"

    @classmethod
    def poll(cls, context):
        return True if hasattr(context, 'selected_nodes') else False

    def execute(self, context):
        bpy.ops.node.add_node(type="NodeReroute", use_transform=True)
        bpy.ops.wm.call_panel(name="TOPBAR_PT_name", keep_open=False)

        return {'FINISHED'}

class NODE_OT_select_grouped_color(bpy.types.Operator):
    bl_label = "Select nodes with similar color"
    bl_idname = "node.select_grouped_color"

    @classmethod
    def poll(cls, context):
        return True if hasattr(context, 'selected_nodes') else False

    def execute(self, context):
        bpy.ops.node.select_grouped(extend=False, type='COLOR')
        return {'FINISHED'}