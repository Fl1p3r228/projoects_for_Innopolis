import pygame
from inventory import inventory
from time import sleep
pygame.init()


show = True

hold_left_but = False

while show:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if click[0] and not hold_left_but:
        print(mouse)
        inventory.set_start_cell(mouse[0], mouse[1])
        hold_left_but = True
    if hold_left_but and not click[0]:
        print(pygame.mouse.get_pos())
        hold_left_but = False

        '''elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(pygame.mouse.get_pos())
                
        elif event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())'''


inventory.draw_penal()

if keys[pygame.K_TAB]:
    print(inventory.get_amount('predmet'))
    inventory.increase('predmet')
    sleep(0.1)
    print(inventory.get_amount('coal'))