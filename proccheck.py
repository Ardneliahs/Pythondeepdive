import psutil, time, subprocess, sys
try:
#    named_id = int(subprocess.check_output('pidof named', shell=True))
    sp = subprocess.Popen('pidof named',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    rc= sp.wait()
    named_id,named_err = sp.communicate()
except:
#    print('UNKNOWN [script error]')
    print(named_err)
    sys.exit(3)
named_proc = psutil.Process(named_id)
named_start = int(named_proc.create_time())
now_epoch = int(time.time())
if now_epoch - named_start > 1800:
    print("CRITICAL")
    sys.exit(2)
else:
    print("OK")
    sys.exit(0)
