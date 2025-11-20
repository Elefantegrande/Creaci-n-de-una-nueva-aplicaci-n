def get_age_group(age):
    if age < 0:
        return 'invalid'
    elif age <= 12:
        return 'child'
    else:
        return 'desconocido'

 
 def test_get_age_group():
 
     """prueba unitaria para get_age_group"""
 
     assert get_age_group(-1) == 'desconocido'
     assert get_age_group(0) == 'infancia'
     assert get_age_group(14) == 'infancia'
     assert get_age_group(15) == 'juventud'
     assert get_age_group(24) == 'juventud'
     assert get_age_group(25) == 'adulto'
     assert get_age_group(64) == 'adulto'
     assert get_age_group(65) == 'vejez'
     assert get_age_group(80) == 'vejez'
     assert get_age_group(150) == 'desconocido'
