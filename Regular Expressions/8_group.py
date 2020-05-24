import re

# 0 to multiple repetition of eggs
# breadbread
# breadeggsbread
# breadeggseggseggseggsbread
pattern = r'bread(eggs)*bread'

if re.match(pattern, 'breadeggseggsbread'):
    print('Match Found')
