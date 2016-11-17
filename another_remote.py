import subprocess
#p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
p = subprocess.Popen("ssh", "root@phillinux.admiral.uk", "ls scripts")
(output, err) = p.communicate()
print ("Today is", output)
