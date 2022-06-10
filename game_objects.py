import math


class GameObject:
    def __init__(self, rect, speed):
        self.rect = rect
        self.speed = speed
    
    def collided_with(self, game_object, collision_distance):
        distance = math.sqrt(math.pow(self.rect.x - game_object.rect.x, 2) + math.pow(self.rect.y - game_object.rect.y, 2))
        if distance <= collision_distance:
            return True
        else:
            return False


class Player(GameObject):
    def __init__(self, rect, speed):
        super().__init__(rect, speed)


class Invader(GameObject):
    def __init__(self, rect, speed, movement_direction_right):
        super().__init__(rect, speed)
        self.movement_direction_right = movement_direction_right


class Bullet(GameObject):
    def __init__(self, rect, speed, ready_for_shot):
        super().__init__(rect, speed)
        self.ready_for_shot = ready_for_shot
        self.init_position_x = rect.x
        self.init_position_y = rect.y

    def reset_position(self):
        self.rect.x = self.init_position_x
        self.rect.y = self.init_position_y

