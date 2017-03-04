import pytest
import toolz


from newspeak import scoring


TEST_CONFIG = {
    'words': ['find', 'me'],
    'suffix': ['ed', 'other'],
    'prefix': ['un', 'ante']
}


@pytest.mark.parametrize(('word', 'has_suffix'), [
    ('ted', True),
    ('not', False),
    ('ed', False), # is this actually a suffix
])
def test_has_suffix(word, has_suffix):
    assert scoring.Newspeak.has_prop('suffix', TEST_CONFIG['suffix'], word) is has_suffix


@pytest.mark.parametrize(('words', 'count'), [
    (['ted', 'fed', 'hello'], {'suffix': 2}),
    (['find'], {'words': 1}),
    (['one', 'two'], {}),
    (['antelucano'], {'prefix': 1}),
])
def test_counter(words, count):
    counted = scoring.Newspeak.counter(TEST_CONFIG, words)
    filtered = toolz.valfilter(lambda v: v > 0, counted)
    assert filtered == count


@pytest.mark.parametrize(('word', 'clean_text'), [
    ('ted', []),
    ('thisisalongword ee', ['thisisalongword']),
    ('ed', []),
])
def test_clean_text(word, clean_text):
    assert scoring.Newspeak.clean_text(word) == clean_text
