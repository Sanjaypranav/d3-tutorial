// Fetch data from the API endpoint and display it in the container
(async function () {
    const response = await fetch('http://127.0.0.1:5000/api/getData');
    const data = await response.json();

    const dataContainer = d3.select('#data-container');

    dataContainer.selectAll('p')
        .data(data)
        .enter()
        .append('p')
        .text(d => JSON.stringify(d));
})();
