// for adding canvas chart to given id
function makeChart(type, id, labels, title, data) {
    if (window.attendanceChart != null) {
        window.attendanceChart.destroy();
    }

    var ctx = document.getElementById(id).getContext('2d');
    window.attendanceChart = new Chart(ctx, {
        // type: 'pie',
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
function fetchStudentAttendanceData(csrf, url, op) {
    sem = document.getElementById("sem").value
    month = document.getElementById("month").value
    if (url[url.length - 1] != '/') {
        url += '/'
    }
    $.ajax({
        method: 'POST',
        url: url,
        data: {
            csrfmiddlewaretoken: csrf,
            sem: sem,
            month: month,
        },
        success: function (response) {

            if (op == 1) {
                setStudentAttendanceData(response)
            }
        }
    })
}
function setStudentAttendanceData(tableData) {

    // inserting data using ajax
    table_data_body = document.getElementById("table_data_body")
    table_data_body.innerHTML = ''
    var sum = 0
    var total = tableData.length
    for (let idx = 0; idx < tableData.length; idx++) {
        var status = tableData[idx].is_present ? 'Present' : 'Absent';
        sum += tableData[idx].is_present ? 1 : 0
        var row = `<tr>
                <th scope="row">${idx + 1}</th>
                <td>${tableData[idx].date}</td>
                <td>${status}</td>
                </tr>`

        table_data_body.innerHTML += row;
    }
    
    makeChart("doughnut", "marksChart", ['Present', 'Absent'], '', [sum, total- sum]);
}
