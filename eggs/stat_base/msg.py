from copy import copy

msg_error = {
    # Arguments type or length error
    105: {
        'status': '200',
        'error': 'argument format or length error: {info}'
    },

    # Multi Arguments compare size error
    205: {
        'status': '200',
        'error': 'multi argument order error: {info}'
    },
}


def failure_msg(error_type=None, info=None):
    error_msg = copy(msg_error.get(error_type, {}))
    if error_msg:
        error_msg['error'] = error_msg['error'].format(info=info)
    return error_msg

