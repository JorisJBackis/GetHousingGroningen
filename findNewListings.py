import json
import os
from retrieve_listings import fetch_listings  # Import the function from your first script

# Load the previous listings
def load_previous_listings(file_path='listings.json'):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

# Save the current listings
def save_current_listings(listings, file_path='listings.json'):
    with open(file_path, 'w') as file:
        json.dump(listings, file)

# Detect new listings
def detect_new_listings(current_listings, previous_listings):
    new_listings = [listing for listing in current_listings if listing not in previous_listings]
    return new_listings

# Main script to test the comparison
if __name__ == "__main__":
    previous_listings = load_previous_listings()
    current_listings = fetch_listings()  # Call the function from the first script
    new_listings = detect_new_listings(current_listings, previous_listings)

    print("New Listings:", new_listings)  # Output new listings to see if the detection works

    # Optionally save the new listings
    save_current_listings(current_listings)
