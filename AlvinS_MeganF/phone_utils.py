#valid phone numbers are NNN-NNN-NNNN
phone_number = 600-600-6000

def is_valid_phone_number(phone_number):
    #assess if p_n is 12 digits
        #assess if dashes are in right position
            # use .replace and assess .isdigit
   if len(phone_number) == 12:
        return True
    else:
        return False

