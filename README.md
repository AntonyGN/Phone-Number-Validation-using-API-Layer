# Phone Number Validation using API Layer

This Jupyter Notebook demonstrates how to use the API Layer to validate phone numbers.

## Requirements
To run this code, you will need:

- Python 3.6 or higher
- Jupyter Notebook
- The requests and json Python packages

## Installation
You can install the required packages using pip:

```bash
pip install requests
pip install json
```
## Usage
1. Open the Jupyter Notebook file in Jupyter Notebook.
2. Replace the API key in the ```headers``` variable with your own API key. You can get a free API key by signing up at [api-layer.com](https://apilayer.com/).
3. Modify the phone number in the ```params``` variable to the phone number you want to validate.
4. Run the notebook cells in order. The output will indicate whether the phone number is valid or not, and if available, the carrier information.

Note that the code includes error handling and response parsing logic, so you should see helpful error messages if something goes wrong with the API request.
