# This is my Stock Simulator Major
# Scrapes data from yahoo finance allowing for real time stock price simulation
# Portfolio has 25000$ to start with

# Imports
import csv  # I've used import csv to format my stock prices
import os.path  # I am using import os path for checking if a file exists, getting the absolute path of a file.
import webbrowser  # Using this for displaying my web based documents, hoping to use it for yahoo finance
from datetime import datetime, date, timedelta  # This was recommended to me for easily managing my dates and times

import matplotlib.pyplot as plt  # Hoping this will allow me to display graphs of the price going up and down
import pandas as pd  # For managing my 2-d and 1-d data
import requests  # This is used, so I don't have to add query requests at the end of yahoo URL
import yfinance as yf  #
from bs4 import BeautifulSoup  #

