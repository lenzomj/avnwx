import argparse

from avnwx import WindTemp, Region, Level, ForecastCycle

def main():

    windtemp = WindTemp()

    data = windtemp.region(Region.SLC).level(Level.LOW).fcst(ForecastCycle.SIX).get_raw()

    print(data)

if __name__ == '__main__':
    main()
