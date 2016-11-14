#! /usr/bin/env python
''' Extracts the mininum temperature on a chosen day of the year from
    the Minnesota Dept of Natural Resources (MN-DNR) records of compiled
    temperature data at/near the airport.  Data are obtained from:
    http://www.dnr.state.mn.us/climate/twin_cities/listings.html

    Writes out a CSV file called min_temps.txt with the year and minTemp
    and a single header line (for reading in to R)
'''

def main():

    date_selec = '01-15'    # mm-dd within the year to select

    filelist = [ '1930s.txt','1940s.txt','1950s.txt','1960s.txt',
                        '1970s.txt','1980s.txt','1990s.txt','2000s.txt' ]

    w = open('min_temps.txt',mode='w+')     # output file
    w.write('year,minTemp\n')               # header line for R's read.csv

    for filename in filelist:
        f = open(filename, mode='r')
        for line in f.readlines():
            # pick off the lines for selected date
            if line[5:10] == date_selec:
                split_line = line.split(',')
                year = split_line[0][:4]
                min_temp = split_line[2]
                w.write(year+','+min_temp+'\n')
        f.close()

    w.close()


if (__name__ == '__main__'):
    main()
