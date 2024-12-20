# requirements.txt
Flask==3.0.0
gunicorn==21.2.0

# vercel.json
{
    "version": 2,
    "builds": [
        {
            "src": "app.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "app.py"
        }
    ]
}

# app.py
from flask import Flask, redirect
from os import environ

# Initialize Flask app
app = Flask(__name__)

# Discord invite URL
DISCORD_INVITE_URL = "https://discord.gg/nEMHqf2DBd"

# Route for root path
@app.route('/')
def redirect_to_discord():
    return redirect(DISCORD_INVITE_URL, code=302)

# Route to catch all paths and redirect them
@app.route('/<path:path>')
def catch_all(path):
    return redirect(DISCORD_INVITE_URL, code=302)

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return redirect(DISCORD_INVITE_URL, code=302)

if __name__ == '__main__':
    # Get port from environment variable or use 5000 as default
    port = int(environ.get('PORT', 5000))
    
    # Run the app
    app.run(
        host='0.0.0.0',  # Makes the server publicly available
        port=port,
        debug=False  # Set to False in production
    )