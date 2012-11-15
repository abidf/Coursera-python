# implementation of card game - Memory
#I'm storing crads on deck as lists of 4 elements: position of left-upper corner,
#number and two boolean variable: first - is this card exposed, second - has 
#player already find pair to this card

import simplegui
import random
WIDTH = 800
HEIGHT = 100
CARD_WIDTH = 50
IDENT_1 = 2
IDENT_2 = 20
moves = 0
deck = []
last_try = []
exposed_count = 0
guessed_pairs = 0


# helper function to initialize globals
def init():
    global deck, moves, last_try, exposed_count, guessed_pairs
    moves = 0
    last_try = []
    exposed_count = 0
    guessed_pairs = 0
    deck = []
    numbers = [x % 8 for x in range(16)]
    random.shuffle(numbers)
    for i in range(16):
        deck.append([CARD_WIDTH * i, numbers[i], False, False])
        
#helper function to flip all unguessed cards face down
def all_down():
    for card in deck:
        if not card[3]: 
            card[2] = False

     
# define event handlers
def mouseclick(pos):
    global exposed_count, last_try, moves, guessed_pairs
    x, y = pos
    if exposed_count == 0:
        for card in deck:
            if 0 < (x - card[0]) < CARD_WIDTH:
                 if not card[2]:
                    card[2] = True
                    last_try = card
                    exposed_count = 1
                    moves += 1
    elif exposed_count == 1:
        for card in deck:
            if 0 < (x - card[0]) < CARD_WIDTH:
                 if not card[2]:
                    card[2] = True
                    exposed_count = 2
                    if last_try[1] == card[1]:
                        last_try[3] = True
                        card[3] = True
                        guessed_pairs += 1
                    moves += 1
    else:
        for card in deck:
            if 0 < (x - card[0]) < CARD_WIDTH:
                 if not card[2]:
                    all_down()
                    card[2] = True
                    last_try = card
                    exposed_count = 1
                    moves += 1
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card in deck:
        l.set_text("Moves = " + str(moves // 2))
        if card[2]:
            canvas.draw_text(str(card[1]), 
                         (card[0] + IDENT_1, HEIGHT - IDENT_2), 
                         70, "White")
        else:
            canvas.draw_polygon([(card[0], 0),
                                (card[0] + CARD_WIDTH, 0),
                                (card[0] + CARD_WIDTH, HEIGHT),
                                (card[0], HEIGHT)], 1, 
                                "White", "Grey")
    
    
        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric
