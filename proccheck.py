import psutil, time, subprocess, sys
try:
#    sssd_id = int(subprocess.check_output('pidof sssd', shell=True))
    sp = subprocess.Popen('pidof sssd',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    rc= sp.wait()
    sssd_id,sssd_err = sp.communicate()
    if rc != 0:
        print(sssd_err)
        sys.exit(4)
except:
    print('UNKNOWN [script error]')
    sys.exit(3)
sssd_proc = psutil.Process(sssd_id)
sssd_start = int(sssd_proc.create_time())
now_epoch = int(time.time())
if now_epoch - sssd_start > 1800:
    print("CRITICAL")
    sys.exit(2)
else:
    print("OK")
    sys.exit(0)
