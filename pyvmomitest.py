from pyVim.connect import SmartConnect

c = SmartConnect(host="glastonbury.admiral.uk", user="adm_evansp", pwd='G9b9gt8!')

print(c.CurrentTime())
