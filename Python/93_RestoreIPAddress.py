"""
 93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter) 

"""



class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        a_result = []
        if len(s) < 4 or len(s) >12:
            return a_result
        else :
            for i in range(1,4):
                a1= s[:i]
                for j in range(1,min(4,len(s)-i)):
                    a2 = s[i:(i+j)]
                    for p in range(1,min(4,len(s)-i-j)):
                        a3 = s[i+j:i+j+p]
                        q = len(s) - i -j -p
                        if q <= 3:
                            a4 = s[-q:]
                            result.append([a1,a2,a3,a4])
                        
            for lst in result:
                for i in lst:
                    if i == '':
                        break
                    elif int(i) > 255:
                        break
                    elif len(i) > 1 and i[0] == '0':
                        break
                else:
                    a_result.append(lst[0]+'.'+lst[1]+'.'+lst[2]+'.'+lst[3])
                    
            return a_result