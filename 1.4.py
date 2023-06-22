# def strcounter(s): #решение за N
#     syms_counter = {}
#     for sym in s:
#         syms_counter[sym] = syms_counter.get(sym, 0)+1
#
#     for sym, count in syms_counter.items():
#         print(sym, count)
#
# strcounter('ABCDAA')


def reversed_str():
    print('Вводные данные: ')
    a = input()
    b = a[::-1]
    if a == b:
        print('True')
    else:
        print('False')
reversed_str()

