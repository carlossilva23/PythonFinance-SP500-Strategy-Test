import fetch_data
import calculate_data
import backtest
import visualize

def main(): 
    portfolio =['EA', 'GRMN', 'GIS', 'VLO', 'GS', 'BSX', 'UBER', 'FSLR', 'ECL', 'IRM', 'PNW']
    portfolio_data = {}
    for stock in portfolio: 
        individual_data = fetch_data.fetch_stock(stock)
        calculate_data.calculate_short_MA(individual_data)
        calculate_data.calculate_long_MA(individual_data)
        calculated_data = calculate_data.crossover(individual_data)
        portfolio_data[stock] = calculated_data
        #backtest.simulate_portfolio(portfolio_data) 
main()



        