 # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# line = 'абвQ/абвG/абвT/    /aaaaaа/dddddб/еее!/!ооооо/абв/!ааабббсссс/!ддддд3049'
# print(line)
# words = line.split('/')

# a = 'абв'

# new_words = []

# for word in words:
#     if a not in word:
#          new_words.append(word)
# #print(new_words)
# clean_line=' '.join(new_words)
# print(clean_line)

#  # Измененный код.

line = 'абвQ/абвG/абвT/    /aaaaaа/dddddб/еее!/!ооооо/абв/!ааабббсссс/!ддддд3049'
print(line)
words = line.split('/')
new_words=list(filter(lambda word:'абв' not in word, words))
clean_line=' '.join(new_words)
print(clean_line)
