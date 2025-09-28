	Auto Cookie Clicker Using Selenium

This is a simple automated script that plays the popular web game Cookie Clicker

using Selenium WebDriver. The script continuously clicks the big cookie, buys upgrades, and purchases products to maximize cookie production automatically.

	Features

Automatically clicks the big cookie to generate cookies.

Periodically checks and buys available upgrades.

Purchases unlocked products when enough cookies are available.

Handles in-game notifications and pop-ups to avoid interruptions.

Uses Microsoft Edge browser with Selenium.

	Prerequisites

Python 3.x installed on your system.

Microsoft Edge browser installed.

Microsoft Edge WebDriver
matching your Edge browser version.

selenium Python package installed.

	Install Selenium via pip if you haven't yet:

pip install selenium

	Usage

Download and place the appropriate Edge WebDriver in your system PATH or specify the executable path in the script.

	Run the script:

python auto_cookie_clicker.py


The Edge browser will open and load the Cookie Clicker game.

The script will select English language and accept cookies to start.

It will automatically click the cookie, buy upgrades, and products indefinitely.

	How It Works

The script uses Selenium to control Edge browser and interact with the game's elements.

Every few seconds, it clicks the big cookie.

Every 30 seconds, it checks for available upgrades and buys the most expensive one.

Between upgrade checks, it purchases unlocked products if enough cookies are available.

It handles pop-up notifications to keep the automation running smoothly.

The script runs in an infinite loop until manually stopped.

	Customization

Modify time intervals by changing the delay values inside the script.

Change the browser to Chrome or Firefox by swapping out the WebDriver initialization.

Add logging or screenshot capture for debugging.

	Disclaimer

This script is for educational purposes and personal use only. Use it responsibly and do not use it to disrupt or harm game servers.

	License

This project is licensed under the MIT License.
