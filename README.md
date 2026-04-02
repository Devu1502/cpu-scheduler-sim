# CPU Scheduling Simulator

## Overview

This project implements multiple CPU scheduling algorithms and compares their performance using key metrics such as waiting time, turnaround time, CPU utilization, and throughput.

---


## Tech Stack

- **Frontend:** React (Vite)
- **Backend:** FastAPI (Python)
- **Communication:** REST API (JSON)

---

## Platform and Dependencies

### Platform Tested On
- macOS (Apple Silicon / Intel)
- Node.js v18+
- Python 3.9+

### Dependencies

#### Backend
- fastapi
- uvicorn

#### Frontend
- react
- vite
- npm

---

## Features

- Input custom processes (arrival time, burst time)
- Select scheduling algorithms
- View computed metrics:
  - Average Waiting Time (AWT)
  - Average Turnaround Time (ATT)
  - CPU Utilization
  - Throughput
- Display scheduling results in a table format
- Interactive web-based interface

---

## Algorithms Implemented

- First Come First Serve (FCFS)
- Shortest Job First (SJF)
- Round Robin (RR)
- Shortest Remaining Time First (SRTF)
- Highest Response Ratio Next (HRRN)

## Project Structure
```
cpu-scheduler-sim/
│
├── backend/
│   ├── main.py
│   └── routes/
│       └── scheduler.py
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── scheduler/
│   ├── fcfs.py
│   ├── sjf.py
│   ├── rr.py
│   ├── srtf.py
│   └── hrrn.py
│
├── metrics/
│   └── metrics.py
│
├── models/
│   └── process.py
│
├── report/
│   └── report.tex
│
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+

### 1. Clone the Repository
```bash
git clone 
cd cpu-scheduler-sim
```

### 2. Run the Backend
```bash
cd backend
pip install fastapi uvicorn
uvicorn main:app --reload
```

Backend will be available at: `http://127.0.0.1:8000`

### 3. Run the Frontend
```bash
cd frontend
npm install
npm run dev
```

Frontend will be available at: `http://localhost:5173`

---

## How It Works

1. User enters processes (arrival time, burst time) in the frontend
2. User selects a scheduling algorithm
3. Frontend sends a POST request to the backend at `/schedule`
4. Backend executes the selected algorithm
5. Results and metrics are returned and rendered in the UI

---

## Metrics Explained

| Metric | Description |
|---|---|
| **AWT** | Average time a process waits before execution begins |
| **ATT** | Average total time from process arrival to completion |
| **CPU Utilization** | Percentage of time the CPU is actively executing processes |
| **Throughput** | Number of processes completed per unit of time |

---

## Output

For each simulation, the system displays:

- **Scheduling Table** — start time, finish time, waiting time, and turnaround time per process
- **Performance Summary** — aggregated metrics for cross-algorithm comparison

---

## Author

Devananda Sreekanth
CS 3502
