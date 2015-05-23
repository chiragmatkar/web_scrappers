#Script to Download Hitorical finacial data from Yahoo finance in a csv file
def make_url(ticker_symbol):
    return base_url + ticker_symbol

output_path = "C://Users/Chirag/Dropbox/Programming/chiragworkspace/web_scrapers"
def make_filename(ticker_symbol, directory="S&P"):
    return output_path + "/" + directory + "/" + ticker_symbol + ".csv"

def pull_historical_data(ticker_symbol, directory="S&P"):
    try:
        urllib.urlretrieve(make_url(ticker_symbol), make_filename(ticker_symbol, directory))
    except urllib.ContentTooShortError as e:
        outfile = open(make_filename(ticker_symbol, directory), "w")
        outfile.write(e.content)
        outfile.close()
		
		
if __name__ == '__main__':
			ticker=raw_input("Enter Ticker to pull out Data\n")
			make_url(ticker)
			make_filename(ticker)
			pull_historical_data(ticker)
