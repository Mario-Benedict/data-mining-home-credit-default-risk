# Project Setup and Installation Guide

This guide provides instructions on how to set up a Python virtual environment, install the required dependencies, and run the program.

## Prerequisites

Before starting, make sure you have the following installed on your system:
* **Python 3.x**
* **pip** (Python package installer)

## Installation Steps

### 1. Clone the Repository
If you haven't already, clone this repository to your local machine and navigate into the directory:

```bash
git clone [https://github.com/Mario-Benedict/data-mining-home-credit-default-risk.git](https://github.com/Mario-Benedict/data-mining-home-credit-default-risk.git)
cd your-repo-name
```

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to avoid dependency conflicts. Run the following command in your project root directory:

```bash
python -m venv venv
```
*(This creates a folder named `venv` containing your isolated Python environment).*

### 3. Activate the Virtual Environment
Before installing any packages or running the code, you must activate the virtual environment. Use the command specific to your operating system:

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source venv/bin/activate
```
*(Once activated, you should see `(venv)` at the beginning of your terminal prompt).*

### 4. Install Dependencies
With the environment activated, install all required packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Running the Program

Make sure your virtual environment is still activated, then execute the main Python script to run the application:

```bash
python main.py
```
*(Note: Change `main.py` if your entry point script has a different name).*

## Deactivating the Environment

When you are finished working, you can safely exit the virtual environment and return to your global Python environment by running:

```bash
deactivate
```