import seq_features as sf
import pytest

def test_n_neg_for_single_E_or_D():
    """Perform unit tests on n_neg."""

    assert sf.n_neg('E') == 1
    assert sf.n_neg('D') == 1


def test_n_neg_for_empty_sequence():
    assert sf.n_neg('') == 0  # Edge-case


def test_n_neg_for_longer_sequences():
    assert sf.n_neg('ACKLWTTAE') == 1
    assert sf.n_neg('DDDDEEEE') == 8


def test_n_neg_for_lower_case_sequences():
    assert sf.n_neg('acklwttae') == 1

def test_n_neg_for_invalid_amino_acid():
    """Raises a runtime error and needs pytest
    package.  Also can specify the output of the
    runtime error"""
    with pytest.raises(RuntimeError) as excinfo:
        sf.n_neg('X')
    excinfo.match("X is not a valid amino acid")
