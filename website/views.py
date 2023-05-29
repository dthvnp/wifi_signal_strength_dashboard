from flask import Blueprint, render_template, jsonify
import time
import pywifi
from flask import render_template
from mysqldb.table import cursor, db

views = Blueprint('views', __name__)

def monitor_signal_strength():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Get the first Wi-Fi interface
    iface.scan()  # Scan for available networks

    cursor.execute('TRUNCATE TABLE signal_strength')

    count = 0
    while (count < 1):
        # time.sleep(1)  # Wait for 1 second
        networks = iface.scan_results()
        count += 1
        for network in networks:
            ssid = network.ssid
            signal_strength = network.signal
            # print(f"Network: {ssid}, Signal Strength: {signal_strength} dBm")

            # Insert data into the database
            cursor.execute('INSERT INTO signal_strength (ssid, strength) VALUES (%s, %s)', (ssid, signal_strength))
            db.commit()

monitor_signal_strength()

@views.route('/')
def display_signal_strength():
    cursor.execute('SELECT id, ssid, strength, timestamp FROM signal_strength')
    data = cursor.fetchall()
    return render_template('dashboard.html', data=data)

@views.route('/api/signal_data')
def get_signal_data():
    cursor.execute('SELECT id, ssid, strength, timestamp FROM signal_strength')
    data = cursor.fetchall()
    return jsonify(data)