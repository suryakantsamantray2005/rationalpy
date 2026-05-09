class Solution():

    def is_Frequent(self,s):
        dict={}
        if s=='':
            return None
        else:
            for i in s:
                if i in dict:
                    dict[i]+=1
                else:
                    dict[i]=1

            max_char=''
            max_count=0
            for i,count in dict.items():
                if count>max_count:
                    max_char=i
                    max_count=count
            return max_char,max_count
        
obj=Solution()
print(obj.is_Frequent("helloool"))