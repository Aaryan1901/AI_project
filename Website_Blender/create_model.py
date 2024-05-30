import bpy

# Read the user input from the file
with open('user_input.txt', 'r') as f:
    user_input = f.read()

# Clear all existing meshes
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Create a new text object with the user input
bpy.ops.object.text_add(location=(0, 0, 0))
text_obj = bpy.context.object
text_obj.data.body = user_input

# Save the Blender file
bpy.ops.wm.save_as_mainfile(filepath='output.blend')
