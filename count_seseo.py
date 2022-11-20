import sys
args = sys.argv

f = open(args[1], 'r', encoding='UTF-8') 

data = f.read()

def count_frequency(str):
  tup = {}
  detect_patterns = [
    'za', 'zu', 'zo', 'ce', 'ci', 'ça', 'çu', 'ço'
  ]

  for pattern in detect_patterns:
    tup[pattern] = 0

  for pattern in detect_patterns:
    tup[pattern] = str.count(pattern)
  return tup

sorted = sorted(count_frequency(data.lower()).items())
# sorted = sorted(count_frequency(data).items(), key=lambda x:x[1], reverse=True)

print(sorted)

with open(args[1].replace('.txt', '') + '_output_seseo.csv', 'w') as f_out:
  for row in sorted:
    print(row)
    print(*row, sep=',', file=f_out)


f.close()