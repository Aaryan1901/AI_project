import bpy

def clear_scene():
    # Delete all existing objects in the scene
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def add_cube(location, scale, rotation):
    bpy.ops.mesh.primitive_cube_add(location=location)
    cube = bpy.context.object
    cube.scale = scale
    cube.rotation_euler = rotation
    return cube

def add_sphere(location, scale, rotation):
    bpy.ops.mesh.primitive_uv_sphere_add(location=location)
    sphere = bpy.context.object
    sphere.scale = scale
    sphere.rotation_euler = rotation
    return sphere

def setup_scene():
    # Clear existing objects
    clear_scene()
    
    # Add a cube
    cube = add_cube(location=(1, 2, 3), scale=(1, 1, 1), rotation=(0, 0, 0))
    
    # Add a sphere
    sphere = add_sphere(location=(4, 5, 6), scale=(1, 1, 1), rotation=(0, 0, 0))
    
    # Add a light source
    bpy.ops.object.light_add(type='POINT', location=(5, 5, 5))
    
    # Add a camera
    bpy.ops.object.camera_add(location=(7, -7, 7))
    camera = bpy.context.object
    camera.rotation_euler = (1.1, 0, 0.7)
    bpy.context.scene.camera = camera
    render_scene("/tmp/rendered_scene.png")

def render_scene(filepath):
    bpy.context.scene.render.filepath = filepath
    bpy.ops.render.render(write_still=True)

if __name__ == "__main__":
    setup_scene()
    render_scene("/tmp/rendered_scene.png")