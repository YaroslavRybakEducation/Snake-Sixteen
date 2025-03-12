from pygame import *

d = display

y, s, h = segments = [15, 16, 17]; n, a = s, 99; screen_fill = d.set_mode([225] * 2).fill

while segments.count(h) % 2 * h % n * (h & 240):
    if e := event.get(768): s = (e[0].key % 4 * 17 + 15) % 49 - n
    segments = segments[a != h:] + [h + s]

    screen_fill('white')
    if a == h: a = segments[0]
    for i, v in enumerate([a] + segments): screen_fill('black' if i else 'black', ((v - 1) % n * y, (v - n) // n * y, y, y))
    d.flip()
    h += s
    time.wait(100)