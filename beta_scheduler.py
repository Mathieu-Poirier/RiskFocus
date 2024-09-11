import yfinance as yf
import schedule
import time
import sys

ticker_search = input("Please input the ticker you want to calculate beta for: ")

def update_ticker_object():
  update_ticker_object.stock_result = yf.Ticker(ticker_search)
  update_ticker_object.market_benchmark = yf.Ticker("SPY")

update_ticker_object.stock_result = yf.Ticker(ticker_search)
update_ticker_object.market_benchmark = yf.Ticker("SPY")

def update_close_prices():
  update_close_prices.stock_last_close_price = float((str(update_ticker_object.stock_result.history(period="1d")['Close']).split(' ')[5])[0:10]) 
  update_close_prices.market_last_close_price = float((str(update_ticker_object.market_benchmark.history(period="1d")['Close']).split(' ')[5])[0:10]) 

update_close_prices.stock_last_close_price = 0.0
update_close_prices.market_last_close_price = 0.0

def save_close_prices():
  save_close_prices.market_price_list.append(update_close_prices.market_last_close_price)
  save_close_prices.stock_price_list.append(update_close_prices.stock_last_close_price)

save_close_prices.market_price_list = []
save_close_prices.stock_price_list = []

def calculate_means():
 calculate_means.mean_daily_market_price = sum(save_close_prices.market_price_list) / len(save_close_prices.market_price_list)
 calculate_means.mean_daily_stock_price = sum(save_close_prices.stock_price_list) / len(save_close_prices.stock_price_list)

calculate_means.mean_daily_market_price = 0.0
calculate_means.mean_daily_stock_price = 0.0

def calculate_beta():
  calculate_beta.covariance = (update_close_prices.market_last_close_price - calculate_means.mean_daily_market_price) * (update_close_prices.stock_last_close_price - calculate_means.mean_daily_stock_price) / (len(save_close_prices.market_price_list) - 1)
  calculate_beta.variance = ((update_close_prices.market_last_close_price - calculate_means.mean_daily_market_price) ** 2) / (len(save_close_prices.market_price_list) - 1)
  calculate_beta.calculated_beta = calculate_beta.covariance / calculate_beta.variance
  return calculate_beta.calculated_beta 

# print(update_ticker_object.stock_result.info.get('beta')) = get ticker beta from Yahoo

def compare_beta():

  try:
    update_ticker_object()
  except:
    print("Enter a valid ticker symbol")
    print("Exiting program...")
    sys.exit(1)
    
  update_close_prices()
  save_close_prices()

  if(len(save_close_prices.market_price_list) > 2):
    calculate_means()
    risk_focus_beta = calculate_beta()
    yahoo_finance_beta = update_ticker_object.stock_result.info.get('beta')

    print(f"The beta we calculated: {risk_focus_beta}")
    print(f"Yahoo finances current beta: {yahoo_finance_beta}")
    if yahoo_finance_beta is not None and yahoo_finance_beta != 0:
          bias_factor = yahoo_finance_beta / risk_focus_beta
          print(f"Suggested bias factor: {bias_factor}")
    else:
          print("No beta data available from Yahoo Finance")

  else:
  
    print("OK: Gathering data points...")


schedule.every().day.at("09:31").do(compare_beta)

while True:
    schedule.run_pending()
    time.sleep(1)


