from project import check_mass, check_height, calculate_bmi, classify_bmi
import pytest

def test_check_mass():
    # Valid metric inputs
    assert check_mass("94", "metric") == 94.0
    assert check_mass("59","metric") == 59.0
    assert check_mass("65.7","metric") == 65.7
    # Invalid metric input with units
    with pytest.raises(ValueError):
        check_mass("65.8kg", "metric")
    # Valid imperial inputs
    assert check_mass("201", "imperial") == 91.2
    assert check_mass("196.97", "imperial") == 89.3
    assert check_mass("170", "imperial") == 77.1
    # Invalid imperial input with units
    with pytest.raises(ValueError):
        check_mass("201 lb", "imperial")
    # Edge cases
    assert check_mass("0", "metric") == 0.0
    assert check_mass("1", "imperial") == round(1 / 2.205, 1)

def test_check_height():
    # Valid metric inputs
    assert check_height("1.98", "metric") == 1.98
    assert check_height("1.78", "metric") == 1.78
    assert check_height("1.60", "metric") == 1.60
    # Invalid metric inputs with incorrect format
    with pytest.raises(ValueError):
        check_height("1,79", "metric")
    with pytest.raises(ValueError):
        check_height("1.90m", "metric")
    # Valid imperial inputs
    assert check_height("6 feet 1 inches", "imperial") == 1.85
    assert check_height("5 feet 9 inches", "imperial") == 1.75
    assert check_height("4 feet 5 inches", "imperial") == 1.35
    # Invalid imperial input with incorrect format
    with pytest.raises(ValueError):
        check_height("6 ft 11 inch", "imperial")
    # Edge cases
    assert check_height("0 feet 0 inches", "imperial") == 0.0
    assert check_height("1 feet 0 inches", "imperial") == 0.30

def test_calculate_bmi():
    # General cases
    assert calculate_bmi(1.90, 95.0) == 26.3
    assert calculate_bmi(1.70, 75.0) == 26.0
    assert calculate_bmi(1.60, 55.0) == 21.5
    assert calculate_bmi(1.99, 85.0) == 21.5
    assert calculate_bmi(1.55, 85.0) == 35.4
    assert calculate_bmi(1.95, 60.0) == 15.8
    # Additional edge cases
    assert calculate_bmi(2.0, 30.0) == 7.5  # Very low BMI
    assert calculate_bmi(0.5, 150.0) == 600.0  # Very high BMI
    assert calculate_bmi(2.5, 50.0) == 8.0  # Edge case

def test_classify_bmi():
    # General classifications
    assert classify_bmi(26.3) == "Overweight"
    assert classify_bmi(41.0) == "Obese Class III"
    assert classify_bmi(21.5) == "Normal"
    assert classify_bmi(17.3) == "Underweight"
    assert classify_bmi(36.4) == "Obese Class II"
    assert classify_bmi(32.3) == "Obese Class I"
    # Boundary cases
    assert classify_bmi(18.5) == "Normal"
    assert classify_bmi(24.9) == "Normal"
    assert classify_bmi(25.0) == "Overweight"
    assert classify_bmi(30.0) == "Obese Class I"
    assert classify_bmi(18.4) == "Underweight"
