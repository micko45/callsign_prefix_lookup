import requests

def get_ham_radio_prefix_info(prefix_or_callsign, key=None):
    """
    Function to get ham radio prefix information from the HamNut API.
    
    Args:
        prefix_or_callsign (str): The ham radio prefix or full callsign to look up.
        key (str, optional): The specific part of the JSON to return (e.g., "countryName").
        
    Returns:
        dict or str: The response data as a dictionary if successful, or a specific key value if provided. None otherwise.
    """
    # Check if the input is a full callsign and extract the prefix
    prefix = extract_prefix(prefix_or_callsign)

    # Define the API URL and parameters
    url = 'https://api.hamnut.com/v1/call-signs/prefixes'
    params = {'prefix': prefix}  # Pass the extracted prefix as a parameter
    
    # Define the headers
    headers = {
        'accept': 'application/json'
    }
    
    try:
        # Send the GET request
        response = requests.get(url, headers=headers, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Parse the JSON data

            # If a specific key is requested, return only that part of the data
            if key:
                return data.get(key, f"{key} not found in the response.")
            
            # Return the full JSON response if no specific key is requested
            return data
        
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def extract_prefix(callsign):
    """
    Function to extract the prefix from a ham radio callsign.
    
    Args:
        callsign (str): The ham radio callsign or prefix.
        
    Returns:
        str: The extracted prefix, usually the first 1-3 alphanumeric characters.
    """
    # Extract the first 1-3 alphanumeric characters (this can be customized if needed)
    prefix = ''.join([char for char in callsign if char.isalpha() or char.isdigit()][:3])
    
    # Return the prefix
    return prefix


# Default prefix value when running the script standalone
default_prefix = 'k2xyz'

if __name__ == "__main__":
    # Use the default prefix value if the script is executed directly
    print(f"Looking up ham radio prefix info for: {default_prefix}")
    
    # Look up the full response
    result = get_ham_radio_prefix_info(default_prefix)
    
    if result:
        print("Full API Response:")
        print(result)
        
        # Example: Requesting a specific part, such as the country name
        country_name = get_ham_radio_prefix_info(default_prefix, key="countryName")
        print(f"Country Name: {country_name}")
        
    else:
        print("Failed to get the ham radio prefix info.")
