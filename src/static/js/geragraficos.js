
    function grafico_mortalidade_sintomas(homem, mulher){  
        var chLine = document.getElementById("sintomas");
        var chartData = {
        labels: ["Masculino","Feminino"],
        datasets: [{
            data: [homem, 0],
            backgroundColor: 'rgba(0, 200, 200, 0.5)',
            borderColor: '#FA8072',

        },
        {
            data: [0,mulher],
            backgroundColor: 'rgba(0, 0, 200, 0.5)',
            borderColor: '#FA8072'}],

        
        Styling:[{
            backgroundColor: 'rgba(0, 2, 200, 0.5)',


        }]

       

        };
        if (chLine) {
        new Chart(chLine, {
        type: 'line',
        data: chartData,
        styling: {
            backgroundColor: '#20B2AA'
        },
        options: {
            scales: {
            yAxes: [{
                ticks: {
                beginAtZero: false
                }
            }]
            },
            legend: {
            display: false
            }
        }
        });
        } 
    }


    
    function grafico(homem, mulher){  
        var chLine = document.getElementById("chLine");
        var chartData = {
        labels: ["Masculino","Feminino"],
        datasets: [{
            data: [homem, 0],
            backgroundColor: 'rgba(0, 200, 200, 0.5)',
            borderColor: '#FA8072',

        },
        {
            data: [0,mulher],
            backgroundColor: 'rgba(0, 0, 200, 0.5)',
            borderColor: '#FA8072'}],

        
        Styling:[{
            backgroundColor: 'rgba(0, 2, 200, 0.5)',


        }]

       

        };

        if (chLine) {
        new Chart(chLine, {
        type: 'polarArea',
        data: chartData,
        styling: {
            backgroundColor: '#20B2AA'
        },
        options: {
            scales: {
            yAxes: [{
                ticks: {
                beginAtZero: false
                }
            }]
            },
            legend: {
            display: false
            }
        }
        });
        } 
    }
