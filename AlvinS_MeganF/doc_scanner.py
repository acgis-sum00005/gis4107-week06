#find code in text
in_text = 'Top secret message Tx6op3'
code = 'Tx6op3'


def has_x_code(in_text):
    return in_text.find(code) != -1
   


#function to return position of code within string
in_text= 'Hello Tx6op3 my old friend'
code = 'Tx6op3'

def get_x_code_position(in_text):
    position = in_text.find(code) + 1
    if position == 0:
        return -1
    else:
        return position
    

