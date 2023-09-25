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
                dir_y += 1
            elif event.key == SDLK_DOWN:
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

        pass
    elif(dir_x != 0):
        if(dir_x > 0):
            character.clip_draw(255 + running_index[frame], 85, 50, 80, x, y, 45, 100)
            pass
        elif(dir_x < 0):
            character.clip_composite_draw(255 + running_index[frame], 85, 50, 80, 0, 'h', x, y, 45, 100)
            pass

        pass
    else:
        character.clip_draw(173 + stand_index[frame], 345, 45, 100, x, y, 45, 100)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 5
    x += dir_x * 5
    y += dir_y * 5
    delay(0.05)

close_canvas()