import pandas as pd
import numpy as np
import time
import requests
from bs4 import BeautifulSoup
import argparse
import sys

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()



def get_nfl_weather(year_range=range(2009,2019),week_range=range(1,18)):

    years = list(year_range)
    weeks = list(week_range)

    l = len(years)

    games = []

    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

    for i, year in enumerate(years):
        for week in weeks:

            url = f'http://www.nflweather.com/en/week/{year}/week-{week}/'

            check = requests.get(url).status_code

            if check == 200:

                url = url

            else:

                url = f'http://www.nflweather.com/en/week/{year}/week-{week}-2/'

            req = requests.get(url).text

            soup = BeautifulSoup(req,'lxml')

            for row in range(len(soup.find('table').find_all('tr')[1::1])):

                game = {}
                data = soup.find('table').find_all('tr')[1::1][row]

                try:
                    away = data.find_all('a')[0].text
                    home = data.find_all('a')[3].text
                    forecast = data.find_all('td', class_ ='text-center')[5].text
                    wind = data.find_all('td', class_ ='text-center')[6].text
                    game['away'] = away
                    game['home'] = home
                    game['forecast'] = forecast.strip('\n').strip('\n ')
                    game['wind'] = wind
                    game['year'] = year
                    game['week'] = week

                except IndexError:pass

                games.append(game)

            time.sleep(1)

        printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

    df = pd.DataFrame(games)
    df.to_csv(f"nfl_weather_{min(years)}_to_{max(years)}_weeks_{min(weeks)}_to_{max(weeks)}.csv",index=False)

    return

if __name__ == '__main__':
    ag = argparse.ArgumentParser()
    ag.add_argument('--yearstart', type=str, default = '2009')
    ag.add_argument('--yearend', type=str, default = '2018')
    ag.add_argument('--weekstart', type=str, default = '1')
    ag.add_argument('--weekend', type=str, default = '17')
    args = vars(ag.parse_args())

    if bool(args) == False:
        print('Default 2009-2018, Weeks 1-17')

    if int(args['yearstart']) < 2009:
        print('Error: Start Year must be 2009 or later.')
        sys.exit()
    if int(args['yearend']) > 2018:
        print('Error: End Year must be 2018 or earlier.')
        sys.exit()
    if int(args['weekstart']) < 1:
        print('Error: Start week must be greater than or equal to 0.')
        sys.exit()
    if int(args['weekstart']) > 17:
        print('Error: End week must be less than or equal to 17.')
        sys.exit()
    if int(args['yearend']) < int(args['yearstart']):
        print('Error: Start year must be less than end year.')
        sys.exit()
    if int(args['weekend']) < int(args['weekstart']):
        print('Error: Start week must be less than end week.')
        sys.exit()

    yearstart = int(args['yearstart'])
    yearend = int(args['yearend']) + 1
    weekstart = int(args['weekstart'])
    weekend = int(args['weekend']) + 1

    get_nfl_weather(range(yearstart,yearend),range(weekstart,weekend))
