import json
import math
import csv
from dateutil.parser import parse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# config
USERNAME = "skdcodes@gmail.com"  # username to login to medeley
PASSWORD = "xj6360xj"  # password
PER_PAGE = 500  # API limits max of 500 results per page. mendley uses PER_PAGE=60 on frontend

# load selenium web driver
browser_options = Options()
browser_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path=ChromeDriverManager(
).install(), chrome_options=browser_options)
wait = WebDriverWait(browser, 10)

# open sign in page
print("Opening website...")
browser.get("https://www.mendeley.com/sign/in/")

# wait till input ready
username = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "pf.username"))
)
username.clear()
username.send_keys("skdcodes@gmail.com")
username.send_keys(Keys.RETURN)
print("Email entered.")

# wait till password ready
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password.clear()
password.send_keys("xj6360xj")
password.send_keys(Keys.RETURN)
print("Password entered.")


# wait till dashboard
feed = WebDriverWait(browser, 10).until(
    EC.title_contains("Feed")
)
print("Login successful!")

# open the grants API endpoint
print("Loading grants ...")
browser.get("https://www.mendeley.com/research-funding/api/opportunities?status=active&pageSize=1&page=0&orderBy=-lastUpdateDate&asjcCategories=2702&asjcCategories=2703&asjcCategories=2704&asjcCategories=2705&asjcCategories=2707&asjcCategories=2706&asjcCategories=2708&asjcCategories=2709&asjcCategories=2710&asjcCategories=2711&asjcCategories=2712&asjcCategories=2713&asjcCategories=2714&asjcCategories=2715&asjcCategories=2700&asjcCategories=2716&asjcCategories=2717&asjcCategories=2718&asjcCategories=2719&asjcCategories=2720&asjcCategories=2721&asjcCategories=2722&asjcCategories=2723&asjcCategories=2725&asjcCategories=2724&asjcCategories=2701&asjcCategories=2726&asjcCategories=2727&asjcCategories=2728&asjcCategories=2729&asjcCategories=2730&asjcCategories=2731&asjcCategories=2732&asjcCategories=2733&asjcCategories=2734&asjcCategories=2735&asjcCategories=2736&asjcCategories=2737&asjcCategories=2738&asjcCategories=2739&asjcCategories=2740&asjcCategories=2741&asjcCategories=2742&asjcCategories=2743&asjcCategories=2744&asjcCategories=2745&asjcCategories=2746&asjcCategories=2747&asjcCategories=2748&filterByOngoing=false")

# calculate total number of pages
html = browser.find_element_by_tag_name("pre").text
total = json.loads(html)["hits"]["total"]
max_pages = math.floor(total / PER_PAGE)
print("Total %s results found." % total)

# create dump file
with open('data.xlsx', 'w+', encoding='utf-8') as h:
    doc = csv.writer(h, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    doc.writerow(['Name', 'Deadline', 'Group', 'Funder', 'Amount',
                  'Type', 'Areas', 'Description', 'Eligibility', 'Contact', 'Source', 'Link'])

# iterate through each page and save result
count = 0
for page in range(0, max_pages+1):
    print("Scraping page: %s/%s ..." %
          (page+1, max_pages))
    browser.get("https://www.mendeley.com/research-funding/api/opportunities?status=active&pageSize=%s&page=%s&orderBy=-lastUpdateDate&asjcCategories=2702&asjcCategories=2703&asjcCategories=2704&asjcCategories=2705&asjcCategories=2707&asjcCategories=2706&asjcCategories=2708&asjcCategories=2709&asjcCategories=2710&asjcCategories=2711&asjcCategories=2712&asjcCategories=2713&asjcCategories=2714&asjcCategories=2715&asjcCategories=2700&asjcCategories=2716&asjcCategories=2717&asjcCategories=2718&asjcCategories=2719&asjcCategories=2720&asjcCategories=2721&asjcCategories=2722&asjcCategories=2723&asjcCategories=2725&asjcCategories=2724&asjcCategories=2701&asjcCategories=2726&asjcCategories=2727&asjcCategories=2728&asjcCategories=2729&asjcCategories=2730&asjcCategories=2731&asjcCategories=2732&asjcCategories=2733&asjcCategories=2734&asjcCategories=2735&asjcCategories=2736&asjcCategories=2737&asjcCategories=2738&asjcCategories=2739&asjcCategories=2740&asjcCategories=2741&asjcCategories=2742&asjcCategories=2743&asjcCategories=2744&asjcCategories=2745&asjcCategories=2746&asjcCategories=2747&asjcCategories=2748&filterByOngoing=false" % (PER_PAGE, page))

    # convert html to json
    html = browser.find_element_by_tag_name("pre").text
    page_data = json.loads(html)["hits"]["hits"]

    # process json and save to file
    with open('data.xlsx', 'a+', encoding='utf-8') as f:
        doc = csv.writer(f, delimiter=',', quotechar='"',
                         quoting=csv.QUOTE_ALL)
        for item in page_data:
            i = item["_source"]
            try:
                grant_name = i["name"]
                grant_deadline = parse(i["upcomingDueDate"]).strftime(
                    "%d %b %Y") if "upcomingDueDate" in i else None
                grant_group = i["groupTypeDescription"]
                grant_funder = i["leadFunder"]["org"]
                grant_amount = i["amountsInfo"]["amountDescription"]
                grant_type = ",".join(i["applicantType"])
                research = i["researchAreas"]
                grant_areas = {i["categoryDescription"]: [[j["categoryDescription"]
                                                           for j in i["children"]]] for i in research}
                grant_description = i["synopsis"][0]["description"]
                grant_eligibility = i["eligibilityDescription"]
                contact = i["contacts"][0] if len(i["contacts"]) != 0 else None
                grant_contact = '%s %s, %s, %s' % (
                    contact['surname'], contact['givenName'], contact['email'], contact['telephone']) if contact else None
                grant_source = i["recordSource"]
                grant_link = "https://www.mendeley.com/research-funding/opportunities/%s" % i["id"]

                doc.writerow([grant_name, grant_deadline, grant_group, grant_funder, grant_amount,
                              grant_type, grant_areas, grant_description, grant_eligibility, grant_contact, grant_source, grant_link])
            except Exception as e:
                print("Error while processing grant ID: %s" % i["id"], e)

            count += 1

        print("%s grants saved to file! Remaning: %s/%s " %
              (count, total-count, total))

browser.close()
print('All done! :)')
