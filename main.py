teksts = input("Ievadi tekstu ")
def replaceTwos(teksts):
  if teksts.count("2")>0:
    teksts = teksts.replace("2", "divi")
    print(teksts)
  else:
    teksts = "Nekas netika aizvietots."
    print(teksts)
  return teksts 
replaceTwos(teksts)
