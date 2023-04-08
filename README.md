
# Automated Login to Sheffield Property Shop Website

This is a Python script that automates the login process to the Sheffield Property Shop website using the Selenium WebDriver because it's so annoying.

## Requirements

* Python 3.x
* Selenium WebDriver for Chrome

## Installation

1. Install Python 3.x from the [official website](https://www.python.org/downloads/).
2. Install the Selenium WebDriver for Chrome by following the instructions on the [official website](https://sites.google.com/a/chromium.org/chromedriver/downloads).

   ```
   pip install selenium
   ```
3. Download the `main.py` file from this repository.

## Usage

1. Set your Sheffield Property Shop website credentials in the `.env` file.
2. Open a command prompt or terminal window and navigate to the directory where the `main.py` file is located.
3. Run the script by entering the following command: `python3 main.py`.
4. The script will use the credentials from the `.env` file to log in to the Sheffield Property Shop website.

## Troubleshooting

* If the script fails to find an element on the login page, make sure that the element ID in the script matches the ID of the element on the website.
* If the script fails to log in, make sure that the login reference number and date of birth are correct.
* If the script fails to open Chrome when the user is successfully logged in, make sure that the path to the Chrome executable is correct in the `webbrowser.register` function.

## License

This script is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
