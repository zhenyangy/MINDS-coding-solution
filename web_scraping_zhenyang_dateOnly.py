from bs4 import BeautifulSoup
import urllib.request
import csv
import datetime
import collections
import re


source_url = "https://en.wikipedia.org/wiki/2019_in_spaceflight#Orbital_launches"
orbital_page = urllib.request.urlopen(source_url).read()
good_outcome = set(("Successful", "Operational", "En route"))
launch_count = collections.defaultdict(int)

soup = BeautifulSoup(orbital_page, 'html.parser')
table = soup.select("#mw-content-text > div:nth-of-type(1) > table:nth-of-type(3)")[0]
flag = False

for row in table.find_all("tr"):
    out_row = []
    cell = row.find_all("td")
    # find date time and format them in ISO format
    if len(cell) == 5:
        if flag:
            launch_count[date] += 1
            flag = False
        year = 2019
        if cell[0].span.find_all():
            day, month = tuple(cell[0].find(cell[0].span.find_all()[0].name).previous_sibling.split())
        else:
            day, month = cell[0].span.text.split()[0], cell[0].find("span").text.split()[1]
        month = datetime.datetime.strptime(month, '%B').month
        hr, minute, second = '00', '00', '00'
        # if cell[0].br and re.match(r'(\d\d(:\d\d)+)', cell[0].br.next_sibling):
        #     time = cell[0].br.next_sibling.split(":")
        #     hr = time[0] if len(time)>=1 else '00'
        #     minute = time[1] if len(time)>=2 else '00'
        #     second = time[2] if len(time)>=3 else '00'
        date = datetime.datetime(year=2019, month=month, day=int(day), hour=int(hr), minute=int(minute), second=int(second)).isoformat()

    # determine if at least one payload is launched
    if len(cell) == 6:
        if not flag:
            flag = any(cell[-1].text.strip().startswith(el) for el in good_outcome)

# edge case
if flag:
    launch_count[date] += 1

start_date = datetime.date(2019, 1, 1)
end_date = datetime.date(2020, 1, 1)
results = [['date', 'value']]
for n_date in (start_date + datetime.timedelta(n) for n in range(int ((end_date - start_date).days))):
    n_date = str(n_date)+"T00:00:00"
    if n_date in launch_count:
        results.append([n_date, launch_count[n_date]])
    else:
        results.append([n_date, 0])

with open("output_dateOnly.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)
