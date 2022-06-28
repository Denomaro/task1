#Лекция 1

#Задание 2

def int32_to_ip(int32):
    return '.'.join([str((int32 >> 8 * i) % 256) for i in [3, 2, 1, 0]])

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"