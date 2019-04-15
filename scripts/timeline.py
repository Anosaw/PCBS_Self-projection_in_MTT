"""
The script to create the timeline to present the experiment
"""

import pygame
import sys

pygame.init()

#define variables for the screen
width = 1500
height = 300

#open a window
screen = pygame.display.set_mode((width, height))

#name the colors for convenience
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

#fill the screen with black
screen.fill(white)

#define variables for the arrows
arrow_length = width #length of the arrow
arrow_span = height / 6 #width of the arrows
arrow_head = arrow_span / 2 #length of the head of the arrows
arrow_height = height / 2 #height of the arrows on the screen

#arrow
pygame.draw.lines(screen, black, False, [(0, arrow_height),
 (arrow_length, arrow_height)], 5)
pygame.draw.lines(screen, black, False, [(arrow_length, arrow_height),
 (arrow_length - arrow_head, arrow_height + arrow_span / 2)], 5)
pygame.draw.lines(screen, black, False, [(arrow_length, arrow_height),
 (arrow_length - arrow_head, arrow_height - arrow_span / 2)], 5)

#define variables for points
year_span = 70 #number of years on the timeline
n_projections = 6 #number of projections (not counting present)
projection_span = 3 #number of years between projections
n_events = 24 #number of events (not counting present)
event_span = 3 #number of years between events
tick_height = arrow_length / 100 #height of the tick

distance_between_years = arrow_length / year_span

#place present
pygame.draw.lines(screen, black, False, [(arrow_length / 2, arrow_height + tick_height),
 (arrow_length / 2, arrow_height - tick_height)], 5)

#place projection points
i = 0
while i <= int(n_projections):
    pygame.draw.lines(screen, red, False,
     [(arrow_length / 2 - ((n_projections / 2 - i) * projection_span) * distance_between_years,
     arrow_height + tick_height),
     (arrow_length / 2 - ((n_projections / 2 - i) * projection_span) * distance_between_years,
     arrow_height - tick_height)], 5)
    i += 1

#place events in the past
i = 0
while i <= int(n_events/2):
    pygame.draw.lines(screen, green, False,
     [(arrow_length / 2 - distance_between_years - ((n_events / 2 - i) * event_span) * distance_between_years,
     arrow_height + tick_height),
     (arrow_length / 2 - distance_between_years - ((n_events / 2 - i) * event_span) * distance_between_years,
     arrow_height - tick_height)], 3)
    i += 1

#place events in the future
i = 0
while i <= int(n_events/2):
    pygame.draw.lines(screen, green, False,
     [(arrow_length / 2 + distance_between_years + ((n_events / 2 - i) * event_span) * distance_between_years,
     arrow_height + tick_height),
     (arrow_length / 2 + distance_between_years + ((n_events / 2 - i) * event_span) * distance_between_years,
     arrow_height - tick_height)], 3)
    i += 1

#display changes
pygame.display.update()

#save image
pygame.image.save(screen, "timeline.png")

# wait till the window is closed
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
