# Selenium-Check-Results

Usage - Create an input file with list of reg_no and dob seperated by commas, one per line

Example input.txt follows

2012124124124,04-07-1998

3241431421421,07-04-1992

and so on. To run the script, use python3 check_results.py input.txt

The result will be saved as a screenshot with the reg_no as the file name.

Needs Google chrome, selenium and python3 installed.

Download chrome driver from 

https://sites.google.com/a/chromium.org/chromedriver/downloads

Copy to /usr/local/bin/ (on *nix based systems)

Captcha has to be manually entered. Wait for the script to fill in the regno and date, and then enter captcha.

