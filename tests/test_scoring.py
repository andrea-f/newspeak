import pytest

from newspeak import scoring


TEST_CONFIG = {
    'words': ['find', 'me'],
    'suffix': ['ed'],
    'prefix': ['un', 'ante']
}


@pytest.mark.parametrize(('word', 'has_suffix'), [
    ('ted', True),
    ('not', False),
    ('ed', False), # is this actually a suffix
])
def test_has_suffix(word, has_suffix):
    assert scoring.Newspeak.has_suffix(TEST_CONFIG['suffix'], word) is has_suffix


@pytest.mark.skip
@pytest.mark.parametrize(('words', 'count'), [
    (['ted', 'fed', 'hello'], 2),
    ([], 0),
    (['one', 'two'], 0),
    (['eden'], 0), # it's a prefix not a suffix
])
def test_count_suffix(words, count):
    assert scoring.count_suffix(TEST_CONFIG, words) == count
