import datetime

data = input()
data_obj = datetime.datetime.strptime(data, "%d.%m.%Y")
print(data_obj.timetuple().tm_yday)
