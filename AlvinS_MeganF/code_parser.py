building_code = '20-WBO-109642-809'

#strip, split and join the string
def get_db_link(building_code):
    if len(building_code) !=  17:
        return False 
    if building_code [2] != ['-'] and building_code [6] != ['-'] and building_code [13] != ['-']:
        return False 
    else:
        return building_code[4] + building_code[5] + building_code[10] + building_code[12]