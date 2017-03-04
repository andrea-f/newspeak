import pytest

from newspeak import scoring


TEST_CONFIG = {
    'words': ['find', 'me'],
    'suffix': ['ed'],
    'prefix': ['un', 'ante']
}


@pytest.mark.parametrize(('words', 'count'), [
    (['ted', 'fed', 'hello'], 2),
    ([], 0),
    (['one', 'two'], 0),
    (['eden'], 0), # it's a prefix not a suffix
])
def test_count_suffix(words, count):
    assert scoring.count_suffix(TEST_CONFIG, words) == count
