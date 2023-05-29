function fetchSignalData() {
    // Retrieve the data from backend using AJAX or fetch API
    fetch('/api/signal_data')
        .then(response => response.json())
        .then(data => {
            // Convert the data into the required format for the chart
            const labels = data.map(row => row[1]);
            const signalStrengths = data.map(row => row[2]);

            // Create the chart
            const ctx = document.getElementById('signalChart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Signal Strength',
                        data: signalStrengths,
                        borderColor: 'blue',
                        fill: false
                    }]
                },
                options: {
                    // Configure the chart options as per your requirements
                }
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Call the fetchSignalData function to populate the chart
fetchSignalData();