/**
 * Created by csubero on 11/6/2017.
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