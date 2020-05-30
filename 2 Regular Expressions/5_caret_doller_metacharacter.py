import re

# ^ -> starting
# $ -> ending
pattern = r'^gr.y$'

if re.match(pattern, 'grey'):
    print('Match Found')
