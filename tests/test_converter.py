import pytest
from src.converter import celsius_to_fahrenheit, celsius_to_kelvin, convert, fahrenheit_to_celsius, kelvin_to_celsius

# ── Basic tests using fixtures ──────────────────────────────────

def test_freezing_c_to_f(freezing_point):
    # freezing_point is injected from conftest.py
    assert celsius_to_fahrenheit(freezing_point["C"]) == freezing_point["F"]

def test_boiling_c_to_f(boiling_point):
    assert celsius_to_fahrenheit(boiling_point["C"]) == boiling_point["F"]

# ── Parametrize for multiple conversion cases ───────────────────

@pytest.mark.parametrize("c, expected_f", [
    (0,     32.0),  # freezing
    (100,  212.0),  # boiling
    (-40,  -40.0),  # where C and F are equal
    (37,    98.6),  # body temperature
])
def test_c_to_f_cases(c, expected_f):
    assert celsius_to_fahrenheit(c) == pytest.approx(expected_f, rel=1e-3)


@pytest.mark.parametrize("f, expected_c", [
    (32.0,     0),  # freezing
    (212.0,  100),  # boiling
    (-40.0,  -40),  # where C and F are equal
    (98.6,    37),  # body temperature
])
def test_f_to_c_cases(f, expected_c):
    assert fahrenheit_to_celsius(f) == pytest.approx(expected_c, rel=1e-3)


@pytest.mark.parametrize("c, expected_k", [
    (1,     274.15),   
    (21.5,  294.65),  
    (50,    323.15),    
])
def test_c_to_k_cases(c, expected_k):
    assert celsius_to_kelvin(c) == pytest.approx(expected_k, rel=1e-3)


@pytest.mark.parametrize("k, expected_c", [
    (274.15,    1),   
    (294.65, 21.5),  
    (323.15,   50),    
])
def test_k_to_c_cases(k, expected_c):
    assert kelvin_to_celsius(k) == pytest.approx(expected_c, rel=1e-3)


@pytest.mark.parametrize("value, fromval, toval, expected", [
    (274.15, 'K', 'C',   1),   
    (5, 'C', 'C', 5), 
    (32, 'F', 'c', 0),
    (0, 'c', 'f', 32),    
])
def test_convert(value, fromval, toval, expected):
    assert convert(value, fromval, toval) == pytest.approx(expected, rel=1e-3)



# ── Edge cases ──────────────────────────────────────────────────

@pytest.mark.edge
def test_absolute_zero_kelvin():
    assert celsius_to_kelvin(-273.15) == pytest.approx(0.0)

@pytest.mark.edge
def test_below_absolute_zero_raises():
    with pytest.raises(ValueError):
        celsius_to_kelvin(-300)


@pytest.mark.edge
def test_below_absolute_zero_raises_2():
    with pytest.raises(ValueError):
        kelvin_to_celsius(-300)

# TODO: add more tests to reach ≥ 80% coverage!
# Suggestions:
#   - test fahrenheit_to_celsius X
#   - test kelvin_to_celsius     X
#   - test convert() for all 6 unit-pair combinations
#   - test convert() with same-unit (e.g. 'C' → 'C')
#   - test convert() raises ValueError for unknown unit 'X'
#   - test negative Kelvin raises ValueError