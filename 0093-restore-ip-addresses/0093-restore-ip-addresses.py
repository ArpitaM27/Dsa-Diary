class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:

        res = []

        def answer(i,temp):

            if len(temp)==4:
                if i == len(s):

                    res.append(".".join(temp[:]))
                return

            for j in range(i+1,min(i+4,len(s)+1)):

                digit = s[i:j]

                if len(digit)>1 and digit[0]=="0":

                    continue

                if int(digit)>255:

                    continue

                temp.append(digit)
                answer(j,temp)
                temp.pop()

        answer(0,[])
        return res