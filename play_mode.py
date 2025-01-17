import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global balls
    global zombies
    global fired_balls

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    balls = [Ball(random.randint(100, 1600-100), 60, 0, is_fired=False) for _ in range(30)]
    game_world.add_objects(balls, 1)

    fired_balls = []

    game_world.add_collision_pair('boy:ball', boy, None)

    for ball in balls:
        game_world.add_collision_pair('boy:ball', None, ball)

    # 좀비 5마리 추가
    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)

    game_world.add_collision_pair('boy:zombie', boy, None)

    for zombie in zombies:
        game_world.add_collision_pair('boy:zombie', None, zombie)
        game_world.add_collision_pair('zombie:ball', zombie, None)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update() # 소년과 볼의 위치가 업데이트 완료됨.

    #for ball in balls.copy():
    #    if game_world.collide(boy, ball):
    #        print('COLLISION boy:ball')
    #        boy.ball_count += 1
    #        game_world.remove_object(ball)
    #        balls.remove(ball)

    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

