
import pygame
import time

import controls
import rendering


try:
    renderer = rendering.Renderer()
    renderer.go_to_level(1)

    running = True
    while running:
        start_time = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue

            controls.check_event(event)

        renderer.render()

        sleep_time = (1 / 60) - (time.time() - start_time)
        if sleep_time > 0:
            time.sleep(sleep_time)
        else:
            print("frame lag")

except KeyboardInterrupt:
    print("exited")
finally:
    pygame.quit()
