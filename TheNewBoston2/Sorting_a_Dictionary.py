stocks = {
    'GOOG': 520,
    'FB': 30,
    'YHOO': 100,
    'AAPL': 127,
    'AMZN':235
}
#code below changes dictionary to tuples and sorts smallest to highest
print(sorted(zip(stocks.keys(),stocks.values())))

#code below finds min. Notice i flip-flopped ".values()" and ".keys()
print(min(zip(stocks.values(),stocks.keys())))

#code below finds max
print(max(zip(stocks.values(),stocks.keys())))