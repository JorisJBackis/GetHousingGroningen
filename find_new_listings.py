import time
import random
from retrieve_listings import fetch_listings
from send_notification_email import send_email
import json
import os

def load_previous_listings(file_path='listings.json'):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

def save_current_listings(listings, file_path='listings.json'):
    with open(file_path, 'w') as file:
        json.dump(listings, file)

def detect_new_listings(current_listings, previous_listings):
    new_listings = [listing for listing in current_listings if listing not in previous_listings]
    return new_listings

def main():
    while True:
        # Get the current time as a string in "HH:MM" format
        current_time_str = time.strftime("%H:%M")
        start_time_str = "08:00"
        end_time_str = "19:30"

        # Check if the current time is within working hours
        if start_time_str <= current_time_str <= end_time_str:
            previous_listings = load_previous_listings()
            current_listings = fetch_listings()
            new_listings = detect_new_listings(current_listings, previous_listings)

            if new_listings:
                send_email(new_listings, 'jorisbackis@gmail.com')  # Replace with email where you wish to receive notifications
                save_current_listings(current_listings)
            else:
                print("No new listings found.")

            # Wait for a random interval (8 to 22 minutes) in order to simulate real human activity
            wait_time = random.randint(8*60, 22*60)  # Convert minutes to seconds
            print(f"Waiting for {wait_time // 60} minutes {wait_time % 60} seconds before the next run.")
            time.sleep(wait_time)
        else:
            print("Outside of working hours. Exiting.")
            break  # Exit the loop and end the script

if __name__ == "__main__":
    main()
