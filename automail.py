import yagmail
import os

receiver = "shreyashkumar621@gmail.com"  # receiver email address
body = "Attendance File"  # email body
filename = "Attendance" + os.sep + "Attendance_2020-08-29_17-05-04.csv"

# Use the app password generated from your Google Account
yag = yagmail.SMTP("enduringimpulse", "SNSp5SZG&P$qJMn")

yag.send(
    to=receiver,
    subject="Attendance Report",
    contents=body,
    attachments=filename
)

print("Email sent successfully.")