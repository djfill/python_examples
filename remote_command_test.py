from subprocess import call
ret = chr(call(["ssh", "root@phillinux.admiral.uk", "ls scripts"]))

for i in ret:
   print(i)

