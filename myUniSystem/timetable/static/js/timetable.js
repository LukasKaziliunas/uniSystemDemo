$(document).ready(function () {

        var start = new Date(2020, 8, 1).getTime() //semestro pradzia

       // var week = calculateWeek(start)
          var week = 1; // visada yra pirma savaite

        get_timetable(week)

        change_week_number(week)

        $('#arrow-left').on('click', function () {
            week--
            week = clamp(week , 1, 16)
            get_timetable(week)
            change_week_number(week)
        })

        $('#arrow-right').on('click', function () {
            week++
            week = clamp(week , 1, 16)
            get_timetable(week)
            change_week_number(week)
        })


        function calculateWeek(semester_start_date) {
            var now = new Date().getTime()
            var diffDays = (now - start) / 86400000       //(1000*60*60*24)
            diffDays = Math.ceil(diffDays)

            var daysToWeeks = Math.ceil(diffDays / 7)

            return daysToWeeks
        }

        function get_timetable(week) {
            $.ajax({
                type: 'GET',
                data: {
                    'week': week
                },
                url: 'http://127.0.0.1:8000/timetable/ajax/load_week/',
                success: function (data) {
                    $("#timetable").html(data);
                },
                error: function () {
                    alert('error loading data');
                }
            });
        }

        function clamp(numb, min, max)
        {
            if(numb < min)
            return min
            else if (numb > max)
            return max
            else
            return numb
        }

        function change_week_number(week)
        {
            $("#week-numb").html("week : " + week);
        }


    });