def echo(usr,lang,sys):
   print('User:',usr,'Language:',lang,'Platform:',sys)

echo('Mike','Python','Windows')
echo(lang = 'Python',sys = 'Mac OS',usr = 'Anne')

def mirror(usr='Carole',lang='Python'):
   print('\nUser:',usr,'Language:',lang)

mirror()
mirror( lang = 'Java')
mirror( usr = 'Tony')
mirror('Susan','C++')

