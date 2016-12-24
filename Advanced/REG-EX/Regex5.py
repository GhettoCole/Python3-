import re

# Make a program that matches email address from a list
# RULES

# 1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase and uppercase letters, numbers, plus ._
# 4. A period(.)
# 5. 2 and 3 lowercase  and uppercase letters


email_List = "Given@Gmail.com m@.com Vivid@apple.com db@.com db@oal.com Niche@Mail.UK"

print("Email matches: ", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email_List)))
