// Use D3.js to create visualizations

// Fetch data from the Django API
fetch('/api/data/')
    .then(response => response.json())
    .then(data => {
        // Process data and create visualizations using D3.js
        // Example: create a bar chart
        const chartContainer = d3.select('#chart-container');
        const bars = chartContainer.selectAll('div').data(data).enter().append('div');
        bars.style('width', d => d.intensity * 10 + 'px')
            .text(d => d.country);
    })
    .catch(error => console.error('Error:', error));