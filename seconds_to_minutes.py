# Prints the number of minutes and seconds for the given seconds.

import sys

if len(sys.argv) <= 1:
  print('Usage: python seconds_to_minutes.py [seconds]')
  exit(1)

seconds = int(sys.argv[1])

print('%s mins %s secs' %(divmod(seconds, 60)))

