HTOP Endpoint Web Application
This repository contains a Flask web application created for an internship test. The application serves a single endpoint, /htop, which displays system information such as your full name, system username, server time in IST, and the output of the top command.

Project Overview
The /htop endpoint provides:

Name: Your full name.
Username: The system username (e.g., codespace).
Server Time in IST: The current time in Indian Standard Time.
Top Output: A snapshot of system usage from the top command.
Technologies Used
Python 3
Flask
GitHub Codespaces
Setup Instructions
Prerequisites
A GitHub account with access to GitHub Codespaces.
Python 3 installed in the Codespace.
Steps to Set Up and Run the Application
Clone the Repository:

bash
Copy code
git clone https://github.com/BhavishyaYarlagadda/MorphleLabs.git
cd your-repository
Start a Codespace:

Open the repository on GitHub and start a Codespace.
Set the timeout to 240 minutes to keep the Codespace active.
Install Flask:

bash
Copy code
pip install flask
Run the Application:

Start the Flask server:
bash
Copy code
python app.py
Expose the Port:

In your Codespace, go to the Ports tab.
Make sure port 5000 is exposed publicly.
Access the Application
Once the application is running, you can access it via the /htop endpoint:

arduino
Copy code
https://your-codespace-url.github.dev/htop
Replace your-codespace-url with the actual URL provided by GitHub Codespaces.

Example Output
When accessed, the /htop endpoint should display information similar to:

yaml
Copy code
HTOP Endpoint
Name: Bhavishya Yarlagadda
User: codespace
Server Time (IST): 2024-11-12 10:45:37.150311
Top Output:
top - 05:15:37 up 21 min, 0 users, load average: 0.23, 0.43, 0.76
...
Troubleshooting
HTTP ERROR 502: If you see this error, ensure the Flask application is running and that the port is set to public.
Access Denied: Verify the port visibility setting in the Ports tab of Codespaces.
Submission Instructions
Link 1: URL to the /htop endpoint (e.g., https://humble-waddle-5ww6665vwv924j4w-5000.app.github.dev/htop).
Link 2: URL to this GitHub repository (ensure it’s public).
