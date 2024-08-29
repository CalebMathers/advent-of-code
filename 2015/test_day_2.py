"""Tests for day 2"""

import pytest
from day_2 import calculate_paper, calculate_total_paper, calculate_ribbon, calculate_total_ribbon


def test_calculate_paper_valid_inputs_one():
    """Tests that calculate paper returns correct num when
    given valid inputs"""
    res = calculate_paper("2x3x4")
    assert res == 58


def test_calculate_paper_valid_inputs_two():
    """Tests that calculate paper returns correct num when
    given valid inputs"""
    res = calculate_paper("1x1x10")
    assert res == 43


def test_calculate_paper_raises_error_missing_dimension():
    """Tests that calculate paper raises an error if three
    dimensions are not given"""
    with pytest.raises(ValueError):
        calculate_paper("20x30")


def test_calculate_total_paper():
    """Tests that the correct total paper amount is returned
    with valid inputs"""
    dimensions = ["2x3x4", "1x1x10"]
    res = calculate_total_paper(dimensions)
    assert res == 101


def test_calculate_ribbon_valid_inputs_one():
    """Test that calculate ribbon returns the correct number
    with valid inputs"""
    res = calculate_ribbon("2x3x4")
    assert res == 34


def test_calculate_ribbon_valid_inputs_two():
    """Test that calculate ribbon returns the correct number
    with valid inputs"""
    res = calculate_ribbon("1x1x10")
    assert res == 14


def test_calculate_total_ribbon_valid_inputs():
    """Tests that the total amount of ribbon is correct
    with valid inputs"""
    dimensions = ["2x3x4", "1x1x10"]
    res = calculate_total_ribbon(dimensions)
    assert res == 48
