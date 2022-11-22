import sys
import spacy
args = sys.argv

trained_pipelines = {
  "ca": "ca_core_news_sm",
  "es": "es_core_news_sm"
}


class LangSet:
  def __init__(self, code, nlp, source_file):
    self.code = code
    self.nlp = nlp
    self.source_file = source_file
    self.doc = nlp(source_file.read())
    self.word_list = []
    self.part_of_speech_dict = {}


class Word:
  def __init__(self, text, pos, alpha):
    self.text = text
    self.pos = pos
    self.alpha = alpha


def main():
  lang = LangSet(
    args[1],
    spacy.load(trained_pipelines[args[1]]),
    open(args[2], 'r', encoding='UTF-8')
  )

  for token in lang.doc:
    lang.word_list.append(Word(token.text, token.pos_, token.is_alpha))
  for n in lang.word_list:
    lang.part_of_speech_dict.setdefault(n.pos, 0)
    lang.part_of_speech_dict[n.pos] += 1

  return lang


if args[1] == '--help' or args[1] == '-h':
  print("> python3 word_analysis_class.py <lang code ('ca', 'es')> <path to input file>")

else:
  lang = main()

  total = sum(lang.part_of_speech_dict.values())
  noun = lang.part_of_speech_dict['NOUN']
  print("lang code | # total | # of nouns | % of nouns")
  print(lang.code, total, noun, noun/total,)

  lang.source_file.close()