def popular_words(text: str, words: list[str]) -> dict[str, int]:
    list_text = text.lower().split()

    dict_word_count = {word: list_text.count(word) for word in words}

    return dict_word_count


assert (popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                      ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}), 'Test1'
print('OK')
