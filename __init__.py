# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {
    "name": "TooManyActions",
    "description": "Adds a quick menu for Node Editors to quickly set color of nodes. Supports multiple selected nodes. Default hotkey Ctrl+Q.",
    "author": "asoftbird (https://titmou.se/)",
    "version": (1, 1, 1),
    "blender": (3, 3, 0),
    "category": "Interface",
    }

import json
from . import config

def load_json(file):
    data = ""
    with open(file, "r") as jsonfile:
        data = json.load(jsonfile)
        return data

configfile = config.config

if "bpy" in locals():
    import importlib
    importlib.reload(ui)
    importlib.reload(operators)
else:
    import bpy

    from . import (
        ui,
        operators,
    )

classes = (
    ui.TooManyActions,
    ui.ColorMenu,
    operators.NODE_OT_remove_node_color,
    operators.NODE_OT_set_node_color,
    operators.NODE_OT_select_grouped_color,
    operators.NODE_OT_add_comment_reroute
)

addon_keymaps = []

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # add keyboard shortcut
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name="Window", space_type='EMPTY')
        kmi = km.keymap_items.new("wm.call_menu", 'Q', 'PRESS', ctrl=True, shift=False)
        kmi.properties.name = ui.TooManyActions.bl_idname
        addon_keymaps.append((km, kmi))


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()