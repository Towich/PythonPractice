from re import match


def main(x):
    match x[4]:
        case "STATA":
            match x[1]:
                case "INI":
                    match x[2]:
                        case 1965:
                            return 0
                        case 2004:
                            match x[0]:
                                case "XML":
                                    return 1
                                case "C":
                                    return 2
                        case 1971:
                            match x[3]:
                                case 1996:
                                    return 3
                                case 1973:
                                    return 4
                                case 2011:
                                    return 5
                case "OCAML":
                    match x[0]:
                        case "XML":
                            return 6
                        case "C":
                            match x[2]:
                                case 1965:
                                    return 7
                                case 2004:
                                    return 8
                                case 1971:
                                    return 9
                case "PONY":
                    return 10
        case "NINJA":
            return 11
        case "HTML":
            return 12


print(main(['XML', 'OCAML', 1965, 1996, 'STATA']))
print(main(['XML', 'INI', 1971, 1973, 'HTML']))
print(main(['C', 'INI', 1971, 1996, 'STATA']))
print(main(['XML', 'OCAML', 1965, 1996, 'NINJA']))
print(main(['C', 'OCAML', 1965, 1973, 'STATA']))