from selenium import webdriver
import time
from tqdm import tqdm
from datetime import datetime, timedelta

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)


# Split date range into chunks of 100 days
start_date = datetime(2014, 7, 1)
end_date = datetime(2024, 9, 12)
chunk_size = 100

current_date = start_date

chunks = []

while current_date <= end_date:
    chunk_end_date = current_date + timedelta(days=chunk_size - 1)

    if chunk_end_date > end_date:
        chunk_end_date = end_date

    start_str = [current_date.strftime('%d'), current_date.strftime('%m'), current_date.strftime('%Y')]
    end_str = [chunk_end_date.strftime('%d'), chunk_end_date.strftime('%m'), chunk_end_date.strftime('%Y')]

    chunks.append((start_str, end_str))

    current_date = chunk_end_date + timedelta(days=1)

# Get data for each date chunk
for ds in ['applications_breakdown', 'applications_by_age_group', 'applications_by_type', 'applications_by_nation']:

    print(ds)

    for date_chunk in tqdm(chunks):

        start = date_chunk[0]
        end = date_chunk[1]

        driver.get(f"https://www.registertovote.service.gov.uk/performance/{ds}/download/with_dates?fromDay={start[0]}&fromMonth={start[1]}&fromYear={start[2]}&toDay={end[0]}&toMonth={end[1]}&toYear={end[2]}")

        time.sleep(5)
