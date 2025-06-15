"""
fuzzy.py

This module provides fuzzy logic utilities for water quality assessment.
It defines membership functions, fuzzy sets (ranges) for pH, TDS, and temperature,
and implements fuzzy inference and defuzzification logic.
"""

import numpy as np

# Fuzzy set definitions for pH values.
# Keys are linguistic terms, values are parameter lists for membership functions.
PH_RANGES = {
    "Asam": [0, 0, 6, 7],  # Acidic
    "Optimal": [6, 7, 8],  # Optimal
    "Basa": [7, 8, 14, 14]  # Basic
}

# Fuzzy set definitions for TDS (Total Dissolved Solids) values.
TDS_RANGES = {
    "Sangat Rendah": [0, 0, 400, 600],  # Very Low
    "Rendah": [400, 600, 900, 1100],  # Low
    "Optimal": [900, 1100, 1800, 2000],  # Optimal
    "Tinggi": [1800, 2000, 3000, 3000]  # High
}

# Fuzzy set definitions for water temperature values.
TEMPERATURE_RANGES = {
    "Dingin": [0, 0, 23, 25],  # Cold
    "Optimal": [24, 27, 30],  # Optimal
    "Panas": [28, 30, 45, 45]  # Hot
}

# Fuzzy output ranges for the final classification.
OUTPUT_RANGES = {
    "Tidak Normal": [0, 1, 2],
    "Normal": [1, 2, 3]
}


def explode_array(arr):
    """
    Flattens and converts an array-like input to a list of floats.

    Args:
        arr: Array-like input.

    Returns:
        List of floats.
    """
    return [float(i) for i in np.array(arr).flatten()]


def membership_function(x, params):
    """
    General membership function for triangular or trapezoidal fuzzy sets.

    Args:
        x: Input value.
        params: List of parameters (length 3 for triangle, 4 for trapezoid).

    Returns:
        Membership degree (float).
    """
    if len(params) == 3:
        a, b, c = explode_array(params)
        return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)
    elif len(params) == 4:
        a, b, c, d = explode_array(params)
        return np.maximum(np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)), 0)
    return None


def fungsi_segitiga(x, params):
    """
    Triangular membership function.

    Args:
        x: Input value.
        params: List of three parameters [a, b, c].

    Returns:
        Membership degree (float).
    """
    a, b, c = [np.array(p) for p in params]
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)


def fungsi_trapezium(x, params):
    """
    Trapezoidal membership function.

    Args:
        x: Input value.
        params: List of four parameters [a, b, c, d].

    Returns:
        Membership degree (float).
    """
    a, b, c, d = [np.array(p) for p in params]
    if x <= a or x >= d:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1
    elif c < x < d:
        return (d - x) / (d - c)


def ph_membership(x):
    """
    Calculates the membership degrees for pH value.

    Args:
        x: pH value.

    Returns:
        Dict of membership degrees for each pH fuzzy set.
    """
    return {
        "Asam": fungsi_trapezium(x, explode_array(PH_RANGES["Asam"])),
        "Optimal": fungsi_segitiga(x, explode_array(PH_RANGES["Optimal"])),
        "Basa": fungsi_trapezium(x, explode_array(PH_RANGES["Basa"]))
    }


def tds_membership(x):
    """
    Calculates the membership degrees for TDS value.

    Args:
        x: TDS value.

    Returns:
        Dict of membership degrees for each TDS fuzzy set.
    """
    return {
        "Sangat Rendah": fungsi_trapezium(x, explode_array(TDS_RANGES["Sangat Rendah"])),
        "Rendah": fungsi_trapezium(x, explode_array(TDS_RANGES["Rendah"])),
        "Optimal": fungsi_trapezium(x, explode_array(TDS_RANGES["Optimal"])),
        "Tinggi": fungsi_trapezium(x, explode_array(TDS_RANGES["Tinggi"]))
    }


def temp_membership(x):
    """
    Calculates the membership degrees for temperature value.

    Args:
        x: Temperature value.

    Returns:
        Dict of membership degrees for each temperature fuzzy set.
    """
    return {
        "Dingin": fungsi_trapezium(x, explode_array(TEMPERATURE_RANGES["Dingin"])),
        "Optimal": fungsi_segitiga(x, explode_array(TEMPERATURE_RANGES["Optimal"])),
        "Panas": fungsi_trapezium(x, explode_array(TEMPERATURE_RANGES["Panas"]))
    }


def fuzzy_rules(x1, x2, x3):
    """
    Applies fuzzy inference rules and computes firing strengths.

    Args:
        x1: Dict of TDS membership degrees.
        x2: Dict of pH membership degrees.
        x3: Dict of temperature membership degrees.

    Returns:
        List of dicts with firing strength and output for each rule.
    """
    rules = [
        # (TDS, pH, Temp, Output)
        ("Sangat Rendah", "Asam", "Dingin", 1),
        ("Sangat Rendah", "Asam", "Optimal", 1),
        ("Sangat Rendah", "Asam", "Panas", 1),
        ("Sangat Rendah", "Optimal", "Dingin", 1),
        ("Sangat Rendah", "Optimal", "Optimal", 1),
        ("Sangat Rendah", "Optimal", "Panas", 1),
        ("Sangat Rendah", "Basa", "Dingin", 1),
        ("Sangat Rendah", "Basa", "Optimal", 1),
        ("Sangat Rendah", "Basa", "Panas", 1),
        ("Rendah", "Asam", "Dingin", 1),
        ("Rendah", "Asam", "Optimal", 1),
        ("Rendah", "Asam", "Panas", 1),
        ("Rendah", "Optimal", "Dingin", 1),
        ("Rendah", "Optimal", "Optimal", 1),
        ("Rendah", "Optimal", "Panas", 1),
        ("Rendah", "Basa", "Dingin", 1),
        ("Rendah", "Basa", "Optimal", 1),
        ("Rendah", "Basa", "Panas", 1),
        ("Optimal", "Asam", "Dingin", 1),
        ("Optimal", "Asam", "Optimal", 1),
        ("Optimal", "Asam", "Panas", 1),
        ("Optimal", "Optimal", "Dingin", 1),
        ("Optimal", "Optimal", "Optimal", 2), # Should be 2 for "Optimal" output
        ("Optimal", "Optimal", "Panas", 1),
        ("Optimal", "Basa", "Dingin", 1),
        ("Optimal", "Basa", "Optimal", 1),
        ("Optimal", "Basa", "Panas", 1),
        ("Tinggi", "Asam", "Dingin", 1),
        ("Tinggi", "Asam", "Optimal", 1),
        ("Tinggi", "Asam", "Panas", 1),
        ("Tinggi", "Optimal", "Dingin", 1),
        ("Tinggi", "Optimal", "Optimal", 1),
        ("Tinggi", "Optimal", "Panas", 1),
        ("Tinggi", "Basa", "Dingin", 1),
        ("Tinggi", "Basa", "Optimal", 1),
        ("Tinggi", "Basa", "Panas", 1),
    ]
    results = []
    weights = {
        "ph": 0.2,  # Weight for pH
        "tds": 0.6,  # Weight for TDS
        "water_temp": 0.2  # Weight for temperature
    }
    for rule in rules:
        tds, ph, suhu, output = rule
        if tds in x1 and ph in x2 and suhu in x3:
            firing_strength = min(
                x1[tds] * weights["tds"],
                x2[ph] * weights["ph"],
                x3[suhu] * weights["water_temp"]
            )
            results.append({"firing_strength": firing_strength, "output": output})
    if not results:
        results.append({"firing_strength": 0, "output": 0})
    return results


def defuzzification(rules):
    """
    Defuzzifies the fuzzy output to a crisp value using weighted average.

    Args:
        rules: List of dicts with 'firing_strength' and 'output'.

    Returns:
        Defuzzified crisp value (float).
    """
    numerator = sum(rule["firing_strength"] * rule["output"] for rule in rules)
    denominator = sum(rule["firing_strength"] for rule in rules)
    if denominator == 0:
        return 0
    return round(numerator / denominator, 2)


def get_z_result(row):
    """
    Calculates the defuzzified water quality result for a given data row.

    Args:
        row (dict): A dictionary containing the keys 'tds', 'ph', and 'water_temp' with their respective values.

    Returns:
        float: The defuzzified crisp value representing the water quality classification.
    """
    tds_mf = tds_membership(row['tds'])
    ph_mf = ph_membership(row['ph'])
    temp_mf = temp_membership(row['water_temp'])
    rules = fuzzy_rules(x1=tds_mf, x2=ph_mf, x3=temp_mf)
    return defuzzification(rules)