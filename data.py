import pandas as pd
import random

# Constants
applications = ["excel", "ppt", "one drive", "share point"]
week_start_date = "2002-05-15"
emails = ["support@example.com", "admin@company.com", "user@mail.com"]
urls = ["http://company.com/help", "https://support.example.com", "http://docs.company.com"]
stopwords = ["the", "is", "at", "which", "on", "for", "a", "an"]

base_descriptions = [
    "issue in managing file permission in one drive",
    "ppt crashes when adding images from http://company.com/help",
    "excel formula =SUM(A1:A5) not working properly for user@mail.com",
    "share point link https://support.example.com not opening correctly",
    "the file is not syncing on the one drive system",
    "broken hyperlink in ppt slides which is causing errors on presentation",
    "the excel sheet is locked for editing by admin@company.com",
    "user unable to upload file on share point due to permission at system level",
    "ppt animations not playing when shared over http://docs.company.com",
    "excel chart formatting resets automatically for a user"
]

# Generate dataset
records = []
for _ in range(200):
    ticket = "GMC" + str(random.randint(3000000, 3999999))
    application = random.choice(applications)
    
    desc = random.choice(base_descriptions)
    desc += f" contact {random.choice(emails)} or visit {random.choice(urls)}"
    desc += f" {random.choice(stopwords)} {random.choice(stopwords)} additional issue."

    records.append({
        "ticket": ticket,
        "application": application,
        "week_start_date": week_start_date,
        "description": desc
    })

df = pd.DataFrame(records)

# Show output
#print(df.head())
df.to_csv("synthetic_app_issues.csv", index=False)
