from utils.api_helper import fetch_data
import json

# Function to get deals data
def get_deals_data():
    data = {
        "location": "Riyadh",  # Example location filter
        "price_range": [1000000, 5000000],  # Example price range filter
    }
    return fetch_data("deals", data)

# Function to get top deals
def get_top_deals():
    data = {"limit": 10}  # Example: Fetch top 10 deals
    return fetch_data("top_deals", data)

# Function to get land details
def get_land_details():
    data = {"location": "Jeddah"}  # Example location filter
    return fetch_data("lands", data)

# Main function to fetch and print the data
def main():
    # Fetch and display deals data
    deals_data = get_deals_data()
    if deals_data:
        print("Deals Data:")
        print(json.dumps(deals_data, indent=4))

    # Fetch and display top deals
    top_deals = get_top_deals()
    if top_deals:
        print("Top Deals:")
        print(json.dumps(top_deals, indent=4))

    # Fetch and display land details
    land_details = get_land_details()
    if land_details:
        print("Land Details:")
        print(json.dumps(land_details, indent=4))

if __name__ == "__main__":
    main()
