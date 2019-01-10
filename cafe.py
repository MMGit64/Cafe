menu = ['cappuccino', 'espresso', 'scone', 'muffin']

stockMenu_dict = {'cappuccino': '20',
              'espresso': '15',
              'scone': '18',
              'muffin': '20'}

priceMenu_dict = {'cappuccino': '2.20',
                  'espresso': '3.00',
                  'scone': '2.50',
                  'muffin': '1.30'}


menuStockValues = [stockMenu_dict['cappuccino'], stockMenu_dict['espresso'], stockMenu_dict['scone'], stockMenu_dict['muffin']]
menuStockValuesFloat = [float(element) for element in menuStockValues]


menuPriceValues = [priceMenu_dict['cappuccino'], priceMenu_dict['espresso'], priceMenu_dict['scone'], priceMenu_dict['muffin']]
menuPriceValuesFloat = [float(element) for element in menuPriceValues]


cappuccinoStockValue = menuStockValuesFloat[0]*menuPriceValuesFloat[0]
espressoStockValue = menuStockValuesFloat[1]*menuPriceValuesFloat[1]
sconeStockValue = menuStockValuesFloat[2]*menuPriceValuesFloat[2]
muffinStockValue = menuStockValuesFloat[3]*menuPriceValuesFloat[3]


totalCafeStockValue = [cappuccinoStockValue, espressoStockValue, sconeStockValue, muffinStockValue]

print sum(totalCafeStockValue)

                      

    
