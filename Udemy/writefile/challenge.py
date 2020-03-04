with open("sample.txt",'w') as example:
    for i in range(2,13):
        for j in range(1,13):
            print("{0} times {1} is {2} \n".format(i, j ,i*j),file=example )
        print("-"*14+"\n",file=example)

