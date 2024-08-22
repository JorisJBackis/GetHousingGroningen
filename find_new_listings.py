from retrieve_listings import fetch_listings
from send_notification_email import send_email  # Import the send_email function
import json
import os

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

# Main script to check for new listings and send notifications
if __name__ == "__main__":
    previous_listings = load_previous_listings()
    current_listings = fetch_listings()  # Fetch the current listings
    new_listings = detect_new_listings(current_listings, previous_listings)

    if new_listings:
        send_email(new_listings, 'recipient-email@example.com')  # Replace with your recipient email
        save_current_listings(current_listings)  # Update the listings.json file
    else:
        print("No new listings found.")
