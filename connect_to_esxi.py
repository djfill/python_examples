from pyVim.connect import Connect, Disconnect
import sys
from pyVmomi import vim
import ssl

s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE

si = Connect(host='esx-boltapp01.admiral.uk',user='root',pwd='Sol654vent168',sslContext=s)

print si.CurrentTime()

ds = si.content.rootFolder.childEntity[0].datastoreFolder.childEntity

for store in ds:
    print store.name

#disconnect fron the vCenter
Disconnect(si)
