import csv
read_file = "/root/Pythondeepdive/my.csv"
fo = open(read_file,'r')
content = csv.reader(fo)
print(content)
