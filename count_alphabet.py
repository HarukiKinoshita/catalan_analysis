import sys
args = sys.argv

f = open(args[1], 'r', encoding='UTF-8') 

data = f.read()

def count_frequency(str):
  dict = {}
  alphabet = [
    'ñ','á','é','í','ó','ú','ü','à','ü','ç','è','ò',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
  ]

  for n in alphabet:
    dict[n] = 0

  for n in str:
    if n in alphabet:
      dict[n] += 1
  return dict


sorted = sorted(count_frequency(data.lower()).items())
# sorted = sorted(count_frequency(data).items(), key=lambda x:x[1], reverse=True)

with open(args[1].replace('.txt', '') + '_output.csv', 'w') as f_out:
  for row in sorted:
    print(*row, sep=',', file=f_out)

f.close()