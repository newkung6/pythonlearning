import time
from time import gmtime, strftime 



test ="ontheway"
name = format(strftime("%Y%m%d-%H%M%S"))
f = open(format(strftime("%Y%m%d-%H%M%S"))+"CRM.txt","w+")
for x in range(5):
    # time.sleep(3)
    start_time = time.time()
    time.sleep(2)
    # your script
    end_time = time.time()
    elapsed_time = end_time - start_time
    # elapsed_time = format.strftime("%H:%M:%S")
    # print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
    f.write("This is line"+time.strftime("%H:%M:%S",time.gmtime(elapsed_time))+"\n" )
    print(time.strftime("%H:%M:%S",time.gmtime(elapsed_time)))
    print(name)
    # print(elapsed_time)
    # timing = z - a
    # print(a)
    # print(timing)
f.close()

# serverlist =['2','3','4','5','6','7']

# # for x in serverlist:
# #     print (x)