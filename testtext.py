text = "BNA-VIP-3CJ-18083 172.18.92.61 18083"
tester= "server_name=/Common/GTM_ThaiSummit&vs_name=BNA-VIP-3CJ-18083&ip=172.18.92.61&port=18083"
server = "GTM_ThaiSummit"


Check = text.split(' ')
print(Check)
mem = "server_name=/Common/"+server+"&vs_name="+Check[0]+"&ip="+Check[1]+"&port="+Check[2]
print(mem)