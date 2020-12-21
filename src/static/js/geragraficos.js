
    function grafico_mortalidade_sintomas(febre, tosse, garganta, dispineia, outros){  
        var Line = document.getElementById("sintomas");
        console.log('A funcao foi carregada')
        var chartDataSintomas = {
        labels: ["Febre","Dor de Garganta", "Tosse", "Dispineia", "Outros"],
        datasets: [{
            data: [febre, tosse, garganta, dispineia, outros],
            backgroundColor: 'rgba(0, 200, 200, 0.5)'}
        ],


      };
        if (Line) {
        new Chart(Line, {
        type: 'bar',
        data: chartDataSintomas,
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
        type: 'bar',
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

    function mortes_por_idade(idade0A25,idade26A30,idade31A40,idade41A60,maisDe60){  
        var radar = document.getElementById("idade");
        var chartData = {
        labels: ["0-25","26-30","31-40","41-60","mais de 60"],
        datasets: [{
            data: [idade0A25,idade26A30,idade31A40,idade41A60, maisDe60],
            backgroundColor: 'rgba(0, 255,0 , 0.5)',
            //borderColor: '#FA8072',

        },

        /*{
            data: [0,0,3300,8000, 0],
            backgroundColor: 'rgba(0, 100, 100, 0.5)',
            //borderColor: '#FA8072',

        }*/

    
    ],

        
        Styling:[{
            backgroundColor: 'rgba(0, 2, 200, 0.5)',


        }]

       

        };

        if (radar) {
        new Chart(radar, {
        type: 'bar',
        data: chartData,
        styling: {
            backgroundColor: '#20B2AA'
        },
        options: {
            scales: {
            yAxes: [{
                
            }]
            },
            legend: {
            display: false
            }
        }
        });
        } 
    }

    function grafico_mortalidade_mes(janeiro, fevereiro, marco,
    abril, maio, junho, julho, agosto,setembro,outubro,novembro,dezembro){  
        var Line = document.getElementById("mes");
        var chartData = {
        labels: ["janeiro", "fevereiro", "marco",
            "abril", "maio", "junho", "julho", "agosto","setembro","outubro","novembro","dezembro"],
        datasets: [{
            data: [janeiro, fevereiro, marco,
                abril, maio, junho, julho, agosto,setembro,outubro,novembro,dezembro],
            backgroundColor: 'rgba(0, 200, 200, 0.5)',
            
        },],

        
        Styling:[{
            backgroundColor: 'rgba(0, 2, 200, 0.5)',


        }]

       

        };
        if (Line) {
        new Chart(Line, {
        type: 'bar',
        data: chartData,
        styling: {
            backgroundColor: '#20B2AA'
        },
        options: {
            scales: {
            yAxes: [{
                
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

    function grafico_mortalidade_raca(parda, branca, negra,indefinida){  
            var Line = document.getElementById("raca");
            var chartData = {
            labels: ["parda", "branca", "negra","indefinida"],
            datasets: [{
                data: [parda,branca,negra,indefinida],
                backgroundColor: 'rgba(0, 200, 200, 0.5)',
                
            },
                
            ],
    
            
            Styling:[{
                backgroundColor: 'rgba(0, 2, 200, 0.5)',
    
    
            }]
    
           
    
            };
            if (Line) {
            new Chart(Line, {
            type: 'bar',
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