# Personal Expense & Spending Analytics Pipeline

A lightweight financial analytics tool built with Python, Pandas, NumPy, and Matplotlib. It ingests transactional CSV data, cleans and standardizes records, computes essential statistical metrics, and generates visual spending reports.

---

## Features
- **Schema-Agnostic Ingestion:** Dynamic column-detection engine that maps varying header patterns (price, revenue, cost, timestamps, dates) automatically.
- **Data Sanitization:** Regex-driven cleaning pipeline stripping non-numeric formatting (currency symbols, comma delimiters) before numeric conversion.
- **Statistical Array Computations:** Employs NumPy vector methods (`sum`, `mean`, `median`, `std`) on dynamic targets.
- **Adaptive Visual Architecture:** Generates categorical rankings alongside an adaptive secondary panel (chronological time-series or fallback frequency histogram).

## Usage
Run with default sample data:
```bash
python core.py

---

## Tech Stack
- Python 3
- Pandas
- NumPy
- Matplotlib

---

## How to Run the Project

1. **Clone this repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<Shad21-u1>/expense-analyzer.git
   cd expense-analyzer
   ```

2. **Activate the virtual environment:**
   - On Windows:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the pipeline:**
   ```bash
   python core.py
   ```

---

## Sample Visual Output

The script exports the analytical chart automatically:

![Expense Summary](expense_summary.png)