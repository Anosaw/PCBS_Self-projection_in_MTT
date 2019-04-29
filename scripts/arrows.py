"""
    The script to create the arrow images needed for MTTexp, using pygame.

"""

import pygame
import sys

pygame.init()

#define variables for the screen
width = 1000
height = 300

#open a window
screen = pygame.display.set_mode((width, height))

#name the colors for convenience
white = (255,255,255)
black = (0,0,0)

#fill the screen with black
screen.fill(black)

#define variables for the arrows
arrow_length = width / 5 #length of the arrow
distance_to_border = arrow_length / 3 #distance between head of the arrow and edge of the screen
inter_arrow_distance = width - 2*arrow_length - 2*distance_to_border #distance between the tails of the arrows
arrow_span = height / 6 #width of the arrows
arrow_head = arrow_span / 2 #length of the head of the arrows
arrow_height = 2*height / 3 #height of the arrows on the screen

#draw words
font_size = 50
font = pygame.font.Font(None, font_size)

before = font.render("avant", True, white)
screen.blit(before, (distance_to_border + arrow_length / 2, height / 3))

x, y = font.size("après") #This is needed to center properly the second word

after = font.render("après", True, white)
screen.blit(after, (distance_to_border + inter_arrow_distance + 3*arrow_length / 2 - x, height / 3))

#draw arrows
#left arrow
pygame.draw.lines(screen, white, False, [(distance_to_border, arrow_height), (distance_to_border + arrow_length, arrow_height)], 5)
pygame.draw.lines(screen, white, False, [(distance_to_border, arrow_height), (distance_to_border + arrow_head, arrow_height + arrow_span / 2)], 5)
pygame.draw.lines(screen, white, False, [(distance_to_border, arrow_height), (distance_to_border + arrow_head, arrow_height - arrow_span / 2)], 5)

#right arrow
pygame.draw.lines(screen, white, False, [(distance_to_border + 2*arrow_length + inter_arrow_distance, arrow_height), (distance_to_border + arrow_length + inter_arrow_distance, arrow_height)], 5)
pygame.draw.lines(screen, white, False, [(distance_to_border + 2*arrow_length + inter_arrow_distance, arrow_height), (distance_to_border + 2*arrow_length + inter_arrow_distance - arrow_head, arrow_height + arrow_span / 2)], 5)
pygame.draw.lines(screen, white, False, [(distance_to_border + 2*arrow_length + inter_arrow_distance, arrow_height), (distance_to_border + 2*arrow_length + inter_arrow_distance - arrow_head, arrow_height - arrow_span / 2)], 5)

#display changes
pygame.display.update()

#save image
pygame.image.save(screen, "before_is_left_arrows.png")

#draw second image

screen.fill(black)

#draw words on second image
before = font.render("après", True, white)
screen.blit(before, (distance_to_border + arrow_length / 2, height / 3))

x, y = font.size("avant") #This is needed to center properly the second word

after = font.render("avant", True, white)
screen.blit(after, (distance_to_border + inter_arrow_distance + 3*arrow_length / 2 - x, height / 3))

#draw arrows
#left arrow
pygame.draw.lines(screen, white, False, [(distance_to_border, arrow_height), (distance_to_border + arrow_length, arrow_height)], 5)
pygame.draw.lines(screen, white, False, [(distance_to_border, arrow_height), (distance_to_border + arrow_head, arrow_height + arrow_span / 2)], 5)
pygame.draw.lines(screen, white, False, [(distance_to_border, arrow_height), (distance_to_border + arrow_head, arrow_height - arrow_span / 2)], 5)

#right arrow
pygame.draw.lines(screen, white, False, [(distance_to_border + 2*arrow_length + inter_arrow_distance, arrow_height), (distance_to_border + arrow_length + inter_arrow_distance, arrow_height)], 5)
pygame.draw.lines(screen, white, False, [(distance_to_border + 2*arrow_length + inter_arrow_distance, arrow_height), (distance_to_border + 2*arrow_length + inter_arrow_distance - arrow_head, arrow_height + arrow_span / 2)], 5)
pygame.draw.lines(screen, white, False, [(distance_to_border + 2*arrow_length + inter_arrow_distance, arrow_height), (distance_to_border + 2*arrow_length + inter_arrow_distance - arrow_head, arrow_height - arrow_span / 2)], 5)

#display changes
pygame.display.update()

#save image
pygame.image.save(screen, "before_is_right_arrows.png")


# wait till the window is closed
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
