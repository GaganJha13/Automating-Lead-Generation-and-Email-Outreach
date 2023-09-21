# Automating-Lead-Generation-and-Email-Outreach
task is to develop a Python script that automates the process of lead generation from Google Maps, data management in Google Sheets, and personalized email outreach using the ChatGPT API and an email service.

Working of the whole API ---->

1. Scrape.py: This file is going to scrape the data from the
Google Map, and in this file we have set the cafe in Jaipur.
as the default industry whose data we need and using the
fileWe will extract each and every cafe name, address,and 
email ID. Here, I see that most of the cafes did not have 
any email ID, so we just set a default email ID and save all
the data into a pagedata.csv file, which will be created 
after running this script.

2. Google Sheets: This is the most confusing part where the 
userneed to set everything according to the user's needs. 
Here youI need to create a Google Sheet with the name and 
title and make itshare with the Google authentication drive 
and also need to attach a JSON file that you have downloaded 
from Google.authentication drive for further assistance in 
this topic I used chatgpt. After doing all the things, we 
just ran this script, which will append all the data to the 
Google Sheet.

3. sendemail: This file will send the email to each email.ID 
in the csv file, as we have set a single mail ID, so it is 
going to send single mail with attaching the csv file.
This is how my simple and very basic code works, if 
The company wants this API at such a level that any user 
can use it, they can ask me. I can create this API and convert
it into GUI form using the tkiner library of Python, so that 
any Normal users can use it very easily for office use.

Kindly appreciate my work ,it is time-consuming as well.

Thankyou !!!
