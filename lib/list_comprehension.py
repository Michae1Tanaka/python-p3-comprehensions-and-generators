#!/usr/bin/env python3


def return_evens(num_list):
    even_list = [num for num in num_list if (num % 2 == 0)]
    return even_list


def make_exclamation(sentence_list):
    new_sentences_list = [string + "!" for string in sentence_list]
    return new_sentences_list
