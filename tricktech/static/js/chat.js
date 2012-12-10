$chat = $('#chat');
id = '';


onSuccess = function(data) {
    $(data).appendTo($chat);
    id = $chat.find('.message').last().data('id');
};

request = function() {
    $.ajax(
        {
        'url': '/ajax_chat/' + id,
        'success': onSuccess,
        'dataType': 'text',
        'cache': false
    }
    );
};


setInterval(request, 5000);
