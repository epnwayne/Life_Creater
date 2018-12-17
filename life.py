from life_data import Country, Background, Event, Ending
import random

#country = random.choice(list(Life.keys()))
#background = random.choice(list(Life[country].keys()))
#work = random.choice(list(Life[country][background]))

def country():
    c = random.choice(Country)
    return c

def background(i):
    b = random.choice(Background[i])
    return b

#def work(country, background):
#    w = random.choice(list(Life[country][background]))
#    return w

#print('country = ' + country)
#print('background = ' + background)
#print('work = ' + work)
