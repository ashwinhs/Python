def checkio(data):

    import math

    rdict = {
         0 : '',
         1: 'I',
         5: 'V',
         10: 'X',
         50: 'L',
         100: 'C',
         500: 'D',
         1000: 'M'
         }

    roman = ""
    power = 1
    if data in rdict:
        roman = rdict[data]
    else:
        while data:
            data,d = divmod(data, 10)
            if d == 9:
                roman = rdict[power]+rdict[power*10] + roman
            else:
                value = rdict[max(k for k in rdict if k <= power*10 - (10 - d))]
                if value == "M":
                    d5 = d * rdict[power]
                else:
                    if d > 4:
                        d5 = value + (d - 5) * rdict[power]
                    elif d == 4 and power > 1:
                        d5 = rdict[power] + value
                    elif d == 4 and power == 1:
                        d5 = rdict[power] + rdict[d + 1]
                    else:
                        d5 = d * rdict[power]

                roman = d5 + roman
            power *= 10

    return roman

