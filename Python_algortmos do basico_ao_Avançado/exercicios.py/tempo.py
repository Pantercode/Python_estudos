import time


agora = time.time()
print(agora)
print(time.ctime(agora))
agora_2 = time.localtime()
print(agora_2)
time.gmtime(agora)
