"""
creates the grid of events to give the participants
"""

import pygame
import sys
import csv

with open("documents/event_list.csv", "rb") as list:
    events = csv.reader(list, delimiter = ',')

events.row[1]




font_size = 40
font = pygame.font.Font(None, font_size)

width =
height =

distance_to_border =
first_line = (distance_to_border, height / 5)

date = font.render(date, True, white)
screen.blit(date, first_line)

#display changes
pygame.display.update()

#save image
pygame.image.save(screen, "event_grid.png")


# wait till the window is closed
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
