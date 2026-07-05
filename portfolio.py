def main():
    # Key concept: dictionary (hardcoded stock prices)
    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "GOOGL": 140.0,
        "AMZN": 130.0,
        "MSFT": 330.0
    }
    
    portfolio = {}
    total_investment = 0.0
    
    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks to track:", ", ".join(stock_prices.keys()))
    
    while True:
        # Key concept: input/output
        stock_name = input("\nEnter the stock ticker (or type 'done' to finish): ").upper().strip()
        
        if stock_name == 'DONE':
            break
            
        if stock_name not in stock_prices:
            print(f"Sorry, {stock_name} is not in our database. Please choose from: {', '.join(stock_prices.keys())}")
            continue
            
        try:
            quantity = float(input(f"Enter the quantity of {stock_name} shares: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
                
            # Store in portfolio
            if stock_name in portfolio:
                portfolio[stock_name] += quantity
            else:
                portfolio[stock_name] = quantity
                
        except ValueError:
            print("Invalid input. Please enter a numerical value for quantity.")
            
    print("\n--- Portfolio Summary ---")
    
    # Calculate and display total
    for ticker, qty in portfolio.items():
        price = stock_prices[ticker]
        # Key concept: basic arithmetic
        value = price * qty
        total_investment += value
        print(f"{ticker}: {qty} shares @ ${price:.2f} = ${value:.2f}")
        
    print("-" * 25)
    print(f"Total Investment Value: ${total_investment:.2f}")
    
    # Key concept: file handling (optional)
    save_option = input("\nWould you like to save this summary to a file? (yes/no): ").lower().strip()
    if save_option in ['yes', 'y']:
        filename = "portfolio_summary.txt"
        try:
            with open(filename, 'w') as file:
                file.write("--- Portfolio Summary ---\n")
                for ticker, qty in portfolio.items():
                    price = stock_prices[ticker]
                    value = price * qty
                    file.write(f"{ticker}: {qty} shares @ ${price:.2f} = ${value:.2f}\n")
                file.write("-" * 25 + "\n")
                file.write(f"Total Investment Value: ${total_investment:.2f}\n")
            print(f"Summary successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving to file: {e}")

if __name__ == "__main__":
    main()
