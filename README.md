# PyCap V0.2
# A simple python CLI using Click with Coinmarketcap's API.


API Keys can be obtained from the link below.

sandbox = https://sandbox.coinmarketcap.com/
live = https://pro.coinmarketcap.com/

sandbox/live API keys are NOT interchangable.

Can be changed to the sandbox version by changing \_\_base in api.py. Please reference the documents on instructions on how to do this.

https://pro.coinmarketcap.com/api/v1#section/Quick-Start-Guide

# Installation

First, clone this repository and open up the directory in a terminal.

API_KEY can be exported by running "export API_KEY='include-the-(')'" in the terminal.

Run 'pip install --editable .' (<--- dont forget the period) and this should install the script in the virtual enviroment.

# Usage

commands : price | portoflio | btc | update

Supported Currency Codes are here: https://pro.coinmarketcap.com/api/v1#section/Standards-and-Conventions

## btc

prints price of btc

'pycap btc' -> {'btc': '6580.44960555'}

## price

'pycap price ada' -> [{'Cardano': '0.00001529'}]

price also supports different currencies as well as chaining mulitple coins.

'pycap price --curr=usd ada hot' -> [{'Cardano': '0.09934988'}, {'Holo': '0.00060517'}]

--curr=XYZ where XYZ is the currency code.

## update

pycap update allows you to add coins to your porfolio

## portfolio

please edit the portfolio.json with your own balances.

Format is {"symbol": units}

'pycap portfolio' -> {'btc': 649.302288075, 'ada': 99349.88, 'iotx': 218.7848, 'hot': 6051.700000000001}

you can also get the sum of total balance by doing

'pycap portfolio --total=y' -> $106269.667088075

Like with price, --curr option is supported

'pycap portfolio --curr=jpy' -> {'btc': 71885.40007175, 'ada': 10999200.22, 'iotx': 24222.056200000003, 'hot': 669992.7}

'pycap portfolio --curr=jpy --total=y' -> ¥11765300.376271749
