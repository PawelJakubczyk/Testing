import Library_Mock.web_data as lm


def user_id():
    import_data = lm.data_to_send()
    if type(import_data) != str:
        raise TypeError('wrong data type')
    forbidden_char = ['$', '#', '%', '^', '&', '?', '<']
    for char in forbidden_char:
        if char in import_data:
            raise ValueError('wrong character in data')
    at_sign_place = import_data.find('@')
    at_sign_place_is_second = import_data.find('@', at_sign_place + 1)
    if at_sign_place_is_second != -1:
        raise ValueError('wrong character in data')
    user_from_mail = import_data[0:at_sign_place]
    return 'hello ' + user_from_mail





