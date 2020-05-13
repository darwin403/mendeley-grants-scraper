# What does this script do?

This selenium script `scrape.py` scrapes all the active research grants for a specific discipline from [https://www.mendeley.com/research-funding/opportunities?discipline=medicine](https://www.mendeley.com/research-funding/opportunities?discipline=medicine) from their Elasticsearch API endpoint! It creates a dump `data.xlsx` with the following columns.

| Grant Name                                                   | Last Update | Deadline    | Group                                     | Funder                                                                          | Amount              | ... |
| ------------------------------------------------------------ | ----------- | ----------- | ----------------------------------------- | ------------------------------------------------------------------------------- | ------------------- | --- |
| Rural Emergency Medical Communications Demonstration Project | 21 Feb 2020 | 24 Jun 2020 | Contract, tender or cooperative agreement | U.S. Department of Homeland Security                                            | Up to 2,000,000 USD | ... |
| Special Call under SATYAM to fight against COVID 19          | 1 Jan 2019  | 31 May 2020 | Programs and projects                     | Department of Science and Technology, Ministry of Science and Technology, India | 1,500,000 INR       | ... |
| ...                                                          | ...         | ...         | ....                                      | ...                                                                             | ...                 | ... |

# Installation

You will require `python3` and `pip3` to be installed on your computer before you can proceed to the next steps. Once installed, begin by installing the required libraries for this script by running

```bash
git clone git@github.com:skdcodes/freelancer-selenium-mendeley.git # git clone repository
cd freelancer-selenium-mendeley # change directory to project
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
