# Logarithmic Scale in Data Visualization

## What this covers
Understanding how logarithms work and applying them to real-world revenue data using Python.

## Problem
Visualizing revenue across companies of vastly different sizes (e.g., Amazon at $386B vs Jindal Steel at $4.7B) 
on a standard bar chart makes smaller values nearly unreadable.

## Solution
Applying a logarithmic Y-axis compresses the scale exponentially, making all values visually comparable.

## Code
- `revenue_log_scale.py` — Loads CSV data and plots a bar chart with a log-scaled Y-axis using pandas and matplotlib
- `revenue1.csv` — Dataset containing company names and revenue figures (in billions USD)

## Key Concept
A log scale progresses as: 1 → 10 → 100 → 1000 (each step = 10× growth)
A linear scale progresses as: 0 → 100 → 200 → 300 (each step = fixed addition)

## Libraries Used
- pandas
- matplotlib

## Output
A bar chart comparing company revenues on a log scale, making large and small values clearly visible side by side.
