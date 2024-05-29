$(function () {
    var Notification = function ($el, options) {
        this.$el = $el;
        this.mask = '<{{header|default("h3")}} style="text-align:center;"><i class="{{icon}}"></i>{{text|safe}}</{{header|default("h3")}}>';
        this.options = options;
    }

    Notification.prototype.mask_render = function (options) {
        return $.fn.nunjucks_env.renderString(this.mask, options)
    }

    /* Displays a spinner in the body of the modal, indicating that a data load is in progress. */
    Notification.prototype.loading = function () {
        return this.$el.html($(this.mask_render({header: "h1", icon: 'fa-spinner fa-spin fa fa-large'})));
    }

    /* Action retry for fail. */
    Notification.prototype.retry = function (name, callback) {
        xadmin.retry = xadmin.retry || {};
        xadmin.retry[name] = callback;
        return "xadmin.retry['" + name + "']()";
    }

    /* When a data load failure occurs. */
    Notification.prototype.fail = function (action) {
        return this.$el.html(this.mask_render({
            icon: 'fa fa-exclamation-circle text-danger mr-1',
            classes: 'retry',
            header: "h6",
            text: $.fn.nunjucks_env.renderString('<a href="javascript:({{action}});">{{msg}}</a>', {
                msg: gettext("Failed to load data."),
                action: action
            },),
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
            self.fail(self.retry('xnotification', function () {
                self.load();
            }))
        })
    }

    $(".nav-item .notification-message").click(function () {
        var notification = new Notification($(".dropdown-menu .notification-message-item"));
        notification.load();
    })
})