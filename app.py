from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Replace with your actual full name
    name = "Bhavishya Yarlagadda"
    
    # Get system username, with a fallback message if not found
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get top command output (first 10 lines)
    try:
        top_output = subprocess.getoutput("top -b -n 1 | head -10")
    except Exception as e:
        top_output = f"Error retrieving top output: {e}"

    # HTML response
    response = f"""
    <html>
        <head><title>HTOP Endpoint</title></head>
        <body>
            <h1>HTOP Endpoint</h1>
            <p><b>Name:</b> {name}</p>
            <p><b>User:</b> {username}</p>
            <p><b>Server Time (IST):</b> {server_time}</p>
            <pre><b>TOP Output:</b>\n{top_output}</pre>
        </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
