import csv
fo = open("/root/Pythondeepdive/my.csv","a",newline="")
csv_writer = csv.writer(fo,delimiter=",")
csv_writer.writerow(["Master of Puppers",1986])
fo.close()
