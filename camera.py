from settings import *

class Camera:
    def __init__(self, position, yaw, pitch):
        self.position = glm.vec3(position)
        self.yaw = glm.radians(yaw)
        self.pitch = glm.radians(pitch)

        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.foward = glm.vec3(0, 0, -1)

        self.m_proj = glm.perspective(V_FOV, ASPECT_RATIO, NEAR, FAR)
        self.m_view = glm.mat4()

    def update(self):
        self.update_vectors()
        self.update_view_matrix()

    def update_view_matrix(self):
        self.m_view = glm.lookAt(self.position, self.position + self.foward, self.up)

    def update_vectors(self):
        self.foward.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.foward.y = glm.sin(self.yaw)
        self.foward.z = glm.sin(self.yaw) * glm.cos(self.pitch)

        self.foward = glm.normalize(self.foward)
        self.right = glm.normalize(glm.cross(self.foward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.foward))

    def rotate_pitch(self, delta_y):
        self.pitch -= delta_y
        self.pitch = glm.clamp(self.pitch, -PITCH_MAX, PITCH_MAX)

    def rotate_yaw(self, delta_x):
        self.yaw += delta_x

    def move_left(self, velocity):
        self.position -= self.right * velocity

    def move_right(self, velocity):
        self.position += self.right * velocity

    def move_up(self, velocity):
        self.position += self.up * velocity

    def move_down(self, velocity):
        self.position -= self.up * velocity

    def move_foward(self, velocity):
        self.position += self.foward * velocity

    def move_back(self, velocity):
        self.position -= self.foward * velocity