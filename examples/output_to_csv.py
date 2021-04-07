from redash_toolbelt import Redash
import redadocs.dashboards as rdd
import os


URL = os.environ["REDASH_URL"]
KEY = os.environ["REDASH_KEY"]

print(f" Connecting to {URL} using API key {KEY}...")
## create a client object
client = Redash(URL,KEY)

rows = rdd.get_all_db_details(client,csv=True)

import csv

headline = ["Name","Tags","Updated","Archived","Description", "Public Link"]
output_file= "output.csv"

with open(output_file, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

    spamwriter.writerow(headline)
    for row in rows:
        spamwriter.writerow(row)