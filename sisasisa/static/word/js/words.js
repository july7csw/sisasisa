function getParameter(name) {
        name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
        var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
            results = regex.exec(location.search);
        return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
    }

$(function () {
    var category = getParameter('category')
    if (category.length !== 0) {
        $('#categoryDefault').text(category)
    }
    var user = $('#user').val()
    var limit = 10


    $(document).on('click', '#limit', function () {
        var list = $('#list')
        list.empty()
        limit += 40
        $.ajax({
            url: '/addHot',
            method: 'POST',
            data: {
                category : category,
                limit : limit
            },
            success: function (data) {
                var content = '';
                var length = data.length
                for(i=0; i<limit; i++){
                    content += '<tr>'
                    content += '<td colspan="2">'
                    content += '<a class="modaldata resultword" data-toggle="modal" data-target="#ssssmodal" data-id="dataidtest">'
                    content += '<h5>'
                    content += i+1+'. '+data[i]
                    content += '</h5><a></td></tr>'
                }
                if(limit === 50) {
                    $('#limitBtnTable').attr('hidden','hidden')
                }
                list.html(content)
            }
        })
    });

    $(document).on('click', '.modaldata',function () {
        var wordvalue = $(this).text();
        var splitindex = wordvalue.indexOf(".")
        var onlyword = wordvalue.slice(splitindex+1)
        var word = onlyword.trim()
        $(".modal-header .modalword").text(word);
        var filepath = '/static/wordCloud/wordCloud_'+word+'.png'
        var img = document.getElementById('wordCloud');
        var req = new XMLHttpRequest()
        req.open('GET',filepath,false)
        req.send(null)
        var headers = req.status
        if (headers===200) {
            img.setAttribute('src',filepath)
        }
        else {
            img.remove()
            $('#wordCloudMsg').text('연관어 이미지가 없습니다.')
        }
        $.ajax({
            url: '/findMeaning',
            method: 'POST',
            data: {
                word: word
            },
            async: false,
            success: function (data) {
                $('#meaning').text(data['word'])
                if (user.length > 0) {
                    $.ajax({
                        url: '/scrapCheck',
                        method: 'POST',
                        data: {
                            word: word
                        },
                        success: function (data) {
                            msg = data['msg']
                            if (msg === 'yes') {
                                $('#scrap').attr('class', 'glyphicon glyphicon-star yellow-star')
                            } else {
                                $('#scrap').attr('class', 'glyphicon glyphicon-star gray-star')
                            }
                        }
                    })
                }
            }
        });
        $(document).on('click', '#scrap', function () {
            if (user.length <= 0) {
                alert("로그인이 필요합니다.");
                window.location.href = 'user/login';
            } else {
                word = $(".modal-header .modalword").text()
                var cls = $('#scrap').attr('class');
                if (cls === 'glyphicon glyphicon-star gray-star') {
                    $.ajax({
                        url: '/insertScrap',
                        method: 'POST',
                        data: {
                            word: word
                        },
                        async: false,
                        success: function (data) {
                            $('#scrap').attr('class', 'glyphicon glyphicon-star yellow-star')
                        }
                    });
                } else if (cls === 'glyphicon glyphicon-star yellow-star') {
                    $.ajax({
                        url: '/deleteScrap',
                        method: "POST",
                        data: {
                            word: word
                        },
                        async: false,
                        success: function (data) {
                            $('#scrap').attr('class', 'glyphicon glyphicon-star gray-star')
                        }
                    });
                }
            }
        });
    })
});