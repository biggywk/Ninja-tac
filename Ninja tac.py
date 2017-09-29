
import arcade
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
class NinjaWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)














def main():
    window = NinjaWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
if __name__ == '__main__':
    main()
