
V7000 = [["ssh", "automate", "@", "bolt_dev_xv7000.admiral.uk", "lsmdiskgrp -nohdr -delim :"],\
         ["ssh", "automate", "@", "uni-v7000-bolt-nonprod-ta.bolt.admiral.uk", "lsmdiskgrp -nohdr -delim :"]]

#print (V7000[0])
#print (V7000[1])

#V7000[0][3]="ta-v7000.admiral.uk"

#for l in V7000[0]:
#   print str.upper(l)

#print (V7000[0])
#a = [V7000[0][1],V7000[0][2],V7000[0][3]]
#b = ''.join(a)
#del V7000[0][1]
#del V7000[0][1]
#V7000[0][1] = b
#print (V7000[0])

V7000s = [[],[]]
count = 0
for V in V7000:
   a = V[1],V[2],V[3]
   b = ''.join(a)
   del V[1]
   del V[1]
   V[1] = b
   V7000s[count] = V
   count+=1
   
print V7000s[0],V7000s[1]
