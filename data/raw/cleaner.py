from sys import argv

s1 = []

path = argv[1]
print(path)

with open(path) as f:
  for l in f.readlines():
    line = l.strip().split("#")[0].replace('www.', '').replace('?s=20','')
    s1.append(line)

ss1 = sorted(set(s1))

with open(path, 'w') as f:
  for line in ss1:
    f.write(line + '\n')