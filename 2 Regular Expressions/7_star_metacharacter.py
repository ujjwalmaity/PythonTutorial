import re

# 0 to multiple repetition of beacon
# eggs
# eggsbeacon
# eggsbeaconbeaconbeaconbeacon
pattern = r'eggs(beacon)*'

if re.match(pattern, 'eggs'):
    print('Match Found')
