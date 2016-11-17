from pyVim.connect import SmartConnect, Disconnect
# import ssl
import getpass

# s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
# s.verify_mode = ssl.CERT_NONE

password = getpass.getpass('Enter vCenter password: ')

try:
   c = SmartConnect(host="glastonbury.admiral.uk", user="adm_evansp", pwd=password)
   print "Valid Certificate"
except:
   c = SmartConnect(host="glastonbury.admiral.uk", user="adm_evansp", pwd=password)
   print "Invaild or untrusted certificate"
# get a list of host clusters
hostclusters = c.content.rootFolder.childEntity[1].hostFolder.childEntity
# print the list of host cluster names and indexs
print "Please select a Cluster:"
for idx, h in enumerate(hostclusters):
   print idx,':',h.name
# get the users choice
choice = int(input(':'))
# print the list of hosts from the host cluster selected by the user
for h in hostclusters[choice].host:
   print h.name
#disconnect fron the vCenter
Disconnect(c)

