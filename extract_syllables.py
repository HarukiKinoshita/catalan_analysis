# Pyphen is a pure Python module to hyphenate words using included or external Hunspell hyphenation dictionaries.
import pyphen
# A python module to reduce Unicode to a 'good enough' ASCII representation
import re
from unidecode import unidecode

import sys
args = sys.argv


def countSyllables(list):
  open_syllables = 0
  syllables = 0

  for syll in list:
    if (len(syll) != 0):
      syllables += 1
      open_syllables += int(syll[-1] not in ['a', 'e', 'i', 'o', 'u'])

  return ["open_syllables: ", open_syllables, "syllables: ", syllables, "percentage: ", open_syllables/syllables]


def countLiasons(list):
  liasons = 0
  for index, word in enumerate(list):
    if index > 1:
      if int(list[index-1][-1] not in ['a', 'e', 'i', 'o', 'u'] and word[0] in ['a', 'e', 'i', 'o', 'u']):
        liasons += 1
  return ["liasons: ", liasons, "length: ", len(list), "percentage: ", liasons/len(list)]


def hyphenate(lang, word_list):
  dict = pyphen.Pyphen(lang=lang)
  syllablized = []

  for word in word_list:
    hyphened = dict.inserted(word)
    if "-" in hyphened:
      list = hyphened.split("-")
      for syll in list:
        syllablized.append(syll)
    else:
      syllablized.append(hyphened)

  return syllablized


def cleanText(str):
  # 音声記号付き文字を変換し、スペースを除く特殊文字を削除
  return re.sub('[ ]+', ' ', re.sub(r'[^a-zA-Z\s]', '', unidecode(str.replace('\n', ''))))


if args[2] in pyphen.LANGUAGES:
  data = open(args[1], 'r', encoding='UTF-8').read()
  splitted_into_words = cleanText(data).split(" ")
  print(countLiasons(splitted_into_words))
  print(countSyllables(hyphenate(args[2], splitted_into_words)))
else:
  print("Dictionary not available:", args[2])