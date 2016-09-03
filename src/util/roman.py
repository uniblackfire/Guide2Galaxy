def getRomanNum(RomanStr):
    """Roman numerals will be converted into digital,RomanStr is a RomanString"""
    import re
    if re.search('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', RomanStr) != None:
        NumDic = {"pattern": "", "retNum": 0}
        RomanPattern = {
            "0": ('', '', '', 'M'),
            "1": ('CM', 'CD', 'D', 'C', 100),
            "2": ('XC', 'XL', 'L', 'X', 10),
            "3": ('IX', 'IV', 'V', 'I', 1)
        }
        i = 3
        NumItems = sorted(RomanPattern.items())
        for RomanItem in NumItems:
            if RomanItem[0] != '0':
                patstr = NumDic["pattern"].join(['', RomanItem[1][0]])
                if re.search(patstr, RomanStr) != None:
                    NumDic["retNum"] += 9 * RomanItem[1][4]
                    NumDic["pattern"] = patstr
                else:
                    patstr = NumDic["pattern"].join(['', RomanItem[1][1]])
                    if re.search(patstr, RomanStr) != None:
                        NumDic["retNum"] += 4 * RomanItem[1][4]
                        NumDic["pattern"] = patstr
                    else:
                        patstr = NumDic["pattern"].join(['', RomanItem[1][2]])
                        if re.search(patstr, RomanStr) != None:
                            NumDic["retNum"] += 5 * RomanItem[1][4]
                            NumDic["pattern"] = patstr
            if NumDic["pattern"] == '':
                NumDic["pattern"] = '^'
            tempstr = ''
            sum = 0
            for k in range(0, 4):
                pstr = RomanItem[1][3].join(['', '{']).join(['', str(k)]).join(['', '}'])
                patstr = NumDic["pattern"].join(['', pstr])
                if re.search(patstr, RomanStr) != None:
                    sum = k * (10 ** i)
                    tempstr = patstr
            if tempstr != '':
                NumDic["pattern"] = tempstr
            else:
                NumDic["pattern"] = patstr
            NumDic['retNum'] += sum
            i -= 1
        return NumDic['retNum']
    else:
        print('String is not a valid Roman numerals')
