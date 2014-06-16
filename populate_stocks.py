import os
import ystockquote

def populate():
    """ Populates the database with the companies entered. """

    companies = get_companies_symbol()

    for stock in companies:
        # Retrieves property for each stock
        properties = get_stock_properties(stock)

        # Calls method to add stock to database
        add_stock(symbol=properties['symbol'], 
            name=properties['name'],
            ask_realtime=properties['ask_realtime'], 
            todays_range=properties['todays_range'], 
            volume=properties['volume'])


def add_stock(symbol, name, ask_realtime, todays_range, volume):
    """ Adds a stock to the database containing argument specific 
    information. """
    Stock.objects.get_or_create(symbol=symbol, name=name, ask_realtime=ask_realtime,
        todays_range=todays_range, volume=volume)


def get_stock_properties(stock):
    """ Returns a dictionary containing properties for a given stock 
    using the ystockquote API. """
    properties = {}
    properties['symbol'] = stock
    properties['name'] = ystockquote.get_company_name(stock)
    properties['ask_realtime'] = float(ystockquote.get_ask_realtime(stock))
    properties['todays_range'] = ystockquote.get_todays_range(stock)
    properties['volume'] = float(ystockquote.get_volume(stock))
    return properties

def get_companies_symbol():
    """ Reads a file and returns the list of symbols of the companies
    in it. """
    # NYSE.txt contains both symbols and company names in one line
    stock_file = open('NYSE.txt', 'r')
    company_list = []

    # Reads each line and adds symbol to company_list
    for company in stock_file:
        symbol = company[:company.find('\t')]
        company_list.append(symbol)

    # Closes file and returns company symbols
    stock_file.close()
    return company_list[1:]


# If the program is run alone
if __name__ == '__main__':
    print "Starting stock script...."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_city_project.settings')

    # Populates the database with stocks
    from stocks.models import Stock
    populate()
