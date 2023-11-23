import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

class FreqSummarize:
    def __init__(self,
                 text,
                 retain_percentage,
                 nlp_loader = spacy.load("en_core_web_sm"),
                 stopwords = STOP_WORDS,
                 punctuation = punctuation,
                 selection_metric = nlargest,
                 intialize=False) -> None:
      self.text = text
      self.retain_percentage = retain_percentage
      self.nlp_loader = nlp_loader
      self.stopwords = list(STOP_WORDS)
      self.punctuation = punctuation + '\n'
      self.selection_metric = selection_metric
      if intialize:
        self.generateDoc()
        self.tokenizeWord()
        self.tokenizeSent()
        self.word_freq_table()
        self.summarize()

    def generateDoc(self) -> None:
      self.doc = self.nlp_loader(self.text)

    def tokenizeWord(self) -> None:
      self.word_frequencies = {}
      for word in self.doc:
        temp_word = word.text.lower()
        if temp_word not in self.stopwords:
          if temp_word not in self.punctuation:
            if temp_word not in self.word_frequencies.keys():
              self.word_frequencies[temp_word] = 1
            else:
              self.word_frequencies[temp_word] += 1

    def tokenizeSent(self) -> None:
      self.max_word_freq = max(self.word_frequencies.values())
      for word in self.word_frequencies.keys():
        self.word_frequencies[word] = self.word_frequencies[word] / self.max_word_freq
      self.sentence_tokens = [sentence for sentence in self.doc.sents]

    def word_freq_table(self) -> None:
      self.sentence_scores = {}
      for sentence in self.sentence_tokens:
        for word in sentence:
          temp_word = word.text.lower()
          if temp_word in self.word_frequencies.keys():
            if sentence not in self.sentence_scores.keys():
              self.sentence_scores[sentence] = self.word_frequencies[temp_word]
            else:
              self.sentence_scores[sentence] += self.word_frequencies[temp_word]

    def summarize(self) -> None:
      self.select_length = int(len(self.sentence_tokens) * self.retain_percentage)
      self.summary = self.selection_metric(self.select_length, self.sentence_scores, key = self.sentence_scores.get)
      self.final_summary = [word.text for word in self.summary]
      self.final_summary = " ".join(self.final_summary)
