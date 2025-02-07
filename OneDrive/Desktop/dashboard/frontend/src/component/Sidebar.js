// src/component/Sidebar.js
import React from 'react';
import './Sidebar.css';  // Make sure the CSS file exists or remove this line

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>Sidebar</h2>
      <ul>
        <li>Dashboard</li>
        <li>Settings</li>
        <li>Profile</li>
        <li>Log Out</li>
      </ul>
    </div>
  );
}

export default Sidebar;
