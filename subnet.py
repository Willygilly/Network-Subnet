def subnet(ipaddr,cidr):
    subNetHosts = (2**(32 - cidr)) # There are 256 available hosts
    octet = list(map(int,ipaddr.split('.'))) # split, apply binary then join again
    octetBit = ''.join(list(map(lambda x: format(x,'b').rjust(8,'0'),octet))) # formating and padding  converting ip address to binary

    hostBitMask = format(subNetHosts,'b').rjust(32,'1')
    netBitMasking = format(int(hostBitMask,2) & int(octetBit,2),'b').rjust(32,'0')
    netAddrBit = f"{netBitMasking[0:8]}.{netBitMasking[8:16]}.{netBitMasking[16:24]}.{netBitMasking[24:32]}"
    netAddr = '.'.join(list(map(lambda x: str(int(x,2)),netAddrBit.split('.'))))

    broadBitMasking= netBitMasking[0:cidr].ljust(32,'1')
    broadAddrBit = f"{broadBitMasking[0:8]}.{broadBitMasking[8:16]}.{broadBitMasking[16:24]}.{broadBitMasking[24:32]}"
    broadAddr = '.'.join(list(map(lambda x: str(int(x,2)),broadAddrBit.split('.'))))

    firstUseAddr = f"{netAddr[0:netAddr.rindex('.')]}.{eval(f"{netAddr[netAddr.rindex('.')+1::]}+1")}" # slice the prefix, add/evalaute the octet of interetst
    lastUseAddr =  f"{broadAddr[0:broadAddr.rindex('.')]}.{eval(f"{broadAddr[broadAddr.rindex('.')+1::]}-1")}"

    return netAddr, broadAddr, firstUseAddr,lastUseAddr
problem1 = subnet('2.134.76.78',26)
problem2 = subnet('169.119.38.121',24)
problem3 = subnet('80.105.255.163',27)
problem4 = subnet('247.90.217.205',25)
problem5 = subnet('157.75.179.248',28)
problem6 = subnet('69.60.141.34',26)
problem7 = subnet('236.45.102.77',29)
problem8 = subnet('147.30.64.119',27)
problem9 = subnet('58.15.26.162',24)
problem10 = subnet('225.0.244.204',27)
#enter your unique code
uniquecode = '76334'

#problem 1
p1Network = problem1[0]
p1Broadcast = problem1[1]
p1First = problem1[2]
p1Last = problem1[3]

#problem 2
p2Network = problem2[0]
p2Broadcast = problem2[1]
p2First = problem2[2]
p2Last = problem2[3]

#problem 3
p3Network = problem3[0]
p3Broadcast = problem3[1]
p3First = problem3[2]
p3Last = problem3[3]

#problem 4
p4Network = problem4[0]
p4Broadcast = problem4[1]
p4First = problem4[2]
p4Last = problem4[3]

#problem 5
p5Network = problem5[0]
p5Broadcast = problem5[1]
p5First = problem5[2]
p5Last = problem5[3]

#problem 6
p6Network = problem6[0]
p6Broadcast = problem6[1]
p6First = problem6[2]
p6Last = problem6[3]

#problem 7
p7Network = problem7[0]
p7Broadcast = problem7[1]
p7First = problem7[2]
p7Last = problem7[3]

#problem 8
p8Network = problem8[0]
p8Broadcast = problem8[1]
p8First = problem8[2]
p8Last = problem8[3]

#problem 9
p9Network = problem9[0]
p9Broadcast = problem9[1]
p9First = problem9[2]
p9Last = problem9[3]

#problem 10
p10Network = problem10[0]
p10Broadcast = problem10[1]
p10First = problem10[2]
p10Last = problem10[3]



"""
example:

uniquecode = 12345

problem 1
p1Network = '199.204.14.128'
p1Broadcast = '199.204.14.255'
p1First = '199.204.14.129'
p1Last =  '199.204.14.254'
"""
