import basics as bs
import platform
import datetime
x = datetime.datetime.now()

print(x.strftime("%x"))
print(bs.my_function("Jonathan"))
print(platform.system())
print(dir(platform))