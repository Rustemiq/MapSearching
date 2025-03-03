from get_organizations import get_organizations
from get_toponym import get_toponym
from show_map import show_map

address = input('Адрес -> ')
toponym = get_toponym(address)
address_ll = toponym['Point']['pos'].replace(' ', ',')

organizations = get_organizations(address_ll, 10)

points = "{0},pmwtm1".format(address_ll)
for organization in organizations:
    point = organization["geometry"]["coordinates"]
    org_point = f"{point[0]},{point[1]}"

    org_name = organization["properties"]["CompanyMetaData"]["name"]
    org_address = organization["properties"]["CompanyMetaData"]["address"]
    try:
        org_hours = organization["properties"]["CompanyMetaData"]["Hours"]["text"]
        is_day_and_night = 'круглосуточно' in org_hours
    except KeyError:
        is_day_and_night = None
    if is_day_and_night is None:
        color = 'gr'
    elif is_day_and_night:
        color = 'gn'
    else:
        color = 'bl'
    points += '~' + ("{0},pm2" + color + "m").format(org_point)
show_map(points)
