# US Airline Delay Analysis

## Overview
Introductory SQL project using SQLite and Python to analyze US airline delay data through basic aggregation queries.

## Data Source
This project uses a dataset from Kaggle.
* **Dataset Name:** Airlines Delay
* **Source:** https://www.kaggle.com/datasets/giovamata/airlinedelaycauses
* **Description:** Contains US airline flight data including departure/arrival times, delays, carriers, origins, and destinations, used to analyze airline performance and delay patterns.
## Airline Delay Summary

| Carrier | Avg Arrival Delay (min) | Total Flights |
|--------|--------------------------|--------------|
| YV | 55.29 | 67,063 |
| B6 | 55.09 | 55,315 |
| OH | 51.02 | 52,657 |
| XE | 50.18 | 103,663 |
| UA | 47.78 | 141,426 |
| EV | 47.55 | 81,877 |
| 9E | 46.94 | 51,885 |
| AA | 46.56 | 191,865 |
| OO | 45.37 | 132,433 |
| MQ | 45.30 | 141,920 |
| NW | 43.91 | 79,108 |
| FL | 43.68 | 71,284 |
| CO | 40.57 | 100,195 |
| DL | 39.88 | 114,238 |
| US | 36.45 | 98,425 |
| AS | 36.06 | 39,293 |
| HA | 34.21 | 7,490 |
| WN | 30.09 | 377,602 |
| F9 | 27.94 | 28,269 |
| AQ | 21.26 | 750 |

## Key Insights
- There is significant variation in average arrival delays across airlines.
- Airline performance differs across both delay metrics and total flight volume.
- SQL aggregation queries (GROUP BY, AVG, COUNT) effectively revealed operational differences across carriers.
