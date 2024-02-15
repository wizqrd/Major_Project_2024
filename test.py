# Setting display options for the simulator
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

today = date.today()

portfolio_value = 25000  # Starting amount that one gets to invest

# Backend control mechanism to aid in calculations later on
money_change_long = 0
money_change_short = 0

c = 0  # To know which iteration of the simulator we're in
break_to_main_menu = 0  # Used to break between loops
exit_short_to_main_menu = 0
exit_long_to_main_menu = 0

exit_initial_choice = 0

# Will now define lists for the variables that we'd like to scrape
# Creating separate lists for each industry as I'm not too confident with creation of manual functions :/

# For industry choice 1 - Energy
prices1 = []
tickers1 = []
names1 = []
changes1 = []
percentChanges1 = []
marketCaps1 = []
totalVolumes1 = []

# Web-scraping
EnergyUrl = "https://sg.finance.yahoo.com/industries/energy"
r = requests.get(EnergyUrl)
data = r.text
soup = BeautifulSoup(data, features="lxml")

counter = 40
for i in range(40, 404, 14):
    for listing in soup.find_all('tr'):
        for ticker in listing.find_all('td', attrs={'aria-label': 'Symbol'}):
            tickers1.append(ticker.text)
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names1.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Last price'}):
            prices1.append(price.text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes1.append(change.text)
        for pchange in listing.find_all('td', attrs={'aria-label': '% change'}):
            percentChanges1.append(pchange.text)
        for cap in listing.find_all('td', attrs={'aria-label': 'Market cap'}):
            marketCaps1.append(cap.text)
        for volume in listing.find_all('td', attrs={'aria-label': 'Volume'}):
            totalVolumes1.append(volume.text)

# We'll now repeat this for all 12 industries

# For industry choice 2 - Financial Services
prices2 = []
tickers2 = []
names2 = []
changes2 = []
percentChanges2 = []
marketCaps2 = []
totalVolumes2 = []

FinancialUrl = "https://sg.finance.yahoo.com/industries/financial"
r = requests.get(FinancialUrl)
data = r.text
soup = BeautifulSoup(data, features="lxml")

counter = 40
for i in range(40, 404, 14):
    for listing in soup.find_all('tr'):
        for ticker in listing.find_all('td', attrs={'aria-label': 'Symbol'}):
            tickers2.append(ticker.text)
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names2.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Last price'}):
            prices2.append(price.text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes2.append(change.text)
        for pchange in listing.find_all('td', attrs={'aria-label': '% change'}):
            percentChanges2.append(pchange.text)
        for cap in listing.find_all('td', attrs={'aria-label': 'Market cap'}):
            marketCaps2.append(cap.text)
        for volume in listing.find_all('td', attrs={'aria-label': 'Volume'}):
            totalVolumes2.append(volume.text)

# For industry choice 3 - Healthcare
prices3 = []
tickers3 = []
names3 = []
changes3 = []
percentChanges3 = []
marketCaps3 = []
totalVolumes3 = []

HealthUrl = "https://sg.finance.yahoo.com/industries/healthcare"
r = requests.get(HealthUrl)
data = r.text
soup = BeautifulSoup(data, features="lxml")

counter = 40
for i in range(40, 404, 14):
    for listing in soup.find_all('tr'):
        for ticker in listing.find_all('td', attrs={'aria-label': 'Symbol'}):
            tickers3.append(ticker.text)
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names3.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Last price'}):
            prices3.append(price.text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes3.append(change.text)
        for pchange in listing.find_all('td', attrs={'aria-label': '% change'}):
            percentChanges3.append(pchange.text)
        for cap in listing.find_all('td', attrs={'aria-label': 'Market cap'}):
            marketCaps3.append(cap.text)
        for volume in listing.find_all('td', attrs={'aria-label': 'Volume'}):
            totalVolumes3.append(volume.text)

# For industry choice 4 - Business Services
prices4 = []
tickers4 = []
names4 = []
changes4 = []
percentChanges4 = []
marketCaps4 = []
totalVolumes4 = []

bizUrl = "https://sg.finance.yahoo.com/industries/business_services"
r = requests.get(bizUrl)
data = r.text
soup = BeautifulSoup(data, features="lxml")

counter = 40
for i in range(40, 404, 14):
    for listing in soup.find_all('tr'):
        for ticker in listing.find_all('td', attrs={'aria-label': 'Symbol'}):
            tickers4.append(ticker.text)
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names4.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Last price'}):
            prices4.append(price.text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes4.append(change.text)
        for pchange in listing.find_all('td', attrs={'aria-label': '% change'}):
            percentChanges4.append(pchange.text)
        for cap in listing.find_all('td', attrs={'aria-label': 'Market cap'}):
            marketCaps4.append(cap.text)
        for volume in listing.find_all('td', attrs={'aria-label': 'Volume'}):
            totalVolumes4.append(volume.text)

# For industry choice 5 - Telecoms & Utilities
prices5 = []
tickers5 = []
names5 = []
changes5 = []
percentChanges5 = []
marketCaps5 = []
totalVolumes5 = []

TelcoUrl = "https://sg.finance.yahoo.com/industries/telecom_utilities"
r = requests.get(TelcoUrl)
data = r.text
soup = BeautifulSoup(data, features="lxml")

counter = 40
for i in range(40, 404, 14):
    for listing in soup.find_all('tr'):
        for ticker in listing.find_all('td', attrs={'aria-label': 'Symbol'}):
            tickers5.append(ticker.text)
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names5.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Last price'}):
            prices5.append(price.text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes5.append(change.text)
        for pchange in listing.find_all('td', attrs={'aria-label': '% change'}):
            percentChanges5.append(pchange.text)
        for cap in listing.find_all('td', attrs={'aria-label': 'Market cap'}):
            marketCaps5.append(cap.text)
        for volume in listing.find_all('td', attrs={'aria-label': 'Volume'}):
            totalVolumes5.append(volume.text)

# For industry choice 6 - Computer Hardware & Electronics
prices6 = []
tickers6 = []
names6 = []
changes6 = []
percentChanges6 = []
marketCaps6 = []
totalVolumes6 = []

HWEUrl = "https://sg.finance.yahoo.com/industries/hardware_electronics"
r = requests.get(HWEUrl)
data = r.text
soup = BeautifulSoup(data, features="lxml")

counter = 40
for i in range(40, 404, 14):
    for listing in soup.find_all('tr'):
        for ticker in listing.find_all('td', attrs={'aria-label': 'Symbol'}):
            tickers6.append(ticker.text)
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names6.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Last price'}):
            prices6.append(price.text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes6.append(change.text)
        for pchange in listing.find_all('td', attrs={'aria-label': '% change'}):
            percentChanges6.append(pchange.text)
        for cap in listing.find_all('td', attrs={'aria-label': 'Market cap'}):
            marketCaps6.append(cap.text)
        for volume in listing.find_all('td', attrs={'aria-label': 'Volume'}):
            totalVolumes6.append(volume.text)

# For industry choice 7 - Computer Software & Services
prices7 = []
tickers7 = []
names7 = []
changes7 = []
percentChanges7 = []
marketCaps7 = []
totalVolumes7 = []

CSSUrl = "https://sg.finance.yahoo.com/industries/software_services"
r = requests.get(CSSUrl)
data = r.text
soup = BeautifulSoup(data, features="lxml")

counter = 40
for i in range(40, 404, 14):
    for listing in soup.find_all('tr'):
        for ticker in listing.find_all('td', attrs={'aria-label': 'Symbol'}):
            tickers7.append(ticker.text)
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names7.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Last price'}):
            prices7.append(price.text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes7.append(change.text)
        for pchange in listing.find_all('td', attrs={'aria-label': '% change'}):
            percentChanges7.append(pchange.text)
        for cap in listing.find_all('td', attrs={'aria-label': 'Market cap'}):
            marketCaps7.append(cap.text)
        for volume in listing.find_all('td', attrs={'aria-label': 'Volume'}):
            totalVolumes7.append(volume.text)

# For industry choice 8 - Manufacturing & Materials
prices8 = []
tickers8 = []
names8 = []
changes8 = []
percentChanges8 = []
marketCaps8 = []
totalVolumes8 = []

ManuUrl = "https://sg.finance.yahoo.com/industries/manufacturing_materials"
r = requests.get(ManuUrl)
data = r.text
soup = BeautifulSoup(data, features="lxml")

counter = 40
for i in range(40, 404, 14):
    for listing in soup.find_all('tr'):
        for ticker in listing.find_all('td', attrs={'aria-label': 'Symbol'}):
            tickers8.append(ticker.text)
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names8.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Last price'}):
            prices8.append(price.text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes8.append(change.text)
        for pchange in listing.find_all('td', attrs={'aria-label': '% change'}):
            percentChanges8.append(pchange.text)
        for cap in listing.find_all('td', attrs={'aria-label': 'Market cap'}):
            marketCaps8.append(cap.text)
        for volume in listing.find_all('td', attrs={'aria-label': 'Volume'}):
            totalVolumes8.append(volume.text)

# For industry choice 9 - Consumer Products & Media
prices9 = []
tickers9 = []
names9 = []
changes9 = []
percentChanges9 = []
marketCaps9 = []
totalVolumes9 = []

CPMUrl = "https://sg.finance.yahoo.com/industries/consumer_products_media"
r = requests.get(CPMUrl)
data = r.text
soup = BeautifulSoup(data, features="lxml")

counter = 40
for i in range(40, 404, 14):
    for listing in soup.find_all('tr'):
        for ticker in listing.find_all('td', attrs={'aria-label': 'Symbol'}):
            tickers9.append(ticker.text)
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names9.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Last price'}):
            prices9.append(price.text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes9.append(change.text)
        for pchange in listing.find_all('td', attrs={'aria-label': '% change'}):
            percentChanges9.append(pchange.text)
        for cap in listing.find_all('td', attrs={'aria-label': 'Market cap'}):
            marketCaps9.append(cap.text)
        for volume in listing.find_all('td', attrs={'aria-label': 'Volume'}):
            totalVolumes9.append(volume.text)

# For industry choice 10 - Industrials
prices10 = []
tickers10 = []
names10 = []
changes10 = []
percentChanges10 = []
marketCaps10 = []
totalVolumes10 = []

IndUrl = "https://sg.finance.yahoo.com/industries/industrials"
r = requests.get(IndUrl)
data = r.text
soup = BeautifulSoup(data, features="lxml")

counter = 40
for i in range(40, 404, 14):
    for listing in soup.find_all('tr'):
        for ticker in listing.find_all('td', attrs={'aria-label': 'Symbol'}):
            tickers10.append(ticker.text)
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names10.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Last price'}):
            prices10.append(price.text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes10.append(change.text)
        for pchange in listing.find_all('td', attrs={'aria-label': '% change'}):
            percentChanges10.append(pchange.text)
        for cap in listing.find_all('td', attrs={'aria-label': 'Market cap'}):
            marketCaps10.append(cap.text)
        for volume in listing.find_all('td', attrs={'aria-label': 'Volume'}):
            totalVolumes10.append(volume.text)

# For industry choice 11 - Diversified Businesses
prices11 = []
tickers11 = []
names11 = []
changes11 = []
percentChanges11 = []
marketCaps11 = []
totalVolumes11 = []

DivBizUrl = "https://sg.finance.yahoo.com/industries/diversified_business"
r = requests.get(DivBizUrl)
data = r.text
soup = BeautifulSoup(data, features="lxml")

counter = 40
for i in range(40, 404, 14):
    for listing in soup.find_all('tr'):
        for ticker in listing.find_all('td', attrs={'aria-label': 'Symbol'}):
            tickers11.append(ticker.text)
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names11.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Last price'}):
            prices11.append(price.text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes11.append(change.text)
        for pchange in listing.find_all('td', attrs={'aria-label': '% change'}):
            percentChanges11.append(pchange.text)
        for cap in listing.find_all('td', attrs={'aria-label': 'Market cap'}):
            marketCaps11.append(cap.text)
        for volume in listing.find_all('td', attrs={'aria-label': 'Volume'}):
            totalVolumes11.append(volume.text)

# For industry choice 12 - Retail & Hospitality
prices12 = []
tickers12 = []
names12 = []
changes12 = []
percentChanges12 = []
marketCaps12 = []
totalVolumes12 = []

RetHosUrl = "https://sg.finance.yahoo.com/industries/retailing_hospitality"
r = requests.get(RetHosUrl)
data = r.text
soup = BeautifulSoup(data, features="lxml")

counter = 40
for i in range(40, 404, 14):
    for listing in soup.find_all('tr'):
        for ticker in listing.find_all('td', attrs={'aria-label': 'Symbol'}):
            tickers12.append(ticker.text)
        for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
            names12.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label': 'Last price'}):
            prices12.append(price.text)
        for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
            changes12.append(change.text)
        for pchange in listing.find_all('td', attrs={'aria-label': '% change'}):
            percentChanges12.append(pchange.text)
        for cap in listing.find_all('td', attrs={'aria-label': 'Market cap'}):
            marketCaps12.append(cap.text)
        for volume in listing.find_all('td', attrs={'aria-label': 'Volume'}):
            totalVolumes12.append(volume.text)

# Creating a consolidated list of stock details, to facilitate choosing stocks directly via inputing the specific
prices_all = prices1 + prices2 + prices3 + prices4 + prices5 + prices6 + prices7 + prices8 + prices9 + prices10 + prices11 + prices12
tickers_all = tickers1 + tickers2 + tickers3 + tickers4 + tickers5 + tickers6 + tickers7 + tickers8 + tickers9 + tickers10 + tickers11 + tickers12
names_all = names1 + names2 + names3 + names4 + names5 + names6 + names7 + names8 + names9 + names10 + names11 + names12
changes_all = changes1 + changes2 + changes3 + changes4 + changes5 + changes6 + changes7 + changes8 + changes9 + changes10 + changes11 + changes12
percentChanges_all = percentChanges1 + percentChanges2 + percentChanges3 + percentChanges4 + percentChanges5 + percentChanges6 + percentChanges7 + percentChanges8 + percentChanges9 + percentChanges10 + percentChanges11 + percentChanges12
marketCaps_all = marketCaps1 + marketCaps2 + marketCaps3 + marketCaps4 + marketCaps5 + marketCaps6 + marketCaps7 + marketCaps8 + marketCaps9 + marketCaps10 + marketCaps11 + marketCaps12
totalVolumes_all = totalVolumes1 + totalVolumes2 + totalVolumes3 + totalVolumes4 + totalVolumes5 + totalVolumes6 + totalVolumes7 + totalVolumes8 + totalVolumes9 + totalVolumes10 + totalVolumes11 + totalVolumes12

# Transforming from list format to dataframe format
complete_list = pd.DataFrame({"Ticker": tickers_all,
                              "Name": names_all,
                              "Price": prices_all,
                              "Market Cap": marketCaps_all})

complete_list = complete_list[complete_list.Price != "N/A"]
complete_list.drop_duplicates(inplace=True, ignore_index=True)

# The simulator itself
while True:
    try:
        initial = input("""Would you like to browse stocks by industry, or do you have a specific stock ticker you'd like to look at?
[I] - Browse by Industry
[S] - Specific Stock Ticker: """).upper()

        if initial == "I":
            while True:
                try:
                    industry = int(input("""Which industry would you like to look at?
[1] - Energy
[2] - Financial Services
[3] - Healthcare
[4] - Business Services
[5] - Telecoms & Utilities
[6] - Computer Hardware & Electronics
[7] - Computer Software & Services
[8] - Manufacturing & Materials
[9] - Consumer Products & Media
[10] - Industrials
[11] - Diversified Businesses
[12] - Retail & Hospitality: """))

                    if industry == 1:

                        list_of_companies = pd.DataFrame({"Ticker": tickers1,
                                                          "Name": names1,
                                                          "Price": prices1,
                                                          "Market Cap": marketCaps1})

                        list_of_companies = list_of_companies[list_of_companies.Price != 'N/A']
                        list_of_companies.drop_duplicates(inplace=True, ignore_index=True)

                        print()
                        print(list_of_companies)

                        while True:
                            try:
                                company = input("Please enter the ticker of the company you'd like to see: ").upper()

                                # Earlier we got data about basic stock information for each industry
                                # We now use the yfinance library to ensure that the stock ticker information is entered correctly, and to get datelise stock information (Price, volume, daily highs/lows etc.)

                                df_yahoo = yf.download(company,
                                                       start='2024-01-01',
                                                       end='2024-02-11',
                                                       progress=False)
                                df_yahoo = df_yahoo.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1)

                                # If ticker is entered incorrectly here, this next block of code will flag it out
                                if df_yahoo.empty == True:
                                    print()
                                    raise Exception("Please recheck the ticker!")
                                    continue
                                # Improvement needed here: Try to ensure that there is nothing printed (Failed download etc) when ticker is incorrectly entered

                                elif company not in list_of_companies.values:
                                    print(
                                        "Please enter a ticker from the list of companies provided above, or select a different industry")

                                else:
                                    print(
                                        f"You have chosen {list_of_companies[list_of_companies.Ticker == company].loc[:, 'Name']}")

                                    confirm = input("""Would you now like to proceed to the simulator?
[Y] - Yes
[N] - No: """).upper()
                                    if confirm == "Y":
                                        break_to_main_menu = 1
                                        break

                                    elif confirm == "N":
                                        continue

                            except:
                                print(
                                    "** There is no data on this ticker. The server may not possess it, or you may have entered an incorrect ticker. Please recheck **")

                    # We repeat the same code block for each industry - Again, a custom function may be more efficient

                    elif industry == 2:

                        list_of_companies = pd.DataFrame({"Ticker": tickers2,
                                                          "Name": names2,
                                                          "Price": prices2,
                                                          "Market Cap": marketCaps2})

                        list_of_companies = list_of_companies[list_of_companies.Price != 'N/A']
                        list_of_companies.drop_duplicates(inplace=True, ignore_index=True)

                        print()
                        print(list_of_companies)

                        while True:
                            try:
                                company = input("Please enter the ticker of the company you'd like to see: ").upper()

                                df_yahoo = yf.download(company,
                                                       start='2015-01-01',
                                                       end='2015-01-02',
                                                       progress=False)
                                df_yahoo = df_yahoo.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1)

                                if df_yahoo.empty == True:
                                    print()
                                    raise Exception("Please recheck the ticker!")
                                    continue

                                elif company not in list_of_companies.values:
                                    print(
                                        "Please enter a ticker from the list of companies provided above, or select a different industry")

                                else:
                                    print(
                                        f"You have chosen {list_of_companies[list_of_companies.Ticker == company].loc[:, 'Name']}")

                                    confirm = input("""Would you now like to proceed to the simulator?
[Y] - Yes
[N] - No: """).upper()
                                    if confirm == "Y":
                                        break_to_main_menu = 1
                                        break

                                    elif confirm == "N":
                                        continue

                            except:
                                print(
                                    "** There is no data on this ticker. The server may not possess it, or you may have entered an incorrect ticker. Please recheck **")

                    elif industry == 3:

                        list_of_companies = pd.DataFrame({"Ticker": tickers3,
                                                          "Name": names3,
                                                          "Price": prices3,
                                                          "Market Cap": marketCaps3})

                        list_of_companies = list_of_companies[list_of_companies.Price != 'N/A']
                        list_of_companies.drop_duplicates(inplace=True, ignore_index=True)

                        print()
                        print(list_of_companies)

                        while True:
                            try:
                                company = input("Please enter the ticker of the company you'd like to see: ").upper()

                                df_yahoo = yf.download(company,
                                                       start='2024-01-01',
                                                       end='2024-02-11',
                                                       progress=False)
                                df_yahoo = df_yahoo.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1)

                                if df_yahoo.empty == True:
                                    print()
                                    raise Exception("Please recheck the ticker!")
                                    continue

                                elif company not in list_of_companies.values:
                                    print(
                                        "Please enter a ticker from the list of companies provided above, or select a different industry")

                                else:
                                    print(
                                        f"You have chosen {list_of_companies[list_of_companies.Ticker == company].loc[:, 'Name']}")

                                    confirm = input("""Would you now like to proceed to the simulator?
[Y] - Yes
[N] - No: """).upper()
