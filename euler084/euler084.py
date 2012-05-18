#Project Euler problem #84
#
# Monopoly!

from random import randint
from random import shuffle

NSQUARES = 40
GO,A1,CC1,A2,T1,R1,B1,CH1,B2,B3,JAIL,C1,U1,C2,C3,R2,D1,CC2,D2,D3,FP,E1,CH2,E2,E3,R3,F1,F2,U2,F3,G2J,G1,G2,CC3,G3,R4,CH3,H1,T2,H2 = range(NSQUARES)
NULL = -1
NEXTR = 41
NEXTU = 42
BACK3 = 43

ccdeck = [NULL for x in range(16)]
ccdeck[0] = GO
ccdeck[1] = JAIL
shuffle(ccdeck)

chdeck = [GO, JAIL, C1, E3, H2, R1, NEXTR, NEXTR, NEXTU, BACK3, NULL, NULL, NULL, NULL, NULL, NULL]
shuffle(chdeck)

cc_i = 0
def draw_cc():
    global cc_i
    cc_i = (cc_i + 1) % len(ccdeck)
    return ccdeck[cc_i]

ch_i = 0
def draw_ch():
    global ch_i
    ch_i = (ch_i + 1) % len(chdeck)
    return chdeck[ch_i]

num_doubles = 0
def advance_token(pos,dice):
    global num_doubles
    if dice[0] == dice[1]:
        num_doubles += 1
        if num_doubles >= 3:
            pos = JAIL
            num_doubles = 0
            return pos
    else:
        num_doubles = 0
    
    pos = (pos + sum(dice)) % NSQUARES

    # Go to jail
    if pos == G2J:
        pos = JAIL
    # Community Chest
    elif pos == CC1 or pos == CC2 or pos == CC3:
        card = draw_cc()
        if card == NULL:
            pass
        else:
            pos = card
    # Chance
    elif pos == CH1 or pos == CH2 or pos == CH3:
        card = draw_ch()
        if card == NULL:
            pass
        elif card == NEXTR:
            #Goto next railroad
            pass
        elif card == NEXTU:
            #Goto next utility
            pass
        elif card == BACK3:
            #Go back 3 spaces
            pos = (pos - 3) % NSQUARES
        else:
            pos = card
            
    return pos
    


visits = [0 for x in range(NSQUARES)]

dice = [0,0]
#NPIPS = 6
NPIPS = 4

NTURNS = 10**6

pos = 0

for t in xrange(NTURNS):
    dice = [randint(1,NPIPS), randint(1,NPIPS)]
    pos = advance_token(pos,dice)
    visits[pos] += 1


print visits
probs = [x/float(NTURNS) for x in visits]
print probs

iprobs = [(x,i) for i,x in enumerate(probs)]
print sorted(iprobs,reverse=True)[:3]
