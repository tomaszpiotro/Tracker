$(function () {
    $('#chart').highcharts({
        chart: {
            type: type
        },
        title: {
            text: title
        },
        xAxis: {
            type: 'datetime',
            dateTimeLabelFormats: { // don't display the dummy year
                month: '%e %B',
                time: '%r'
            },
            title: {
                text: 'Date'
            }
        },
        yAxis: {
            title: {
                text: 'People online'
            },
            min: 0
        },
        tooltip: {
            formatter: function() {
                return  '<b>' + this.series.name + ': ' + this.y + '</b><br/>' +
                    Highcharts.dateFormat('%e - %B - %Y: %H:%M', new Date(this.x));
            }
        },

        plotOptions: {
            spline: {
                marker: {
                    enabled: false
                }
            }
        },

        series: series
    });
});
