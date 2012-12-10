// Constants
FADEINSPEED = 1000;

$chat = $('#chat');
id = '';

replaceChatWithoutMagic = function() {
    $magic = $chat.find('#magic');
    $chats = $magic.children();
    $magic.remove();
    $chats.appendTo($chat);
};

onSuccess = function(data) {
    // If it is blank, 1 is returned?
    if (data.length <= 1) {
        return;
    }
    // We add magic so we can keep track of our "latest" elements, and remove magic after fadein
    $('<div id="magic" class="hide">' +data + '</div>').appendTo($chat);
    $chat.find('#magic').fadeIn(FADEINSPEED, replaceChatWithoutMagic);
    // update the latest ID for the next request
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
