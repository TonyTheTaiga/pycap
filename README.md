# PyCap V0.1

A simple command line application to check crypto prices in terminal

## Pre-reqs

**Mac**

**A coinmartketcap API Key ((FREEEEEEE))**

**This app uses the SANDBOX API but can easily be changed to the live version. Please check the link below for information on how to do that**

https://pro.coinmarketcap.com/api/v1#section/Quick-Start-Guide

## Installation

As of now you can only run this in a virtual enviroment.

First, clone this repository and open up the directory in a terminal.

Then, run 'python3 -m venv env'.

Now, start the virtual enviroment by running 'source env/bin/activate'.

Your terminal should now look like something like '(env) dir_name $ '.

Next, your going to need to export your API KEY or update the config.py file.
API key can be easily exported by running export API='your-api-key' after venv is running.

After this, run 'pip install --editable .' and this should install the script in the virtual enviroment.

## Usage

commands supported are [price, portfolio]

**price**

'pycap price ada' -> [{'Cardano': '0.00001529'}]

price also supports different currencies as well as chaining mulitple coins.

'pycap price --curr=usd ada hot' -> [{'Cardano': '0.09934988'}, {'Holo': '0.00060517'}]

--curr=xxx where xxx is the currency code

**portfolio**

please edit the portfolio.json with your own balances.

Format is {"symbol": units}

'pycap portfolio' -> {'btc': 649.302288075, 'ada': 99349.88, 'iotx': 218.7848, 'hot': 6051.700000000001}

you can also get the sum of total balance by doing

'pycap portfolio --total=y' -> $106269.667088075

Like with price, --curr option is supported

--curr=xxx where xxx is the currency code

'pycap portfolio --curr=jpy --total=y' -> {'btc': 71885.40007175, 'ada': 10999200.22, 'iotx': 24222.056200000003, 'hot': 669992.7}

'pycap portfolio --curr=jpy --total=y' -> ¥11765300.376271749
