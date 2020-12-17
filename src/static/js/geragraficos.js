
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

    function mortes_por_idade(idade0A25,idade26A30,idade31A40,idade41A60,maisDe60){  
        var radar = document.getElementById("idade");
        var chartData = {
        labels: ["0-25","26-30","31-40","41-60","mais de 60"],
        datasets: [{
            data: [2000,5000,idade31A40,idade41A60, 6000],
            backgroundColor: 'rgba(0, 255,0 , 0.5)',
            //borderColor: '#FA8072',

        },

        {
            data: [0,0,3300,8000, 0],
            backgroundColor: 'rgba(0, 100, 100, 0.5)',
            //borderColor: '#FA8072',

        }

    
    ],

        
        Styling:[{
            backgroundColor: 'rgba(0, 2, 200, 0.5)',


        }]

       

        };

        if (radar) {
        new Chart(radar, {
        type: 'radar',
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
            data: [0,janeiro],
            backgroundColor: 'rgba(0, 200, 200, 0.5)',
            
        },
        {
             data: [0,fevereiro],
            backgroundColor: 'rgba(255, 0, 0 , 0.5)',
            },
            
            {
                data: [0,marco],
                backgroundColor: 'rgba(0, 255, 127 , 0.5)',
               },
            {
                data: [0,abril],
                backgroundColor: 'rgba(255, 0, 255, 0.5)',
               },
            {
                data: [0,maio],
                backgroundColor: 'rgba(255, 255, 0 , 0.5)',
               },
            {
                data: [0,junho],
                backgroundColor: 'rgba(255, 255, 0 , 0.5)',
               },
            {
                data: [0,julho],
                backgroundColor: 'rgba(255, 255, 0 , 0.5)',
               },
            {
                data: [0,agosto],
                backgroundColor: 'rgba(255, 255, 0 , 0.5)',
               },
            {
                data: [0,setembro],
                backgroundColor: 'rgba(255, 255, 0 , 0.5)',
               },
            {
                data: [0,outubro],
                backgroundColor: 'rgba(255, 255, 0 , 0.5)',
               },
            {
                data: [0,novembro],
                backgroundColor: 'rgba(255, 255, 0 , 0.5)',
               },
            {
                data: [0,dezembro],
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