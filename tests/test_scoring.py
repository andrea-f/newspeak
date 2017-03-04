import pytest

from newspeak import scoring


TEST_CONFIG = {
    'words': ['find', 'me'],
    'suffix': ['ed'],
    'prefix': ['un', 'ante']
}


@pytest.mark.parametrize(('words', 'count'), [
    (['ted', 'fed', 'hello'], 2)
])
def test_count_suffix(words, count):
    assert scoring.count_suffix(TEST_CONFIG, words) == count
