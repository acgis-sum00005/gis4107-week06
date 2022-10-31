gpx = 'trkpt lat="45.3888995" lon="-75.7472631"'

def get_coords_from_gpx(gpx):
    if gpx.find('trkpt') == -1:
        return (None, None)
    else:
        gpx_list = gpx.split()
        print(gpx_list)
        lat_list = gpx_list[1]
        print(lat_list)
        lon_list = gpx_list[2]
        print(lon_list)
    return (lat_list[5:-1], lon_list[5:-1])
    
