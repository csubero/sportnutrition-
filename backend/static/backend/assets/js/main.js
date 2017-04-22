/**
 * Created by csubero on 22/4/2017.
 */
function show_notification(message, type, title) {
    $.notify(
        {
            title: title,
            message: message,
        },
        {
            type: type,
            placement: {
                from: 'top',
                align: 'center'
            }
        }
    );
}