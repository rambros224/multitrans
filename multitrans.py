# translate a word (form EN) or series of words using --text "word thing", and get multitranslation outputs from 20+langs
# use --list-languages to see the language names from codes
# note, if using more than one word to multi-translate, each word will be translated from EN, and not as a sentance of words

# note on deprecation warning for setuptools - this uses setuptools==80.9.0

import warnings 

# for now, ignore depcration warnings, use setuptools version instead (shouldnt matter after packed to binary)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", module="pkg_resources")

from PyMultiDictionary import MultiDictionary
import pronouncing
import argparse
import os
import cmudict

# for version notes
#from importlib.metadata import version
#print(version("setuptools"))

#from importlib.metadata import version   # will be deprecated
#from importlib.resources import files
#print("using 
# multi trans, translate en word with as many translations possible to cli or text file
# pip install pymultidictionary pronouncing setuptools
# mathematiacl corrleations exist between translations and reverse, where a translation may seem like another languages translation and then can that word can be translated in the same way as the first to find logical connections
parser=argparse.ArgumentParser(description="Translate en to many languages")
parser.add_argument("-t", "--text", type=str,  help="the text to be translated")
parser.add_argument("-l", "--list-languages", action="store_true", help="lists language codes with languae names")
args=parser.parse_args()

language_list='''
af : Afrikaans
ar : Arabic
bn : Bengali
de : German
el : Greek
en : English
es : Spanish, Castilian
fr : French
hi : Hindi
it : Italian
ja : Japanese
jv : Javanese
ko : Korean
mr : Marathi
ms : Malay
no : Norwegian
pl : Polish
pt : Portuguese
ro : Romanian, Moldavian
ru : Russian
sv : Swedish
ta : Tamil
tr : Turkish
uk : Ukrainian
vi : Vietnamese
zh : Chinese
'''

if args.list_languages:
    print(language_list)
    os._exit(0)
    
if not args.text:
    print("invalid arguments")
    os._exit(0)
    
test_words=args.text.split(' ')
if len(test_words) > 3:
    print("Note: You are using more than three words to multitranslate.\nSince this app uses some cloud features, translations may take longer than normal")
 
from PyMultiDictionary import MultiDictionary
import pronouncing

def word_translations(word):
    translations = dictionary.translate("en", word)
    for lang, translated_word in translations:  # Correct unpacking of tuple
        #pronunciation = pronouncing.phones_for_word(translated_word) if lang == "en" else "N/A"
        print(f"{lang}: {translated_word}") # - Pronunciation: {pronunciation}")
    
# needs list of ' ' split words from text
def multi_word_translations(words):
    translations = dictionary.translate("en", "null")
    print(f"en: {' '.join(words)}")
    for lang, translated_word in translations:  # Correct unpacking of tuple
        word_arr=[]
        print(f"{lang}:", end=" ")
        for word in words:
            translations = dictionary.translate("en", word)
            for wlang, wtranslated_word in translations:
                if lang==wlang:
                    print(f"{wtranslated_word}", end=" ")#word_arr.append({word, translated_word})
        print("")
        #for word_arr_word in word_arr:
            #print(f"{word_arr_word}")
 
        #pronunciation = pronouncing.phones_for_word(translated_word) if lang == "en" else "N/A"
        #print(f"{lang}: {translated_word}") # - Pronunciation: {pronunciation}")

dictionary = MultiDictionary()

word = args.text
argwords=word.split(' ')
if len(argwords) > 1:
    print("More than a word used, looping through each word (Note this is not a sentance translation)")
    multi_word_translations(argwords)
else:
    word_translations(word)




