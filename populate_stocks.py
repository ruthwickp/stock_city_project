import os
import ystockquote
import time

def populate():
    """ Populates the database with the companies entered. """
    companies = get_companies_symbol()

    # Gets current date and last year's dates
    current_time = time.strftime('%Y-%m-%d')
    last_year = str(int(time.strftime('%Y')) - 1) + time.strftime('-%m-%d')

    # Adds stock to database
    for stock in companies:
        print stock
        Stock.objects.get_or_create(
            symbol=stock,
            name=ystockquote.get_company_name(stock)[1:-1],
            historical_prices=ystockquote.get_historical_prices(
                stock, last_year, current_time))

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
