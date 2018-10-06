# PyCap V0.1

A simple CLI using Click with Coinmarketcap's API.

## Pre-reqs

**TESTED ONLY ON A MAC**

Working on adding support for other OS's. Windows will not work as of now with how the API_KEY is exported, Linux might work.

**A coinmartketcap API Key**

Their public API v2 shuts down in December.

**Currently uses the sandbox site and not the pro site**

Can easily be changed by changing the \_\_base in api.py. Please reference the documents on instructions on how to do this.

https://pro.coinmarketcap.com/api/v1#section/Quick-Start-Guide

## Installation

**As of now, this only works in a virtual enviroment in the project directory**

First, clone this repository and open up the directory in a terminal.

Next, run 'python3 -m venv env'. this should work in python2 as well.

Now, start the virtual enviroment by running 'source env/bin/activate'.

Your terminal should now look like something like '(env) pycap $ '.

Next, your going to need to export your API_KEY or update the config.py file.
API_KEY can be easily exported by running export API_KEY='your-api-key' in the terminal.

Now run 'pip install --editable .' and this should install the script in the virtual enviroment.

# Usage

commands : [price, portfolio]

Supported Currency Codes are here: https://pro.coinmarketcap.com/api/v1#section/Standards-and-Conventions

## price

'pycap price ada' -> [{'Cardano': '0.00001529'}]

price also supports different currencies as well as chaining mulitple coins.

'pycap price --curr=usd ada hot' -> [{'Cardano': '0.09934988'}, {'Holo': '0.00060517'}]

--curr=XYZ where XYZ is the currency code. Check the link below for supported codes.

https://pro.coinmarketcap.com/api/v1#section/Standards-and-Conventions

## portfolio

please edit the portfolio.json with your own balances.

Format is {"symbol": units}

'pycap portfolio' -> {'btc': 649.302288075, 'ada': 99349.88, 'iotx': 218.7848, 'hot': 6051.700000000001}

you can also get the sum of total balance by doing

'pycap portfolio --total=y' -> $106269.667088075

Like with price, --curr option is supported

'pycap portfolio --curr=jpy' -> {'btc': 71885.40007175, 'ada': 10999200.22, 'iotx': 24222.056200000003, 'hot': 669992.7}

'pycap portfolio --curr=jpy --total=y' -> ¥11765300.376271749
