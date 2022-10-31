def dms2dd(coord):
    coord = coord.strip()
    dms_list = coord.split()
    d_long = int(dms_list[0])
    m_long = int(dms_list[1])
    s_long = int(dms_list[2])
    d_lat = int(dms_list[4])
    m_lat = int(dms_list[5])
    s_lat = int(dms_list[6])
    long = d_long + (m_long/60) + (s_long/3600)
    lat = d_lat + (m_lat/60) + (s_lat/3600)
    if dms_list[3] == 'E' or dms_list[3] == 'e':
        if d_long >=0 and d_long <=180 and m_long >= 0 and m_long <= 59 and s_long >= 0 and s_long <=59:
            long = long
        else:
            return None, None 
    elif dms_list[3] == 'W' or dms_list[3] == 'w':
        if d_long >=0 and d_long <=180 and m_long >= 0 and m_long <= 59 and s_long >= 0 and s_long <=59:
            long = -long
        else:
            return None, None    
    if dms_list[7] == 'N' or dms_list[7] == 'n':
        if d_lat >=0 and d_lat <=90 and m_lat >= 0 and m_lat <= 59 and s_lat >= 0 and s_lat <=59:
            lat = lat  
        else:
            return None, None 
    elif dms_list[7] == 'S' or dms_list[7] == 's':
        if d_lat >=0 and d_lat <=90 and m_lat >= 0 and m_lat <= 59 and s_lat >= 0 and s_lat <=59: 
            lat = -lat
        else:
            return None, None
    return long, lat


    
print(dms2dd('188 45 03 E 89 23 05 S\n'))

    