# Ham Prefix API Lookup

This Python script (`ham_prefix_api.py`) is designed to query the HamNut API to retrieve detailed information about ham radio prefixes. Given a prefix (extracted from a callsign), it returns various details such as country name, CQ zone, ITU zone, continent, and more.

## Features

- **Prefix Lookup:** Given a ham radio callsign prefix, the script retrieves information about the associated country and radio zone details using the [HamNut API](https://api.hamnut.com/).
- **Standalone and Importable:** The script can be run on its own to look up a predefined ham radio prefix or can be imported into other Python scripts for use in larger projects.

## API Information

The script uses the following HamNut API endpoint:



```bash
GET https://api.hamnut.com/v1/call-signs/prefixes?prefix=<PREFIX>
```
This API returns detailed information about the given ham radio prefix, including the country name, continent, and various other details.

Example API Response
```json
{
  "status": "ok",
  "found": true,
  "countryName": "United States",
  "cqZone": 5,
  "ituZone": 8,
  "continent": "NA",
  "prefix": "K2",
  "countryCode": "US",
  "primaryDXCCPrefix": "K",
  "_t": "2024-09-26T15:41:49Z"
}
```
## Usage
1. Run the Script Directly
When the script is run directly, it uses a predefined ham radio prefix to fetch information. By default, the prefix used is 'k2'.

```bash
python ham_prefix_api.py
```
The output will display the API response for the k2 prefix:

```bash
Looking up Maidenhead conversion for: k2
API Response:
{
  "status": "ok",
  "found": true,
  "countryName": "United States",
  "cqZone": 5,
  "ituZone": 8,
  "continent": "NA",
  "prefix": "K2",
  "countryCode": "US",
  "primaryDXCCPrefix": "K",
  "_t": "2024-09-26T15:41:49Z"
}
```
2. Import and Use in Another Python Script
You can import the get_ham_radio_prefix_info function from ham_prefix_api.py into other Python projects to perform prefix lookups programmatically.

```python
from ham_prefix_api import get_ham_radio_prefix_info

# Lookup the prefix 'k2'
result = get_ham_radio_prefix_info('k2')

# Display the country name
if result and 'countryName' in result:
    print(f"Country Name: {result['countryName']}")
else:
    print("No country information found.")
Function: get_ham_radio_prefix_info
This function takes in a ham radio prefix and optionally a key to extract a specific value from the API response.

python
Copy code
def get_ham_radio_prefix_info(prefix, key=None):
    """
    Function to get ham radio prefix information from the HamNut API.
    
    Args:
        prefix (str): The ham radio prefix to look up.
        key (str, optional): The specific part of the JSON to return (e.g., "countryName").
        
    Returns:
        dict or str: The response data as a dictionary if successful, or a specific key value if provided.
    """
prefix: A string containing the ham radio prefix to look up.
key: (Optional) A string representing the specific field you want from the API response, such as "countryName" or "continent". If key is not provided, the entire JSON response will be returned.
```
Example Usage of the key Argument
```python
# Lookup and get only the country name for the prefix 'k2'
country_name = get_ham_radio_prefix_info('k2', key='countryName')
print(f"Country Name: {country_name}")
```
## Requirements
Python 3.x
requests library
You can install the required library by running:

```bash
Copy code
pip install requests
```
## Configuration
If you want to modify the default prefix when running the script standalone, you can change the default_prefix variable within the ham_prefix_api.py file:

```python
# Default prefix value when running the script standalone
default_prefix = 'k2'
```
## License
This project is licensed under the MIT License.

## Contributions
Feel free to fork the repository and submit pull requests for any improvements or additional features.

