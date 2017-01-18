#!/usr/bin/env python
#Program to convert a sentence to pig latin.

sentence = (input("Please enter a sentence in lower case and no other punctuation: "))
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]
templist = sentence.split(" ")

def vowel1(word):
    for i in range(len(word)):
        if (word[i] in vowels):
            return i

final_sentence = ""
for word in templist:
    vowel1_index = vowel1(word)
    if (word[0] in consonants):
            final_sentence += (word[vowel1_index:] + word[:vowel1_index] + "ay ")
    elif (word[0] in vowels):
        final_sentence += (word + "yay ")

print(final_sentence)
