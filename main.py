from get_organizations import get_organizations
from get_toponym import get_toponym
from show_information import show_information
from show_map import show_map

address = input('Адрес -> ')
toponym = get_toponym(address)
address_ll = toponym['Point']['pos'].replace(' ', ',')

organization = get_organizations(address_ll)

point = organization["geometry"]["coordinates"]
org_point = f"{point[0]},{point[1]}"

org_name = organization["properties"]["CompanyMetaData"]["name"]
org_address = organization["properties"]["CompanyMetaData"]["address"]
org_hours = organization["properties"]["CompanyMetaData"]["Hours"]["text"]

pt = "{0},pm2dgl".format(org_point) + '~' + "{0},pmwtm1".format(address_ll)
show_information(address_ll, org_point, org_name, org_address, org_hours)
show_map(pt)
