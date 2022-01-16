from buzz import generator


def test_sample_single_word():
    test1 = ('foo', 'bar', 'foobar')
    word = generator.sample(test1)
    assert word in test1


def test_sample_multiple_words():
    test2 = ('foo', 'bar', 'foobar')
    words = generator.sample(test2, 2)
    assert len(words) == 2
    assert words[0] in test2
    assert words[1] in test2
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
