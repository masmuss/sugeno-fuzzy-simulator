# Fuzzy Logic Water Quality Monitoring for Melon Hydroponic Farming

This project implements a fuzzy logic system to monitor water quality based on pH, TDS (Total Dissolved Solids), and temperature. The system uses fuzzy membership functions and rules to evaluate the water quality and provides a defuzzified output.

## Project Structure

- `main.ipynb`: Jupyter notebook containing the main implementation of the fuzzy logic system.
- `fuzzy.py`: Fuzzy utils for implementating into `main.ipynb`
- `evaluation.py`: Evaluation library using confussion matrix method.
- `save_image.py`: Utils for show and save memberships plots.
    
- `data/*`: Folder that containing the water quality monitoring data.
- `data/raw/*`: Folder that containing fuzzy result data.
- `data/result/*`: Folder that containing cleaned fuzzy result that already used for evaluation.
- `images/*`: Folder for exported membership functions plot.

- `requirements.txt`: Required library.
- `README.md`: Project documentation.

## Requirements

- Python 3.x
- Jupyter Notebook
- Pandas
- Matplotlib
- NumPy
- IPython

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/masmuss/sugeno-fuzzy-simulator.git
    cd sugeno-fuzzy-simulator
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Open the Jupyter notebook:
    ```sh
    jupyter notebook main.ipynb
    ```

2. Run the cells in the notebook to execute the fuzzy logic system and visualize the results.

## Functions

- `membership_function(x, params)`: Calculates the membership value for a given input `x` and membership function parameters `params`.
- `fuzzy_rules(x1, x2, x3)`: Defines the fuzzy rules and returns the firing strength and output.
- `defuzzification(rules)`: Performs defuzzification using the Sugeno method (Weighted Average).
- `fungsi_segitiga(x, params)`: Defines a triangular membership function.
- `fungsi_trapezium(x, params)`: Defines a trapezoidal membership function.
- `ph_membership(x)`: Returns the membership values for pH.
- `tds_membership(x)`: Returns the membership values for TDS.
- `temp_membership(x)`: Returns the membership values for temperature.
- `fuzzy_output(row)`: Evaluates the fuzzy output for a given row of data.

## Example

To test the fuzzy logic system with a single set of data:
```python
ph = 6.8
tds = 1000
temp = 25

ph_result = ph_membership(ph)
tds_result = tds_membership(tds)
temp_result = temp_membership(temp)

print(ph_result)
print(tds_result)
print(temp_result)

rule_result = fuzzy_rules(ph_result, tds_result, temp_result)
output = defuzzification(rule_result)
print(output)
```
