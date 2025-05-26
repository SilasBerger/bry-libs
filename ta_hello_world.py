entscheid = input('Willst du gehen oder bleiben? [gehen/bleiben]: ').lower()
if entscheid == 'gehen':
  print('Ok, ciao!')
elif entscheid == 'bleiben':
  print('Gute Wahl.')
  entscheid = input('Willst du gewinnen oder verlieren? [gewinnen/verlieren]: ')
  if entscheid == 'gewinnen':
    print('Du hast gewonnen! 🥳')
  else:
    print('Du hast verloren! 😞')
else:
  print('Ungültige Wahl. Spiel vorbei!')
