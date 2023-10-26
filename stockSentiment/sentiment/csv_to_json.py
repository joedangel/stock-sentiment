import csv
import json

# Create an empty dictionary to store the data
result = {}

# Open the CSV file and read its content
with open('Stocks Sentiment Scores Oct-Dec GSHeet.csv', 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    
    # Get the header
    header = next(csvreader)
    
    # Indices for date and price columns in the CSV file
    date_indices = range(5, len(header))
    
    # Iterate through each row in the CSV file
    for row in csvreader:
        
        # Extract the symbol and relevant information
        symbol = row[0]
        
        # Initialize an empty list to store date and price data for this symbol
        symbol_data = []
        
        # Iterate through each date and corresponding price
        for i in date_indices:
            
            # Create a dictionary for this date
            date_data = {
                "Date": header[i],
                "Score": int(row[i])
            }
            
            # Append this date data to the list of date data for this symbol
            symbol_data.append(date_data)
        
        # Add this symbol and its date data to the result
        result[symbol] = symbol_data

# Convert the dictionary to a JSON string
json_str = json.dumps(result, indent=4)

# Save the JSON string to a file
with open('output.json', 'w') as jsonfile:
    jsonfile.write(json_str)

# Or if you want to print the JSON string
# print(json_str)