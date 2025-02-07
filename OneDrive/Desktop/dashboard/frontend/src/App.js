// src/App.js
import React from 'react';
import Sidebar from './component/Sidebar';
import Dashboard from './component/Dashboard';  // Default import  // Only if you have App.css

function App() {
  return (
    <div className="app-container">
      <Sidebar />
      <div className="main-content">
        <Dashboard />  {/* Using the default Dashboard import */}
      </div>
    </div>
  );
}

export default App;
