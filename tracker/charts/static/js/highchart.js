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
            labels : {
                formatter: function() {
                    var myDate = new Date(this.value);
                    console.log(this.value);
                    var newDateMs = Date.UTC(myDate.getUTCFullYear(),myDate.getUTCMonth(),myDate.getUTCDate());
                    return Highcharts.dateFormat('%e. %b',newDateMs);
                }
            },
            title: {
                text: xAxis
            }
        },
        yAxis: {
            title: {
                text: yAxis
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

Highcharts.setOptions({
	global: {
		useUTC: false
	}
});
