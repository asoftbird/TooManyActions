# TooManyActions

Blender addon (3.3.0+) that adds a shortcut for quick node editor actions.
Current functionality:
- Set color of selected nodes to one of the predefined colors.
- Remove color from all selected nodes.
- Add Comment: adds a reroute at cursor position and immediately opens the Rename modal.

The node color functions are intended to be used together with Blender's "Select nodes by color" feature, to easily select nodes marked by colors.
The default hotkey for this addon is Ctrl+Q.

Don't like the default colors? The palette is registered in config.py and can be edited. You may need to restart Blender for the changes to take effect.

This is just a start for an addon which I want to give more functionality, features may creep in over time. 