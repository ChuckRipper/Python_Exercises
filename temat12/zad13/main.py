from cmath import rect

rotator = rect(1, math.radians(angle_deg))
wyjscie = [point * rotator for point in wejscie]
