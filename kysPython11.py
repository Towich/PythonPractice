import struct


def read_b_structures(data, address):
    result = []
    for b_structure in struct.unpack(">4H", data[address: address + 8]):
        b1 = struct.unpack(">b", data[b_structure: b_structure + 1])[0]
        b2 = struct.unpack(">f", data[b_structure + 1: b_structure + 5])[0]
        result .append({
            "B1": b1,
            "B2": b2
        })
        return result

def main(data):
    a1 = read_b_structures(data, 4)
    a2 = struct.unpack(">h", data[12:14])[0]
    a3 = struct.unpack(">7s", data[14:21])[0].decode()
    a5 = struct.unpack(">f", data[71:75])[0]

    c1 = struct.unpack(">q", data[21:29])[0]
    c2 = struct.unpack(">Q", data[29:37])[0]
    c3 = list(struct.unpack(">7H", data[37:51]))

    d1 = struct.unpack(">2I", data[51:59])
    d1 = list(struct.unpack(">" + 'b' * d1[0], data[d1[1]: d1[1] + d1[0]]))
    d2 = struct.unpack(">2H", data[59:63])
    d2 = list(struct.unpack(">" + 'i' * d2[0], data[d2[1]: d2[1] + d2[0] * 4]))
    d3 = struct.unpack(">d", data[63:71])[0]

    out_dict = {
        "A1": a1,
        "A2": a2,
        "A3": a3,
        "A4": {
            "C1": c1,
            "C2": c2,
            "C3": c3,
            "C4": {
                "D1": d1,
                "D2": d2,
                "D3": d3,
            }
        },
        "A5": a5
    }
    return out_dict

print(main((b'BOUG\x00K\x00P\x00U\x00Zb"jbazxvh\x12\x01\xe3\x0e\xf6\x0b\x03\xfbg\xaa\x01'
 b'2\xca\xeb0\ti\x07\xaf\xf6\xe3\xfe\x11XX\x81\xadH0\x90\x00\x00\x00\x02\x00'
 b"\x00\x00_\x00\x02\x00a?\xd4\xeaB\xfeh\x99 >z\x04\x81\xfd?Y\x07g\xa8?'\xca"
 b'\x931>5isw\xbe\xecG\x84\t\xebn}\xa0\xb9D\x01\xa3\x1c')))
