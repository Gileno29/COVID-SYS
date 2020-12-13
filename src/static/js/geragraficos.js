
    function grafico_mortalidade_sintomas(febre, tosse, garganta, dispineia, outros){  
        var Line = document.getElementById("sintomas");
        var chartData = {
        labels: ["Febre","Dor de Garganta", "Tosse", "Dispineia", "Outros"],
        datasets: [{
            data: [0,febre],
            backgroundColor: 'rgba(0, 200, 200, 0.5)',
            
        },
        {
             data: [0,tosse],
            backgroundColor: 'rgba(255, 0, 0 , 0.5)',
            },
            
            {
                data: [0,garganta],
                backgroundColor: 'rgba(0, 255, 127 , 0.5)',
               },
            {
                data: [0,dispineia],
                backgroundColor: 'rgba(255, 0, 255, 0.5)',
               },
            {
                data: [0,outros],
                backgroundColor: 'rgba(255, 255, 0 , 0.5)',
               }   
        ],

        
        Styling:[{
            backgroundColor: 'rgba(0, 2, 200, 0.5)',


        }]

       

        };
        if (Line) {
        new Chart(Line, {
        type: 'line',
        data: chartData,
        styling: {
            backgroundColor: '#20B2AA'
        },
        options: {
            scales: {
            yAxes: [{
                stacked: true,
                ticks:{
                    suggestedMin: 0,
                    suggestedMax: 5
                } 
            },
            
            ]
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
