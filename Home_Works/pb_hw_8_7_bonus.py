def reverse_words(sentence: str) -> str:
    sentence_revers_words = ' '.join((sentence[::-1]).split()[::-1])

    return sentence_revers_words
