# List of variables, hosts and commands
host = []
host.append('bolt_dev_xv7000.admiral.uk')
host.append('uni-v7000-bolt-nonprod-ta.bolt.admiral.uk')
host.append('uni-v7000-bolt-nonprod-sa.bolt.admiral.uk')
host.append('uni-v7000-bolt-ta.bolt.admiral.uk')
host.append('uni-v7000-bolt-sa.bolt.admiral.uk')
host.append('v7000-ta.admiral.uk')
host.append('v7000-swa.admiral.uk')

list_pool = "lsmdiskgrp -nohdr -delim :"
v = []
V7000 = []
cmd = "ssh"
usr = "automate"
create_disk = []

# Generate lists of ssh commands per V7000
for h in host:
   v = [cmd,usr,'@',h,list_pool]
   V7000.append(v)

# Join the lists into a readable argument to pass to Popen
V7000s = []
for V in V7000:
   a = V[1],V[2],V[3]
   b = ''.join(a)
   del V[1]
   del V[1]
   V[1] = b
   V7000s.append(V)
   
print "\nSelect a v7000 from the below list:\n"

count = 1
for h in host:
   print count,":",h
   count+=1

select = getOption(": ",len(V7000s))
choice = V7000s[select]
return choice
