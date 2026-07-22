class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums=[int(tokens[0])]
        length=len(tokens)
        i=1
        while i<length:
            while tokens[i] not in '+-*/':
                nums.append(int(tokens[i]))
                i+=1
                continue
            a=len(nums)-1
            n1=nums.pop(a)
            a-=1
            n2=nums.pop(a)
            if tokens[i]=='+':
                nums.append(n1+n2)
            elif tokens[i]=='-':
                nums.append(n2-n1)
            elif tokens[i]=='*':
                nums.append(n1*n2)
            elif tokens[i]=='/':
                nums.append(int(n2/n1))
            i+=1
        return nums[0]

        '''        
        answer=int(tokens[0])
        
        if num==1:
            return token[0]
        n=tokens[2]
        temp=int(tokens[1])

        for c in range(1,num):
            if tokens[c] in '+-*/':
                n=tokens[c]
                if n=='+':
                    answer=answer+temp
                elif n=='-':
                    answer=answer-temp
                elif n=='*':
                    answer=answer*temp
                elif n=='/':
                    answer=answer/temp
            else:
                temp=int(tokens[c])
            
        return answer
        '''