import pytest
from drone_flight_calculator.flight_calculator import calculate_flight_time


def test_calculate_flight_time_zero_weight_returns_180():
    assert calculate_flight_time(0) == 180.0


def test_calculate_flight_time_regular_weight_uses_formula():
    assert calculate_flight_time(100) == 170.0
    assert calculate_flight_time(250) == 155.0


def test_calculate_flight_time_handles_fractional_weights():
    assert calculate_flight_time(123.5) == pytest.approx(167.65)


def test_calculate_flight_time_negative_weight_raises_value_error():
    with pytest.raises(ValueError, match="Payload weight must be non-negative."):
        calculate_flight_time(-1)


def test_calculate_flight_time_large_weight_clamps_to_zero():
    assert calculate_flight_time(1801) == 0.0
    assert calculate_flight_time(5000) == 0.0