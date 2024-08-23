# GetHousingGroningen

GetHousingGroningen is a Python-based web scraping application designed to monitor new housing listings on the [Campus Groningen website](https://www.campusgroningen.com/huren-groningen). This tool is particularly useful for this specific website because the opportunity to participate in a viewing is offered on a first-come, first-served basis. Only the first four people can register for a viewing, making it crucial to be notified as soon as new listings are available. The script checks for new listings at random intervals during working hours and sends an email notification with the details of any new listings it finds.

## Features

- Automated Web Scraping: Fetches housing listings from the Campus Groningen website.
- Email Notifications: Sends email notifications when new listings are found.
- Randomized Intervals: Checks for updates at random intervals to mimic human activity.
- Working Hours: Operates between 08:00 and 19:30, ensuring it runs only during relevant hours.

## Requirements

- Python 3.x: Ensure Python 3 is installed on your system.
- Required Libraries: Install the following Python libraries:
  - requests
  - beautifulsoup4
  - smtplib (built-in with Python)
  - email (built-in with Python)

You can install the external libraries using pip:

`pip install requests beautifulsoup4`

## Installation

1. Clone the Repository:
   - Download or clone this repository to your local machine.

   `git clone https://github.com/yourusername/GetHousingGroningen.git`
   
   `cd GetHousingGroningen`

2. Set Up the Environment:
   - If you're familiar with Python virtual environments, you can create and activate one:

   `python -m venv venv`
   
   `source venv/bin/activate  # On Windows use: venv\Scripts\activate`

3. Install Dependencies:
   - Install the required Python libraries.

   `pip install -r requirements.txt`

4. Configure Email Notifications:
   - Open send_notification_email.py and replace `sender_email` and `sender_password` with your Gmail credentials.
   
   **Important**: For security, you might want to generate an "App Password" in your Gmail account instead of using your actual Gmail password. You can enable "App Passwords" in your Google Account settings if you have 2-Step Verification enabled.

## Usage

1. Run the Script:
   - To start the application, run the `find_new_listings.py` script:

   `python find_new_listings.py`

   The script will begin checking for new housing listings at random intervals within working hours (08:00 to 19:30). If any new listings are found, they will be emailed to the address you specified.

2. Stop the Script:
   - To stop the script, simply press `Ctrl + C` in the terminal.

## How It Works

- retrieve_listings.py: This script contains the function that scrapes the Campus Groningen website for housing listings.
- find_new_listings.py: The main script that loads previous listings, checks for new listings, and sends notifications if any new listings are found.
- send_notification_email.py: This script sends email notifications with the details of the new listings.

## Notes

- Running the Script Continuously: If you want the script to run continuously, consider using a task scheduler (like Windows Task Scheduler) to automatically start the script at specific times.
- Customizations: Feel free to modify the `start_time_str` and `end_time_str` variables in `find_new_listings.py` to change the operating hours of the script.





# Project by **Joris Backis**
