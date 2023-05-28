from flask import Blueprint, render_template, request, flash, jsonify
import time
import pywifi
from flask import Flask, render_template
import mysql.connector


db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='comnet_wifi'
)


cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS signal_strength (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ssid VARCHAR(255),
        strength INT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

views = Blueprint('views', __name__)

def monitor_signal_strength():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Get the first Wi-Fi interface
    iface.scan()  # Scan for available networks

    cursor.execute('TRUNCATE TABLE signal_strength')

    count = 0
    while (count < 2):
        time.sleep(1)  # Wait for 1 second
        networks = iface.scan_results()
        count += 1
        for network in networks:
            ssid = network.ssid
            signal_strength = network.signal
            # print(f"Network: {ssid}, Signal Strength: {signal_strength} dBm")

            # Insert data into the database
            cursor.execute('INSERT INTO signal_strength (ssid, strength) VALUES (%s, %s)', (ssid, signal_strength))
            db.commit()

@views.route('/')
def display_signal_strength():
    cursor.execute('SELECT id, ssid, strength, timestamp FROM signal_strength')
    data = cursor.fetchall()
    return render_template('dashboard.html', data=data)

monitor_signal_strength()