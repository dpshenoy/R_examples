#! /usr/bin/env python
''' Check the min and max temps in allyears.txt, at least one
    is "M" for missing:

        1939-05-22,90,M,0.00,0.0,0,24,,0,0,0

    I have to decide how to handle, but assess the problem first...
    Okay, after a run of this program, looks like this is the ONLY
    row that is missing a minimum temperature.  The minimum temperature
    for the days before and after are 48 and 49.  Mean is 48.5, round
    up to 49, and replace the M with 49.  I am doing that manually
    in the original 1930s.txt file.
'''

def main():
    f = open('allyears.txt', mode='r')

    for line in f.readlines():
        words = line.split(',')

        # try to convert maxTemp to int; if it fails, display why
        try:
            maxTemp = int(words[1])
        except (ValueError):
            print(line)

        # try to convert maxTemp to int; if it fails, display why
        try:
            minTemp = int(words[2])
        except (ValueError):
            print(line)



if (__name__ == '__main__'):
    main()
