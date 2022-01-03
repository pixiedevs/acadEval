function makeChart(type, canvas, labels, title, data) {
    let ctx = canvas.getContext('2d');
    new Chart(ctx, {
        type: type,
        data: {
            labels: labels,
            datasets: [{
                label: title,
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.5)',
                    'rgba(255, 159, 64, 0.5)',
                    'rgba(54, 162, 235, 0.5)',
                    'rgba(255, 206, 86, 0.5)',
                    'rgba(75, 192, 192, 0.5)',
                    'rgba(153, 102, 255, 0.5)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function createCharts() {

    let chartBlocks = document.querySelectorAll(".chart-block");

    chartBlocks.forEach(block => {
        let canvas = null;
        block.childNodes.forEach(element => {
            if (element.tagName == 'CANVAS') {
                canvas = element;
            }
        });
        if (canvas == null)
            return;

        if (canvas.tagName != 'CANVAS')
            canvas = block.childNodes[2];

        let type = canvas.getAttribute("type");
        let labels = canvas.getAttribute("labels").split(", ");
        let title = canvas.getAttribute("title").split(", ");
        let data = canvas.getAttribute("data").split(", ");

        makeChart(type, canvas, labels, title, data);
    });
}
