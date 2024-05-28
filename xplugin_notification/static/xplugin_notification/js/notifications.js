$(function () {
    $(".nav-item .notification-message").click(function () {
        var notifications = $(".dropdown-menu .notification-message-item");
        $.ajax({
            url: notifications.data("list_url"),
            data: {"plugin": "xnotification"},
        }).done(function (data) {
            $.each(data, function (index, notification) {
                var message = $("#notification_message").template_render$({
                    notification: notification
                });
                notifications.append(message);
            });
        })
    })
})