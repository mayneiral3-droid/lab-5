def ty4(spicok):
    resylt = spicok
    while True:
     start = resylt.find("(")
     end = resylt.find(")")
     if start != -1 and end != -1 and end > start:
         resylt = resylt.replace(resylt[start:end+1])
     break