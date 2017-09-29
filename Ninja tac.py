
import arcade
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
Scale = 1
class NinjaWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.background = arcade.load_texture("pics/sand back.jpg")
        
        
        
    def on_draw(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.start_render()
        
       
        











def main():
    window = NinjaWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
if __name__ == '__main__':
    main()
