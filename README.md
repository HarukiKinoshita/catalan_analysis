# なぜカタルーニャ語はスペイン語よりも軽やかに聞こえるのか？
*Why does Catalan sounds lighter than Spanish?*


## 指標の定義

### カタルーニャ語・スペイン語とは
- カタルーニャ語
  - カタルーニャ地方で話される言語。行政文書などからテキストデータを集める観点から、狭義のカタルーニャ語とし、バレンシア語やバレアレス諸島方言は含まないことにする。
- スペイン語
  - Castellano（カスティリャーノ）を指す。ただし、この呼称は日本語では一般的ではないことから、便宜上「スペイン語」という表現を用いることにする。

### 「軽やかさ」とは？
- 文中に含まれる音の割合を比較できないか？
- 濁音が少なく、清音が多いのではないか？
  - 清音・濁音・半濁音という分類は日本語のみらしい。
  - スペイン語では有声音と無声音で区別できそう。
  - ceceoとseseoの違いも関係あるかも。
- アルファベットの出現頻度を比較できそう。
  - 「軽やかさ」に貢献すると考えられるアルファベットと、そうでないものに分類して、両言語におけるそれぞれの割合を比較する。
- しかし、音とアルファベットは1対1で対応しているのか？
  - 1つのアルファベットに複数の発音が対応する場合がある。
  - 音と対応するのはアルファベットではなく発音記号。
  - テキストを発音記号に変換するライブラリなどが必要になる。
- 音と1対1対応するようなアルファベットだけに絞って考えられないか？
  - 例えば、スペイン語でzは常に`/θ/`の音となる。
  - カタルーニャ語でçは常に`/s/`の音となる。
  - それらの一部は、対応関係があるのではないか？


## テキストデータ
- スペイン語・カタルーニャ語で同一内容である必要がある。
  - 外交文書、行政文書、契約書、製品の取扱説明書など
    - スペイン1978年憲法 [Castellano](https://www.boe.es/legislacion/documentos/ConstitucionCASTELLANO.pdf) / [Català](https://www.boe.es/legislacion/documentos/ConstitucionCATALAN.pdf)
    - カタルーニャ自治憲章 [Castellano](https://www.parlament.cat/document/cataleg/48146.pdf) / [Català](https://www.parlament.cat/document/cataleg/48089.pdf)
    - イベリア航空 運送約款 [Castellano](https://www.iberia.com/es/condiciones-transporte/) / [Català](https://www.iberia.com/es/condicions-transport/)
- PDFファイルからテキストを抽出するツールがある。


## count_alphabet.py
Run the following command: 
```
> python3 count_alphabet.py "./dataset/estatut/Estatut d'autonomia.txt"
```
You will get `Estatut d'autonomia_output.csv` in the same directory. 


## アルファベット出現頻度に関する他の仮説検証

「軽やかさ」の定量分析とは別に、両言語のアルファベット使用の特徴を検証してみたい。
カタルーニャ語は、
- tが多く、dが少ない
  - -dadで終わる名詞が、-tatになる
- nが少ない
  - -ciónで終わる名詞が、-cióになる
- çが多く、zが少ない
  - スペイン語にはçが存在しない
  - a, o, uの前と語尾でçが使われる
- nとyが多い
  - ñが、nyで置き換わる
- xがある
  - スペイン語にはxが存在しない
  - スペイン語のchが、xで置き換わる	
- oが少ない
  - 動詞から派生している形容詞の語尾の-oが付かない


## 参考資料
- [Seeing Speech: IPA Charts](https://seeingspeech.ac.uk/ipa-charts/)
- [Fonología del español - Wikipedia, la enciclopedia libre](https://es.wikipedia.org/wiki/Fonolog%C3%ADa_del_espa%C3%B1ol)	
- [Fonología del catalán - Wikipedia, la enciclopedia libre](https://es.wikipedia.org/wiki/Fonolog%C3%ADa_del_catal%C3%A1n#Sonorizaci%C3%B3n_y_ensordecimiento)
- [カタルーニャ語 - Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%AB%E3%82%BF%E3%83%AB%E3%83%BC%E3%83%8B%E3%83%A3%E8%AA%9E#%E6%AD%A3%E6%9B%B8%E6%B3%95%E3%81%A8%E7%99%BA%E9%9F%B3)