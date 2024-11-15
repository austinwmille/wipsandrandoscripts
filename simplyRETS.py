# this script has a block of code missing from line 8

import requests
import csv
from requests.auth import HTTPBasicAuth

# Set your SimplyRETS credentials
AP..com/properties"

# Define search parameters for stale listings (e.g., listed for 30+ days)
params = {
    "daysOnMarket": 30,  # Adjust as needed
}

# Make the request
response = requests.get(URL, auth=HTTPBasicAuth(API_KEY, API_SECRET), params=params)

# Check for successful response
if response.status_code == 200:
    properties = response.json()
    
    # Open a CSV file to save the data
    with open('stale_listings.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header row
        writer.writerow(['Address', 'Price', 'Days on Market', 'URL'])
        
        # Write property data
        for property in properties:
            address = property.get('address', {}).get('full')
            price = property.get('listPrice')
            days_on_market = property.get('daysOnMarket')
            url = property.get('url')
            
            writer.writerow([address, price, days_on_market, url])
    
    print("Data has been saved to stale_listings.csv")
else:
    print("Failed to retrieve data:", response.status_code)