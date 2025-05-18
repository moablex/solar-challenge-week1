# Solar Challenge Week 1

This repository contains the setup for the Solar Challenge Week 1 project, including a Python virtual environment and basic CI pipeline.

## Setup Instructions

## Prerequisites

- Python 3.12.7 or higher
- Git

# 1 . Clone the Repository:

```bash
  git clone [https://github.com/moablex/solar-challenge-week1.git]
  cd solar-challenge-week1
```

# 2 . Create and Activate Virtual Environment:

Create:

```bash

python -m venv venv

```

# Activate:

- Windows:

```bash
venv\Scripts\activate

```

- macOS/Linux:

```bash
source venv/bin/activate
```

# Install Dependencies:

```bash
pip install -r requirements.txt
```

# Verify Setup:

Check Python version:

```bash
python --version
```

# Folder Structure

```plain
solar-challenge-week1/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .vscode/
├── data/
├── notebooks/
├── src/
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```
