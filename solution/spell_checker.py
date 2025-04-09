
'''
Create a function that checks if the words in a thesis are spelled correctly.
'''


def spell_checker(thesis_path, dict_path):

  words = list()
  dict_words = list()

  with open (thesis_path,'r') as file:
    for line in file:
      words.extend(line.split(' '))

  with open (dict_path,'r') as file:
    for line in file:
      dict_words.append(line.strip())

  for i in words: if i not in dict_words: print(f'{i} is incorrect word')


spell_checker('thesis.txt','dictionary.txt')