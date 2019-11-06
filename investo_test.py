from arctic import Arctic
import quandl

# Connect to Local MONGODB
store = Arctic('localhost',27017)

# Create the library - defaults to VersionStore
store.initialize_library('NASDAQ')

# Access the library
library = store['NASDAQ']

# Load some data - maybe from Quandl
aapl = quandl.get("WIKI/AAPL", authtoken="zhxQB5gTzGYTgYs7h7Us")

# Store the data in the library
library.write('AAPL', aapl, metadata={'source': 'Quandl'})

# Reading the data
item = library.read('AAPL')
print(item)
aapl = item.data
print(aapl)
metadata = item.metadata
