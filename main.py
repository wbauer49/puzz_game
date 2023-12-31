
import asyncio
import pygame
import time

import constants
import controller
import menu
import rendering
import env


async def main_loop():

    env.controller = controller.Controller()
    env.menu = menu.Menu()
    env.renderer = rendering.Renderer()

    env.menu.go_to_world(1)

    running = True
    while running:
        start_time = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue
            env.controller.check_event(event)
        env.controller.check_pressed_keys()

        env.renderer.render()

        await asyncio.sleep(0)

        sleep_time = (time.time() - start_time) / constants.FRAME_RATE
        if sleep_time > 0:
            time.sleep(sleep_time)
        else:
            print("frame lag")

try:
    asyncio.run(main_loop())
except KeyboardInterrupt:
    print("exited")
finally:
    pygame.quit()
