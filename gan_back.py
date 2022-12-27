import csv



data = open('./demo_trades.csv')



csvreader = csv.reader(data)



header = []

header = next(csvreader)



stocks = {}

worth = {}



rows = []



for row in csvreader:

    rows.append(row)



header_new = ['OPEN_TIME', 'CLOSE_TIME', 'SYMBOL', 'QUANTITY', 'PNL', 'OPEN_SIDE', 'CLOSE_SIDE', 'OPEN_PRICE', 'CLOSED_PRICE']



rows_new = []



for row in rows:

    if(row[2] == 'B'):

        if row[1] not in stocks.keys():

            stocks[row[1]] = [[row[0], float(row[3]), int(row[4])]]

            worth[row[1]] = [float(row[3]) * int(row[4]), int(row[4])]

        else:

            stocks[row[1]].append([row[0], float(row[3]), int(row[4])])

            worth[row[1]][0] = worth[row[1]][0] + (float(row[3]) * int(row[4]))

            worth[row[1]][1] = worth[row[1]][1] + int(row[4])

            

    if(row[2] == 'S'):

        row_temp = []

        flag = -1

        

        openT, closeT, qty, pnl, openP, closeP

        

        sell = int(row[4])

        

        if(sell == worth[row[1]][1]):

            flag = 0

            

            openT = stocks[row[1]][0][0], closeT = row[0], qty = int(row[4])

            pnl = (float(row[3]) * int(row[4])) - worth[row[1]][0]

            openP = float(stocks[row[1]][0][3])

            closeP = float(row[3])

            

        else if(sell < inventory[row[1]]):

            flag = 1

            

            openT = stocks[row[1]][0][0], qty = min(sell, inventory[row[1]]), openP = float(stocks[row[1]][0][3])

            

            

        