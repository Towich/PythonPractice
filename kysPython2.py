import re


def task6(x):
    if x[4] == "STATA":
        if x[1] == "INI":
            if x[2] == 1965:
                return 0
            elif x[2] == 2004:
                if x[0] == "XML":
                    return 1
                elif x[0] == "C":
                    return 2
            elif x[2] == 1971:
                if x[3] == 1996:
                    return 3
                elif x[3] == 1973:
                    return 4
                elif x[3] == 2011:
                    return 5
        elif x[1] == "OCAML":
            if x[0] == "XML":
                return 6
            elif x[0] == "C":
                if x[2] == 1965:
                    return 7
                elif x[2] == 2004:
                    return 8
                elif x[2] == 1971:
                    return 9
        elif x[1] == "PONY":
            return 10
    elif x[4] == "NINJA":
        return 11
    elif x[4] == "HTML":
        return 12

    return -1  # error


# print(task6(['XML', 'OCAML', 1965, 1996, 'STATA']))
# print(task6(['XML', 'INI', 1971, 1973, 'HTML']))
# print(task6(['C', 'INI', 1971, 1996, 'STATA']))
# print(task6(['XML', 'OCAML', 1965, 1996, 'NINJA']))
# print(task6(['C', 'OCAML', 1965, 1973, 'STATA']))


#  <%<block> global inbe_748 is #(mausan_943 ; rivequ_640 ; mainbi ; sori_999 ); </block>.<block> global aveso is #( tees_80 ; lave_569 ; xeatar_155 ; rius);</block>. <block>global raesat_468 is #(aateser_421 ; ardi_270 ; zain;usdice);</block>. %>
# <%<block> global eszaer is #( ened_929 ;quaxe ); </block>. <block> global esed is#( tice_870;isis_220); </block>. %>

#  global\s(\w+)\s\w+\s#\S\s?(\w+) ; (\w+) ; (\w+) ?;? ?(\w+)
#  global\s(\w+)\s?\w+\s?#\S\s?(\w+)? ?;? ?(\w+)? ?;? (\w+)? ?;? ?(\w+)?
def task8():
    s1 = "<%<block> global inbe_748 is #(mausan_943 ; rivequ_640 ; mainbi ; sori_999 ); </block>.<block> global aveso " \
         "is #( tees_80 ; lave_569 ; xeatar_155 ; rius);</block>. <block>global raesat_468 is #(aateser_421 ; " \
         "ardi_270 ; zain;usdice);</block>. %> "
    s2 = "<%<block> global eszaer is #( ened_929 ;quaxe ); </block>. <block> global esed is#( tice_870;isis_220); " \
         "</block>. %> "

    result = re.findall(r"<block> ?global\s(\w+)\s?\w+\s?#\S\s?(\w+)? ?;? ?(\w+)? ?;? ?(\w+)? ?;? ?(\w+)? ?\); ?<\/block>\.", s2)

    newResult = []


    return result


print(task8())
