import yahoostockquote as yquote
print yquote.get_price('GOOG')
yquote.get_historical_prices('GOOG','20131004','20131007')

# Using Pandas IO
import pandas.io.data as web
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 01, 27)
gdp=web.DataReader("GDP", "fred", start, end)
gdp.ix['2013-01-01']