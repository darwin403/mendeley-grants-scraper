# What is this?

This selenium script scrapes all the grants [https://www.mendeley.com/research-funding/opportunities?discipline=medicine](https://www.mendeley.com/research-funding/opportunities?discipline=medicine) for any specific "discipline".

# Installation

You will require `python3` and `pip3` to be installed on your computer before you can proceed to the next steps. Once installed, begin by installing the required libraries for this script by running

```bash
cd myproject # change directory to project
pip3 install -r requirements.txt # pip installs required libraries
```

Open the file `scrape.py` and edit the following lines to your mendeley email, password

```vim
.
.
USERNAME = "skdcodes@gmail.com"  # email to login to mendeley
PASSWORD = "xj6360xj"  # password
.
.
```

You can now run the script by doing

```bash
python3 scrape.py
```
Thats it! You will now see the scrape progress on your console something similar to:

```bash
# Opening website...
# Email entered.
# Password entered.
# Login successful!
# Loading grants ...
# Total 4877 results found.
# Scraping page: 1/9 ...
# 500 grants saved to file! Remaning: 4377/4877 
# Scraping page: 2/9 ...
# 1000 grants saved to file! Remaning: 3877/4877 
# Scraping page: 3/9 ...
# 1500 grants saved to file! Remaning: 3377/4877 
# Scraping page: 4/9 ...
# 2000 grants saved to file! Remaning: 2877/4877 
# Scraping page: 5/9 ...
# 2500 grants saved to file! Remaning: 2377/4877 
# Scraping page: 6/9 ...
# 3000 grants saved to file! Remaning: 1877/4877 
# Scraping page: 7/9 ...
# 3500 grants saved to file! Remaning: 1377/4877 
# Scraping page: 8/9 ...
# 4000 grants saved to file! Remaning: 877/4877 
# Scraping page: 9/9 ...
# 4500 grants saved to file! Remaning: 377/4877 
# Scraping page: 10/9 ...
# 4877 grants saved to file! Remaning: 0/4877 
# All done! :)
```

The data dump file is saved to `data.xlsx` in the same folder as the script.

# Notes

- You see what the browser is doing by removing the "headless" options. That is, by **removing** the line: `browser_options.add_argument("--headless")`

