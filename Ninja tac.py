import random
import arcade
import math
from random import randint
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
SPRITE_SCALING = 0.5
MOVEMENT_SPEED = 8
BULLET_SPEED = 7
INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3
class Bulletp(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

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
        self.frame_count = 0
        self.all_sprites_list = arcade.SpriteList()
        self.bulletp_list = arcade.SpriteList()
        self.current_state =0
        self.score = 0
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
    def setup(self):
        self.current_state = 1
        self.all_sprites_list = arcade.SpriteList()
        self.bulletp_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.background = arcade.load_texture("pics/sand back.jpg")
        self.score = 0
        self.player_sprite = Player("pics/ninja1use.png", SPRITE_SCALING)
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 200
        self.all_sprites_list.append(self.player_sprite)        
    def on_draw(self):
       
            arcade.start_render()
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
            self.enemy_list.draw()
            self.bullet_list.draw()
            self.bulletp_list.draw()
            self.all_sprites_list.draw()
            output = "Score: {}".format(self.score)
            arcade.draw_text(output, 10, 20, arcade.color.RED, 14)
            if self.current_state == GAME_OVER:
                        output = "Game Over"
                        arcade.draw_text(output, 240, 400, arcade.color.BLACK, 100)
                        output = "Press R to restart"
                        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)
                    
    def on_mouse_press(self, x, y, button, delta_time):
        bulletp = Bulletp("pics/ดาวกระจาย.png", SPRITE_SCALING * 1.5)
        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        bulletp.center_x = start_x
        bulletp.center_y = start_y
        dest_x = x
        dest_y = y
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
        bulletp.angle = math.degrees(angle)
        bulletp.change_x = math.cos(angle) * BULLET_SPEED
        bulletp.change_y = math.sin(angle) * BULLET_SPEED
        self.all_sprites_list.append(bulletp)
        self.bulletp_list.append(bulletp)
    def update(self, delta_time):
        print(self.current_state);
        if self.current_state == 1:
            self.frame_count += 1
            if self.frame_count %50==0:
                enemy = arcade.Sprite("pics/badthief.png", 0.5)
                enemy.center_x = randint(0,1000)
                enemy.center_y = SCREEN_HEIGHT - enemy.height
                enemy.angle = 180
                self.all_sprites_list.append(enemy)
                self.enemy_list.append(enemy)
            for enemy in self.enemy_list:
                start_x = enemy.center_x
                start_y = enemy.center_y
                dest_x = self.player_sprite.center_x
                dest_y = self.player_sprite.center_y
                x_diff = dest_x - start_x
                y_diff = dest_y - start_y
                angle = math.atan2(y_diff, x_diff)
                enemy.angle = math.degrees(angle)-90
                if self.frame_count % 50 == 0:
                    bullet = arcade.Sprite("pics/ebbt.png")
                    bullet.center_x = start_x
                    bullet.center_y = start_y
                    bullet.angle = math.degrees(angle)
                    bullet.change_x = math.cos(angle) * BULLET_SPEED
                    bullet.change_y = math.sin(angle) * BULLET_SPEED
                    self.bullet_list.append(bullet)
                    self.all_sprites_list.append(bullet)
            for bulletp in self.bulletp_list:
                hit_list = arcade.check_for_collision_with_list(bulletp,self.enemy_list)
                if len(hit_list) > 0:
                    bulletp.kill()
                for enemy in hit_list:
                    enemy.kill()
                    self.score += 1                       
                if bulletp.top < 0:
                    bulletp.kill()
                    self.score = self.score-1
                if bulletp.top > 800:
                    bulletp.kill()
                    self.score = self.score-1
            for bullet in self.bullet_list:
                
                if (arcade.check_for_collision(bullet,self.player_sprite)) :
                    bullet.kill()
                    self.player_sprite.kill()  
                    self.current_state = GAME_OVER
                    
                if bullet.top < 0:
                    bullet.kill()
                if bullet.top > 800:
                    bullet.kill()
                    
              
            
                
            self.bulletp_list.update()
            self.bullet_list.update()

        


            
            for bulletp in self.bulletp_list:
                if bulletp.bottom > SCREEN_HEIGHT:
                    bulletp.kill()

            self.bulletp_list.update()
            self.all_sprites_list.update()
        
                
    def on_key_press(self, key, delta_time):
     
        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.R:
            if self.current_state == GAME_OVER:
                self.setup()
                self.current_state = 1
    def on_key_release(self, key, delta_time):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

def main():
    window = NinjaWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()
if __name__ == '__main__':
    main()
