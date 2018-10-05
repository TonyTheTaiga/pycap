# PyCap V0.1

A simple command line application to check crypto prices in terminal

## Pre-reqs

Mac

Coinmarketcap's new API Key

**This app uses the SANDBOX API but can easily be changed to the live version. Please check the link below for information on how to do that**

https://pro.coinmarketcap.com/api/v1#section/Quick-Start-Guide

### Installation

As of now you can only run this can only be set up in a virtual enviroment.

First, clone this repository and open up the directory in a terminal.

Then, run 'python3 -m venv env'.

Now, start the virtual enviroment by running 'source env/bin/activate'.

Your terminal should now look like something like '(env) dir_name $ '.

Next, your going to need to export your API KEY or update the config.py file.
API key can be easily exported by running export API='your-api-key' after venv is running.

After this, run 'pip install --editable .' and this should install the script in the virtual enviroment.

## Usage

As of now (V0.1), the only command supported is price.

Basic layout = price [options][tickers]

'price ada' -> [{'Cardano': '0.00001529'}]

price also supports different currencies as well as chaining mulitple coins.

'price --curr=usd ada hot' -> [{'Cardano': '0.09934988'}, {'Holo': '0.00060517'}]

--curr=xxx where xxx is the currency code