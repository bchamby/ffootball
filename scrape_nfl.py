#################
# Author: Brad Chamberlain, Eric Chamberlain
# Summary: Scrapes NFL's fantasy website for projection data at each position, QB, RB, WR, TE, K, and D/ST.
# TODO: Break out sites into separate sites.txt file and import / loop
#################

import csv
import time
import requests
from BeautifulSoup import BeautifulSoup

sites = {}
sites['nfl_qb'] = 'http://fantasy.nfl.com/research/projections?position=1&amp;statCategory=projectedStats&amp;statSeason=2015&amp;statType=weekProjectedStats&amp;statWeek=4'
sites['nfl_rb'] = 'http://fantasy.nfl.com/research/projections?position=2&amp;statCategory=projectedStats&amp;statSeason=2015&amp;statType=weekProjectedStats&amp;statWeek=4'
sites['nfl_wr'] = 'http://fantasy.nfl.com/research/projections?position=3&amp;statCategory=projectedStats&amp;statSeason=2015&amp;statType=weekProjectedStats&amp;statWeek=4'
sites['nfl_te'] = 'http://fantasy.nfl.com/research/projections?position=4&amp;statCategory=projectedStats&amp;statSeason=2015&amp;statType=weekProjectedStats&amp;statWeek=4'
sites['nfl_k'] = 'http://fantasy.nfl.com/research/projections?position=7&amp;statCategory=projectedStats&amp;statSeason=2015&amp;statType=weekProjectedStats&amp;statWeek=4'
sites['nfl_dst'] = 'http://fantasy.nfl.com/research/projections?position=8&amp;statCategory=projectedStats&amp;statSeason=2015&amp;statType=weekProjectedStats&amp;statWeek=4'

for nfl_position, nfl_url in sites.iteritems():
    response = requests.get(nfl_url)
    html = response.content
    soup = BeautifulSoup(html)
    #nfl_table = soup.findAll("div", { "class" : "tableWrap" })
    nfl_table = soup.findAll("div", { "class" : "tableWrap" })

    #Write HTML file
    output_file = open('../data/output/' + nfl_position + '.html', 'w')
    output_file.write(repr(nfl_table))
    output_file.close()

    #Create CSV file
    # list_of_rows = []
    # for row in nfl_table.findAll('tr'):
    #     list_of_cells = []
    #     for cell in row.findAll('td'):
    #         text = cell.txt.replace('&nbsp;', '')
    #         list_of_cells.append(text)
    #     list_of_rows.append(list_of_cells)
    # output_file = open('./output/' + nfl_position + '.csv', 'wb')
    # writer = csv.writer(output_file)
    # writer.writerows(list_of_rows)
