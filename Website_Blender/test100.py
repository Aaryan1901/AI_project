import bpy
import addon_utils

# Enable MB-Lab add-on
addon_name = 'MB-Lab'
addon_utils.enable(addon_name)

# List all operators in the mbast namespace to verify correct names
mbast_ops = dir(bpy.ops.mbast)
print("Available MB-Lab Operators:", mbast_ops)

# Use the correct operator to initialize a character
if 'init_character' in mbast_ops:
    bpy.ops.mbast.init_character('INVOKE_DEFAULT')
else:
    print("init_character operator not found. Available operators:", mbast_ops)