# multitrans
Translate a word or series of Words into multiple languages per command. Cli tool

- this version should output 25 languages per translation in an cli (normal print),
- if more than one word is entered it will output each words translation per language
- --text is required if translating word(s)
- --list-languages is a simple output of the language codes diesplayed from translations

- this program uses some cloud data for translations, as it uses and (within the exe) it uses the module Pymultidict

  If running the script (p313) the following needs to be installed
  pip install MultiDictionary pronounciation, warnings, cmudict  ..
  this is to run the script without editing

  - pronounciation is a possible to do after the literal translations, as well as the possible option to use google translation services

    Release file should work without any dependancies (thank you PyInstaller)
