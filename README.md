# A SIMPLE AND SOBER BULK EMAIL SENDER

![](ZZZ/ZZZ.png)

* Send bulk emails using simple templates
* Format with custom data easily
* Send HTML emails
* Have some fun

# HOW TO USE
```python3

from EMAIL_AUTOMATION.email_automation IMPORT EMAIL

#$$$$$$$$$$#

# CREATE_OBJECT WITH SERVER ADDRESS
EMAIL_OBJ = EMAIL("smtp.gmail.com:587")
# SET THE MAIN BODY TEMPLATE
EMAIL_OBJ.set_template("""How's this mail ? {format_param}""")
# SET DATA FOR ACCOUNT LOGIN
EMAIL_OBJ.set_user_pass("YOUR_EMAIL@provider", "SECRET_KEY_OBTAINED_FROM_PROVIDER")
# LOGIN TO THE ACCOUNT
EMAIL_OBJ.login()
# SEND EMAIL
EMAIL_OBJ.send_mail("RECIPIENT_S_ADDRESS", # SET RECIPIENT_S ADDRESS
                    "SUBJECT", # SET SUBJECT
                    {"format_param": "HU HU HU HU"}, # GIVE ALL PARAMERTES OR KEYS REQ TO FORMAT THE MAIN BODY TEMPLATE
                    ["init.vim", "m1.py"]) # ABSOLUTE OR RELATIVE PATH TO FILES TO ATTACH
