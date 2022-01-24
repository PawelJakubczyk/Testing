

def get_country(iso_code=None):
    if type(iso_code) != str:
        raise TypeError('iso_code need to be a string')
    elif len(iso_code) != 2:
        raise ValueError('iso_code need to be 2 characters long')

    country_dict = {
        'DK': {
            'name': 'Denmark'
        },
        'DE': {
            'name': 'Germany'
        }
    }

    if iso_code in country_dict:
        return True, country_dict[iso_code]
    else:
        return False, None


