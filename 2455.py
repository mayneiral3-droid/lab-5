def get (tex):
 word = tex.split()
 rt=[]
 for word in word:
  if len(word) > 3:
    et = word.upper()
    rt.append(et)
 return ''.join(rt)