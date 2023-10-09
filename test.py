import cv2
import numpy as np
import trimesh
import pyrender
# fuze_trimesh = trimesh.load('pyrender/examples/models/wood.obj')
fuze_trimesh = trimesh.load('demo.obj')
mesh = pyrender.Mesh.from_trimesh(fuze_trimesh)
# Create a Pyrender scene and add the mesh to it
scene = pyrender.Scene(ambient_light=[0.245, 0.42, 0.32], bg_color=[0.55, 0.55, 0.55])
scene.add(mesh)

# pyrender.Viewer(scene, use_raymond_lighting=True)

# Create a Pyrender camera (e.g., PerspectiveCamera or OrthographicCamera)
camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0)

# Adjust the camera position and target as needed
camera_pose = np.array([
    [1.0, 0.0,  0.0, 0.0],
    [0.0, 1.0,  0.0, 0.0],
    [0.0, 0.0,  1.0, 2.0],  # Adjust the Z position
    [0.0, 0.0,  0.0, 1.0]
])
scene.add(camera, pose=camera_pose)

# Create an OffscreenRenderer
r = pyrender.OffscreenRenderer(viewport_width=800, viewport_height=600)

# Render the scene
color, _ = r.render(scene)



# Convert the color image to OpenCV format (BGR)
color_cv = cv2.cvtColor(color, cv2.COLOR_RGB2BGR)

# Display the rendered image using OpenCV
cv2.imshow("Rendered Image", color_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()