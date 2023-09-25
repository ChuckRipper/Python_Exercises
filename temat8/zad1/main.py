# Wariant #1
# def grawitacja_ziemi(m2, r=PROMIEN_ZIEMI):
#     MASA_ZIEMI_LOCAL = MASA_ZIEMI
#     return grawitacja(MASA_ZIEMI_LOCAL, m2, r)

# Wariant #2
def grawitacja_ziemi(m2):
    return grawitacja(MASA_ZIEMI, m2, PROMIEN_ZIEMI)
