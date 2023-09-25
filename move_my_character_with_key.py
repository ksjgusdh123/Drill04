from pico2d import *

open_canvas()
character = load_image('sonic.png')
ground = load_image('TUK_GROUND.png')

stand_index = [0,51,101,147,196,270]
running_index = [-3,55,115,170, 170]
jump_index_x = [0, 80, 0, 0, 0]
jump_index_y = [150, 150, 245, 245, 245]
down_index_x = [90, 165, 170, 170, 170]
down_index_y = [260, 250, 152, 152, 152]

def handle_events():
    global dir_x, dir_y, running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                frame = -1
                dir_y += 1
            elif event.key == SDLK_DOWN:
                frame = -1
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True
x = 800 // 2
y = 600 // 2
frame = 0
dir_x = 0
dir_y = 0

while running:
    clear_canvas()
    ground.draw(800 // 2, 600 // 2)
    if(dir_y != 0):
        if(dir_y > 0):
            if(dir_x > 0):
                character.clip_draw(20 + jump_index_x[frame], jump_index_y[frame], 65, 105, x, y)
            else:
                character.clip_composite_draw(20 + jump_index_x[frame], jump_index_y[frame], 65, 105, 0, 'h', x, y, 65, 105)
        elif (dir_y < 0):
            character.clip_draw(20 + down_index_x[frame], down_index_y[frame], 55, 95, x, y)
    elif(dir_x != 0):
        if(dir_x > 0):
            character.clip_draw(255 + running_index[frame], 85, 50, 80, x, y, 45, 100)
        elif(dir_x < 0):
            character.clip_composite_draw(255 + running_index[frame], 85, 50, 80, 0, 'h', x, y, 45, 100)
    else:
        character.clip_draw(173 + stand_index[frame], 345, 45, 100, x, y, 45, 100)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 5
    if(dir_x > 0):
        if(x < 700):
            x += dir_x * 5
    elif (dir_x < 0): 
        if (x > 50):
            x += dir_x * 5

    if(dir_y > 0):
        if(y < 500):
            y += dir_y * 5
    elif(dir_y < 0):
        if(y > 50):
            y += dir_y * 5
    delay(0.07)

close_canvas()