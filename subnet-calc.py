#subnet calculator 1.0
#fill in just ip and mask in output.csv, rest will be calculated
import csv


with open('output.csv', 'rb') as F:                 #load csv file to list
    reader = csv.reader(F, delimiter=';')
    
    IPS=[]
    MASKS=[]
    L1=0
    for row in reader:
        L1+=1
        if L1 == 1: continue
        IPS.append(row[0])
        MASKS.append(row[1])



'''
IPS = open('ip.txt', 'r').readlines()           #wersja z odczytem z plikow do list
MASKS = open('mask.txt', 'r').readlines()
'''


with open('output.csv', 'wb') as F:             #open csv file to write
    writer = csv.writer(F,delimiter=';')                                   
    writer.writerow(['IP', 'MASK', 'SUBNET', 'FIRST ADDRESS', 'LAST ADDRESS', 'BROADCAST'])                          #write column headers
    
    for I in range (len(IPS)):                      #go throught lines (i know.. non phytonic)

        IP_OCTET0 = IPS[I].split('.')[0]            # split into octets
        IP_OCTET1 = IPS[I].split('.')[1]
        IP_OCTET2 = IPS[I].split('.')[2]
        IP_OCTET3 = IPS[I].split('.')[3]

        MASK_OCTET0 = MASKS[I].split('.')[0]
        MASK_OCTET1 = MASKS[I].split('.')[1]
        MASK_OCTET2 = MASKS[I].split('.')[2]
        MASK_OCTET3 = MASKS[I].split('.')[3]

        NET_OCTET0 = int(IP_OCTET0) & int(MASK_OCTET0)      # bit AND for IP and MASC
        NET_OCTET1 = int(IP_OCTET1) & int(MASK_OCTET1)
        NET_OCTET2 = int(IP_OCTET2) & int(MASK_OCTET2)
        NET_OCTET3 = int(IP_OCTET3) & int(MASK_OCTET3)
                                                                
############################################################################################ below i get subnet address: NET_STR
        NET = [ str(NET_OCTET0), str(NET_OCTET1), str(NET_OCTET2), str(NET_OCTET3) ]
        NET_STR= '.'.join(NET)
        
        

        NET_OCTET3_2 = NET_OCTET3
        if int(MASK_OCTET3) != 255:                     # if mask is different from /32
            NET_OCTET3_2+=1                             
############################################################################################ below i get first address in subnet: IP_START                   
        IP_START = ''.join(str(NET_OCTET0)+'.'+str(NET_OCTET1)+'.'+str(NET_OCTET2)+'.'+str(NET_OCTET3_2))
       

        WILD_OCTET0 = ~int(MASK_OCTET0) & 255                   #negated mask, '& 255' is necessary for negation
        WILD_OCTET1 = ~int(MASK_OCTET1) & 255
        WILD_OCTET2 = ~int(MASK_OCTET2) & 255
        WILD_OCTET3 = ~int(MASK_OCTET3) & 255
  
   
        END_OCTET0 = int(WILD_OCTET0) | int(NET_OCTET0)        # OR of negated mask and subnet address
        END_OCTET1 = int(WILD_OCTET1) | int(NET_OCTET1)
        END_OCTET2 = int(WILD_OCTET2) | int(NET_OCTET2)
        END_OCTET3 = int(WILD_OCTET3) | int(NET_OCTET3)

############################################################################################ below i get broadcast address: IP_BCAST                                                                                      #ponizej daje broadcast address
        IP_BCAST = ''.join(str(int(END_OCTET0))+'.'+str(int(END_OCTET1))+'.'+str(int(END_OCTET2))+'.'+str(int(END_OCTET3)))


        END_OCTET3_2 = END_OCTET3
        if int(MASK_OCTET3) != 255:                     # o ile maska jest rozna od /32
            END_OCTET3_2-=1                             
############################################################################################ below i get last subnet address: IP_STOP                  
        IP_STOP = ''.join(str(END_OCTET0)+'.'+str(END_OCTET1)+'.'+str(END_OCTET2)+'.'+str(END_OCTET3_2))



     
       
        writer.writerow([IPS[I], MASKS[I], NET_STR, IP_START, IP_STOP, IP_BCAST])                          #write to scv
    

