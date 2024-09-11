## The Repository

This Python script includes a system for computing a given security's beta using Yahoo finances API. It also mesures a bias factor which can be used to more accurately assess beta with daily close prices.

## Features

- Automated daily updates: Uses the schedule library to update stock and market prices at a set time each day.

- Beta calculation: Computes beta by calculating the covariance between stock and market prices and dividing by the market variance.

- Comparison with Yahoo Finance: The script fetches Yahoo Finance’s beta and compares it with the calculated beta, offering a bias factor to adjust for discrepancies.

- Error handling: Validates ticker symbols before proceeding to avoid invalid inputs.

## Script Design

- User Input: The user inputs the ticker symbol of the stock they want to analyze.

- Data Fetching: The script retrieves the closing price for both the stock and the S&P 500 (SPY) on a daily basis.

- Beta Calculation: It calculates beta based on the collected historical price data and compares it to Yahoo Finance’s beta.

- Bias Factor: If Yahoo Finance's beta is available, the script suggests a bias factor to correct for any differences between the computed beta and the reported beta.

## Installation Guide

Follow the steps below to set up and run the Beta Calculator with Yahoo Finance Comparison project on your local machine.

### Prerequisites

Make sure you have the following installed:

- Python 3.6 or higher
- `pip` (Python package installer)

### Clone the Repository

First, clone the repository to your local machine using the following command in your terminal:

```
git clone https://github.com/Mathieu-Poirier/RiskFocus
```

### Change directory into the repository folder

```
cd RiskFocus 
```
(Should be under your current working directory)

### Download the requirements and run the program

```
pip install -r packages.txt
```
```
python beta_scheduler.py
```
## Initial Version Constraints

The script is set to run daily at 09:31 AM to gather the closing prices of both the selected stock and the S&P 500 index (SPY). 
It will automatically calculate the beta and compare it with Yahoo Finance’s beta, suggesting a bias factor if applicable.
