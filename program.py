# Group members for this exercise are Daniel Cisneros, 
# Dene Logan, Ricky Sequera, and Joseph Onghena.

# This program gets the URL of UNC Charlotte and prints the HTML within it.

import requests

r = requests.get('https://www.charlotte.edu/')
print(r.text)