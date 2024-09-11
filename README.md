## The Repository

This Python script includes a system for computing a given security's beta using Yahoo finances API. It also mesures a bias factor which can be used to more accurately assess beta with daily close prices.

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
cd RiskFocus (should be under your current working directory)
```
### Download the requirements and run the program

```
pip install -r packages.txt
python beta_scheduler.py
```
## Initial Version Constraints

The script is set to run daily at 09:31 AM to gather the closing prices of both the selected stock and the S&P 500 index (SPY). 
It will automatically calculate the beta and compare it with Yahoo Finance’s beta, suggesting a bias factor if applicable.
