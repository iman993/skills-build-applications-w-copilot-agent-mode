
import logo from './octofitapp-small.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="OctoFit Logo" />
        <h1 className="ms-3">OctoFit Tracker</h1>
      </header>
      <main className="container mt-4">
        <div className="card p-4">
          <h2>Welcome to OctoFit!</h2>
          <p className="lead">Track your fitness, join teams, and compete on the leaderboard.</p>
          <a className="btn btn-primary" href="#">Get Started</a>
        </div>
      </main>
    </div>
  );
}

export default App;
