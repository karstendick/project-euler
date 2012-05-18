#PE #205

from random import randint

ntrials = 10000000

Pwins = 0
for i in xrange(1,ntrials+1):
    Ptotal = randint(1,4) +randint(1,4) +randint(1,4) +randint(1,4) +randint(1,4) +randint(1,4) +randint(1,4) +randint(1,4) +randint(1,4)
    Ctotal = randint(1,6) +randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)
    if Ptotal > Ctotal:
        Pwins += 1

print Pwins/(1.0*ntrials)
