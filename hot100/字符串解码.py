class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ''
        output=''
        #使用栈
        stack_num=[] #数字栈
        char_num=[] #结果栈
        num=0
        for string in s:
            if string.isdigit():#判断数字
                num=num*10+(int)(string)
            elif string=='[':
                stack_num.append(num)
                char_num.append(output)
                num=0
                output=''
                #重新置0
            elif string==']':
                count=stack_num.pop()
                prev_str=char_num.pop()
                output=prev_str+output*count #顺序不能乱
            else:
                output+=string
        return output
        
