import random
import arcade
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
SPRITE_SCALING = 0.5
MOVEMENT_SPEED = 5
class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1
class NinjaWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.all_sprites_list = None

        self.player_sprite = None
        self.score = 0
    def setup(self):

        self.all_sprites_list = arcade.SpriteList()

        self.score = 0
        self.player_sprite = Player("pics/ninja1.jpg", SPRITE_SCALING)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500
        self.all_sprites_list.append(self.player_sprite)
        self.background = arcade.load_texture("pics/sand back.jpg")
    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()
    def update(self, delta_time):
        self.all_sprites_list.update()    
    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    window = NinjaWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()
if __name__ == '__main__':
    main()
