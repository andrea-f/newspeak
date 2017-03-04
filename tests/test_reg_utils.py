import pytest

from newspeak import regexp_utils


@pytest.mark.parametrize(('typ', 'words', 'expr'), [
    ('exact', ['w1', 'w2'], '^(w1|w2)$'),
    ('prefix', ['pre', 'ante'], '^(pre|ante)\w+'),
    ('suffix', ['ful', 'post'], '\w+(ful|post)$'),
])
def test_gen_regexp(typ, words, expr):
    assert regexp_utils.gen_regexp(typ, words).pattern == expr
