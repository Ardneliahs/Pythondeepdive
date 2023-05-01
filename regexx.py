import re
re_pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
re_text = "10.9.68.111"
print(re.findall(re_pattern,re_text))
print(len(re.findall(re_pattern,re_text))) # number of occurences
