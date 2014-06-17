import os
import ystockquote

def populate():
    """ Populates the database with the companies entered. """
    companies = get_companies_symbol()

    # Adds stock to database
    for stock in companies:

        print stock
        Stock.objects.get_or_create(
            symbol=stock,
            name=ystockquote.get_company_name(stock),
            historical_prices=ystockquote.get_historical_prices(
                stock, '2013-01-01', '2014-01-01'))

def get_companies_symbol():
    """ Reads a file and returns the list of symbols of the companies
    in it. """
    # Loads stocks from text file and returns the company symbols
    stock_file = open('stock_list.txt', 'r')
    company_list = [company.strip() for company in stock_file]
    stock_file.close()
    return company_list

# If the program is run alone
if __name__ == '__main__':
    print "Starting stock script...."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_city_project.settings')

    # Populates the database with stocks
    from stocks.models import Stock
    populate()
