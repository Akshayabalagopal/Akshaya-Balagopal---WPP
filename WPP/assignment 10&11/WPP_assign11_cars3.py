import pandas as pd

def find_good_deals():
    num_cars = int(input("Enter the number of cars: "))

    asking_prices = []
    fair_prices = []

    for i in range(num_cars):
        asking_price = float(input(f"Enter the asking price for car {i+1}: "))
        fair_price = float(input(f"Enter the fair price for car {i+1}: "))
        asking_prices.append(asking_price)
        fair_prices.append(fair_price)

    asking_prices_series = pd.Series(asking_prices)
    fair_prices_series = pd.Series(fair_prices)
 
    good_deals = asking_prices_series < fair_prices_series
  
    good_deal_indices = good_deals[good_deals].index.tolist()
    
    if good_deal_indices:
        print("\nGood deals are available at the following car indices (0-based):", good_deal_indices)
    else:
        print("\nNo good deals found.")

find_good_deals()
