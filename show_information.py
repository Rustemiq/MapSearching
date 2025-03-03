from distance import lonlat_distance


def show_information(address_ll, org_point, org_name, org_address, org_hours):
    point1 = map(float, address_ll.split(','))
    point2 = map(float, org_point.split(','))
    distance = lonlat_distance(point1, point2)
    print('---Ближайшая аптека---')
    print(f'Адрес: {org_address}\nНазвание:{org_name}')
    print(f'Расстояние до аптеки: {distance} (метров)\nВремя работы: {org_hours}')
