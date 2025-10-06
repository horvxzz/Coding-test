word=input()
for c in range(ord('a'),ord('z')+1):
  print(word.find(chr(c)), end=" ")