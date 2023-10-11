#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 13:26:49 2022

@author: jannafoy
"""

import math 

def clean_text(txt):
    """ takes a string input, and converts it so that all punctaution is removed,
    and all words are in lowercase via a for loop
    """
    lowercase = txt.lower()
    for symbol in """.,?"'!;:""":
        if symbol in lowercase:
            lowercase = lowercase.replace(symbol,'')
        #for test in s:
         #if symbol in txt:
          #      txt.replace(symbol,'')
           # else:
               #s_new + test
    s = lowercase.split()
    return s

        
def sample_file_write(filename):
     """A function that demonstrates how to write a
        Python dictionary to an easily-readable file.
     """
     d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
     f = open(filename, 'w')      # Open file for writing.
     f.write(str(d))              # Writes the dictionary to the file.
     f.close()        
        
        
def sample_file_read(filename):
    """A function that demonstrates how to read a
       Python dictionary from a file.
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()

    d = dict(eval(d_str))      # Convert the string to a dictionary.

    print("Inside the newly-read dictionary, d, we have:")
    print(d)

def stem(s):
    """ isolates the stems from a word and returns said stem """ 
    if len(s) > 4 and s[-4:] == 'able':
            s = s[:-4]
    elif s[-3:] == 'ing':
        if s[-4] != s[-5]:
                s = s[:-3]
        else:
            s = s[:-4]
    elif s[-3:] == 'ish':
        s = s[:-3]
    elif s[-3:] == 'ers':
        s = s[:-3]
    elif s[-3:] == 'ful':
        s = s[:-3]
    elif s[-2:] == 'ed':
        s = s[:-2]
    elif s[-2:] == 'es':
        s = s[:-2]
    elif s[-2:] == 'er':
        s = s[:-2]
    elif s[-2:] == 'ic':
        s = s[:-2]
    elif s[-1:] == 's' and len(s) > 3:
        s = s[:-1]
    elif s[-1:] == 'e' and len(s) > 3:
        s = s[:-1]
    elif s[-1:] == 'y' and len(s) > 3:
        s = s[:-1] + 'i'
    return s


def compare_dictionaries(d1, d2):
    """ compares two dictionaries and returns how similar the two are
    based on the occurances of the same words 
    """
    score = 0
    total = 0
    if d1 == {}:
           return -50
    elif d2 == {}:
        return -50

    for d in d1:
        total += d1[d]
    for f in d2:
        if f in d1:
            numer = d1[f]
            log = math.log(numer / total)
            numtimes = d2[f]
            score += log * numtimes 
        else:
            log = math.log(0.5/ total)
            numtimes = d2[f]
            score += log * numtimes
          
    return score 
            
       
    

#def similarity_scores(self, other):
 #   if d1 == {}:
  #      return -50
   # score = 0
    
        
        
    
class TextModel:
    def __init__(self, model_name):
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.num_vowels = {}
    def __repr__(self):
       # t = 'text model name: '
      #  nw = 'number of words: '
     #   nwl = 'number of word lengths: '
        #nw_val = len(self.words)
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: '+ str(len(self.word_lengths)) + '\n'
        s += '  number of stems: '+ str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: '+ str(len(self.sentence_lengths)) + '\n'
        s += '  number of vowels:  '+ str(len(self.num_vowels)) + '\n'
        return s
            
        #return str()
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model.
        """
        
        s_sen_len = s.split()
        count = 0
        #length = len(s)
        for r in s_sen_len: #range(length):
            count += 1
            for check in """.?!;:""":
                if check in r:
         #       nums = len(s[])
                    if count not in self.sentence_lengths:
                    
                        self.sentence_lengths[count] = 1
                        count = 0
                #else: 
                  #  count += 1 
            
            
        word_list = clean_text(s)
    
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
        
        for b in word_list:
            if len(b) not in self.word_lengths:
                self.word_lengths[len(b)] = 1
            else:
                self.word_lengths[len(b)] += 1
                
        let_a = 'a'
        let_e = 'e' 
        let_i = 'i' 
        let_o = 'o'
        let_u = 'u'
        word_list = clean_text(s)
        for t in word_list:
            for z in t:
                if let_a == z:
                    if let_a not in self.num_vowels:
                        self.num_vowels[let_a] = 1
                    else:
                        self.num_vowels[let_a] += 1
                if let_e == z:
                    if let_e not in self.num_vowels:
                        self.num_vowels[let_e] = 1
                    else:
                        self.num_vowels[let_e] += 1
                if let_i == z:
                    if let_i not in self.num_vowels:
                        self.num_vowels[let_i] = 1
                    else:
                        self.num_vowels[let_i] += 1
                if let_o == z:
                    if let_o not in self.num_vowels:
                        self.num_vowels[let_o] = 1
                    else:
                        self.num_vowels[let_o] += 1
                if let_u == z:
                    if let_u not in self.num_vowels:
                        self.num_vowels[let_u] = 1
                    else:
                        self.num_vowels[let_u] += 1
         
     
        for u in word_list:
            #if len(u) > 3:
            ste = stem(u)
            if ste not in self.stems:
                self.stems[ste] = 1
            else:
                self.stems[ste] += 1
                
            
            
            # either add a new key-value pair for w
            # or update the existing key-value pair.
    
            # Add code to update self.word_lengths
    def add_file(self, filename):
        """ adds all text in a given file to the model """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        f_read = f.read()
        self.add_string(f_read)
        
    def save_model(self):
        """A function that demonstrates how to write a
           Python dictionary to an easily-readable file.
        """
        wordsfile = self.name + '_' + 'words'
        wordlengthsfile = self.name + '_' + 'word_lengths'
        stemsfile = self.name + '_' + 'stems'
        sentencelengthfile = self.name + '_' + 'sentence_lengths'
        numvowelsfile  = self.name + '_' + 'num_vowels'
        
        f = open(wordsfile, 'w')
        f.write(str(self.words))
        f.close()        
        
        w = open(wordlengthsfile, 'w')
        w.write(str(self.word_lengths))
        w.close()        
        
        s = open(stemsfile, 'w')
        s.write(str(self.stems))
        s.close()
        
        s_l = open(sentencelengthfile, 'w')
        s_l.write(str(self.sentence_lengths))
        s_l.close()
        
        nm = open(numvowelsfile, 'w')
        nm.write(str(self.num_vowels))
        nm.close()
        
    def read_model(self):
        """ reads the given saved model, and converts the string represenation
        of the dictionary back into dictionary format
        """
        wordsfile = self.name + '_' + 'words'
        wordlengthsfile = self.name + '_' + 'word_lengths'
        stemsfile = self.name + '_' + 'stems'
        sentencelengthfile = self.name + '_' + 'sentence_lengths'
        numvowelsfile  = self.name + '_' + 'num_vowels'
        
        f = open(wordsfile, 'r')    # Open for reading.
        wrds = f.read()           # Read in a string that represents a dict.
        f.close()
    
        wrddsdic = dict(eval(wrds))      # Convert the string to a dictionary.
        
        self.words = wrddsdic
        
        w = open(wordlengthsfile, 'r')    # Open for reading.
        wrdleng = w.read()           # Read in a string that represents a dict.
        w.close()
    
        wrdlengdic = dict(eval(wrdleng))      # Convert the string to a dictionary.
        
        self.word_lengths = wrdlengdic
        
        s = open(stemsfile, 'r')
        stm = s.read()
        s.close()
        
        self.stems = dict(eval(stm))
        
        s_l = open(sentencelengthfile, 'r')
        sl = s_l.read()
        s_l.close()
        
        self.sentence_lengths = dict(eval(sl))
        
        nm = open(numvowelsfile, 'r')
        n_m = nm.read()
        nm.close()
        
        self.num_vowels = dict(eval(n_m))
    
    def similarity_scores(self, other):
        """ computes similarity scores for all attributes in the class """
        loglist = []
        
        word_score = [compare_dictionaries(other.words, self.words)]
        
        word_lengths_score = [compare_dictionaries(other.word_lengths, self.word_lengths)]
        
        stems_score = [compare_dictionaries(other.stems, self.stems)]
        
        sentence_lengths_score = [compare_dictionaries(other.sentence_lengths, self.sentence_lengths)]
        
        num_vowels_score = [compare_dictionaries(other.num_vowels, self.num_vowels)]
        
        loglist = word_score + word_lengths_score + stems_score + sentence_lengths_score + num_vowels_score 
        
        return loglist 
    
    def classify(self, source1, source2):
        """ looks at both of the sources and uses similarity_scores
        to determine if self is closer to source1 or source2"""
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        score_for_score1 = 0
        score_for_score2 = 0
        
        for s in range(len(scores1)):
            if scores1[s] > scores2[s]:
                score_for_score1 += 1
            elif scores1[s] < scores2[s]:
                score_for_score2 += 1
        s = [[score_for_score1,source1.name], [score_for_score2, source2.name]]
        s_max = max(s)
                
        
        print('scores for ', source1.name, ':', scores1) #'source 1', ':', scores1)  
        print('scores for ',source2.name, ':', scores2) #  'source 2', ':', scores1) 
        print(self.name, 'is more likely to have come from', s_max[1])
        
        
def test():
    """ does a smaller scale test to make sure code runs """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

def run_tests():
    """ tests my choosen txt files and determines which song has the closests
    fit to a given artists based by comparing lyrics
    """
    source1 = TextModel('szalyrics')
    source1.add_file('szalyrics_file.txt')
    
    print('')

    source2 = TextModel('sminolyrics')
    source2.add_file('sminolyrics_file.txt')
    
    print('')

    new1 = TextModel('ihateu')
    new1.add_file('ihateu_sza.txt')
    print('')
    new1.classify(source1, source2)
    
    print('')
    
    new2 = TextModel('gooddays')
    new2.add_file('gooddays_SZA.txt')
    print('')
    new2.classify(source1, source2)
    
    print('')
    
    new3 = TextModel('pudgy')
    new3.add_file('pudgy_smino.txt')
    print('')
    new3.classify(source1, source2)
    
    print('')
    
    new4 = TextModel('90proof')
    new4.add_file('90proof_smino.txt')
    print('')
    new4.classify(source1, source2)
    
    print('')
    
    new5 = TextModel('conceited')
    new5.add_file('conceited_sza.txt')
    print('')
    new5.classify(source1, source2)
    
    print('')
    
    new6 = TextModel('defibrillator')
    new6.add_file('defibrillator_smino.txt')
    print('')
    new6.classify(source1, source2)
    
    print('')
    
    new7 = TextModel('matinee')
    new7.add_file('matinee_smino.txt')
    print('')
    new7.classify(source1, source2)
    
    print('')
    
    new8 = TextModel('settledown')
    new8.add_file('settledown_smino.txt')
    print('')
    new8.classify(source1, source2)
    
    print('')
    
    new9 = TextModel('toolate')
    new9.add_file('toolate_sza.txt')
    print('')
    new9.classify(source1, source2)
    
    print('')
    
    new10 = TextModel('used')
    new10.add_file('used_sza.txt')
    print('')
    new10.classify(source1, source2)

        
       