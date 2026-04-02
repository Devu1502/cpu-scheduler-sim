import { useState } from "react";

function App() {
  const [results, setResults] = useState([]);
  const [metrics, setMetrics] = useState(null);

  const [processes, setProcesses] = useState([
    { pid: "P1", arrival_time: 0, burst_time: 5 },
    { pid: "P2", arrival_time: 1, burst_time: 4 },
  ]);

  const [algorithm, setAlgorithm] = useState("FCFS");

  const addProcess = () => {
    setProcesses([
      ...processes,
      { pid: `P${processes.length + 1}`, arrival_time: 0, burst_time: 1 },
    ]);
  };

  const updateProcess = (index, field, value) => {
    const updated = [...processes];
    updated[index][field] = value;
    setProcesses(updated);
  };

  const handleRun = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/schedule", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          algorithm,
          processes,
        }),
      });

      const data = await response.json();

      setResults(data.results);
      setMetrics(data.metrics);

    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>CPU Scheduling Simulator</h1>

      <h3>Processes</h3>
      {processes.map((p, i) => (
        <div key={i}>
          {p.pid}
          <input
            type="number"
            value={p.arrival_time}
            onChange={(e) => updateProcess(i, "arrival_time", +e.target.value)}
            placeholder="Arrival"
          />
          <input
            type="number"
            value={p.burst_time}
            onChange={(e) => updateProcess(i, "burst_time", +e.target.value)}
            placeholder="Burst"
          />
        </div>
      ))}

      <button onClick={addProcess}>Add Process</button>

      <h3>Algorithm</h3>
      <select value={algorithm} onChange={(e) => setAlgorithm(e.target.value)}>
        <option>FCFS</option>
        <option>SJF</option>
        <option>RR</option>
        <option>SRTF</option>
        <option>HRRN</option>
      </select>

      <br /><br />
      <button onClick={handleRun}>Run Simulation</button>

      {metrics && (
        <div>
          <h3>Metrics</h3>
          <p>AWT: {metrics.AWT.toFixed(2)}</p>
          <p>ATT: {metrics.ATT.toFixed(2)}</p>
          <p>CPU Utilization: {metrics["CPU Utilization"].toFixed(2)}</p>
          <p>Throughput: {metrics.Throughput.toFixed(2)}</p>
        </div>
      )}

      {results.length > 0 && (
        <div>
          <h3>Results</h3>
          <table border="1">
            <thead>
              <tr>
                <th>PID</th>
                <th>Start</th>
                <th>Finish</th>
                <th>Waiting</th>
                <th>Turnaround</th>
              </tr>
            </thead>
            <tbody>
              {results.map((r, i) => (
                <tr key={i}>
                  <td>{r.pid}</td>
                  <td>{r.start_time}</td>
                  <td>{r.finish_time}</td>
                  <td>{r.waiting_time}</td>
                  <td>{r.turnaround_time}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default App;
