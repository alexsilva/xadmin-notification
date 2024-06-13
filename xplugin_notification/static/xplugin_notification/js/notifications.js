$(function () {
    var Notification = function ($el, options) {
        this.$el = $el;
        this.options = options || {};
    }

    Notification.prototype.render = function (elId, options) {
        return $(elId).template_render$(options);
    }

    /* Displays a spinner in the body of the modal, indicating that a data load is in progress. */
    Notification.prototype.loading = function () {
        return this.$el.html(this.render("#notification_admin_loading", {
            classes: 'loading',
        }));
    }

    /* Action retry for fail. */
    Notification.prototype.retry_action = function (name, callback) {
        xadmin.retry = xadmin.retry || {};
        xadmin.retry[name] = callback;
        return "xadmin.retry['" + name + "']()";
    }

    /* When a data load failure occurs. */
    Notification.prototype.fail = function (action) {
        return this.$el.html(this.render("#notification_admin_retry", {
            classes: 'retry',
            retry: {
                text: gettext("Failed to load data."),
                action: action
            }
        }));
    }

    Notification.prototype.load = function () {
        var self = this;
        return $.ajax({
            url: self.$el.data("list_url"),
            data: {"plugin": "xnotification"},
            beforeSend: function () {
                self.loading();
            }
        }).done(function (data) {
            self.$el.empty();
            $.each(data, function (index, notification) {
                var message = $("#notification_message").template_render$({
                    notification: notification
                });
                self.$el.append(message);
            });
        }).fail(function () {
            self.fail(self.retry_action('xnotification', function () {
                self.load();
            }))
        })
    }

    $(".notification-menu").on("show.bs.dropdown", function () {
        var notification = new Notification($(this).find(".dropdown-menu .notification-message-item"));
        notification.load();
    })
})