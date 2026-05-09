#finding the most frequent character in the string
#example s='hello'
#output - 'l'
class Solution():

    def is_Frequent(self,s):
        dict={}
        if s=='':
            return 0
        else:
            for i in s:
                if i in dict:
                    dict[i]+=1
                else:
                    dict[i]=1

            return max(dict,key=dict.get)
obj=Solution()
print(obj.is_Frequent(""))