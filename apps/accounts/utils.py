from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# this function retrieve ip, location (country) and device from request
def get_session_info(request):
    ip = get_client_ip(request)
    g = GeoIP2()
    try:
        location = g.city(ip)['country_name']
    except AddressNotFoundError:
        location = 'test (maybe localhost)'
    device = request.user_agent.device.family

    return ip, location, device
