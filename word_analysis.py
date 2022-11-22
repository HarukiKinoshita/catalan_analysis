import sys
import spacy
args = sys.argv
nlp_ca = spacy.load("ca_core_news_sm")

f_ca = open(args[1], 'r', encoding='UTF-8')
data_ca = f_ca.read()


class Word:
  def __init__(self, text, pos, alpha):
    self.text = text
    self.pos = pos
    self.alpha = alpha

list_ca = []
doc_ca = nlp_ca(data_ca)

for token in doc_ca:
  list_ca.append(Word(token.text, token.pos_, token.is_alpha))

dict = {}
for n in list_ca:
  dict.setdefault(n.pos, 0)
  dict[n.pos] += 1

print(dict)

f_ca.close()