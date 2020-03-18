import time
import os

def do_run(category):
  # Each run increments the filesize by 1 byte
  runs = os.path.getsize('C:/dev/python/%s.txt' % category)
  last_mod = 0
  f = open('%s.txt' % category, 'a')
  
  def last_mod_date():
    return os.stat('C:/games/Diablo II/D2SE/CORES/1.13c/save/Klarabebis.d2x').st_mtime
  
  def print_runs():
    print("%s runs: %d" % (category, runs))
  
  last_mod = last_mod_date()
  print_runs()
  
  while True:
    if last_mod_date() > last_mod:
      last_mod = last_mod_date()
      runs = runs + 1
      print_runs()
      f.write('|')
      f.flush()
    time.sleep(10)
  
  f.close()

# Main
choices = {'1': 'mephisto',
        '2': 'travincal',
        '3': 'ancient tunnels',
        '4': 'andy',
        '5': 'chaos'}
choice = input(str(choices) + ', choose run: ')

do_run(choices[choice])
