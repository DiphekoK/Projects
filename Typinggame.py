import time
print("Type the following as fast as you can:")
print("The lazy dog had a very bad day as it was attacked by another dog.")
current_time=time.time()
name=input("")
end_time=time.time()

duration = end_time-current_time
x = round(duration,1)
print(x)