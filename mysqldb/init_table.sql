-- CREATE DATABASE comnet_wifi;
-- USE comnet_wifi;

CREATE TABLE IF NOT EXISTS signal_strength (
      id INT AUTO_INCREMENT PRIMARY KEY,
      ssid VARCHAR(255),
      strength INT,
      timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
