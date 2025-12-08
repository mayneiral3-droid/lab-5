import re
def tr (t1):
 entences = re.split(r'(?<=[.?!])+\s', t1.strip())
 for i , entences in enumerate(entences +1):
     print(entences)
 print(f"{len(entences)}")
