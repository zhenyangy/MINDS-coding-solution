### README

The date part of this assignment is ambiguous to me. It could mean:

- date only like in given example output.
  - e.g. 2019-01-01T00:00:00
  - but then exact time information in the original data is never used
- date including exact launching time.
  - e.g. 2019-01-10T17:05:00
  - then value column would most likely only be 0 and 1 because it's highly unlikely to have multiple launches at exactly same hour and minute.



Therefore I am submitting two script for these two cases:

- "web_scraping_zhenyang_dateOnly.py" for first case
- "web_scraping_zhenyang.py" for second case



To run script, simply use "python3 FILENAME". No extra command line argument is needed.



P.S. I didn't include timezone in date format because timezone information cannot be found in data source.

