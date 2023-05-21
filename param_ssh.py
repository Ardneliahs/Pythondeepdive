import paramiko
sshc = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.6',username='root',password='Skelter1',port=22)
stdin, stdout, stderr = ssh.exec_command('uptime')
print(stdout.readline())
