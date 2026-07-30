class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0' 
        def convert(s):
            res = 0

            for i in range(len(s)):
                if s[i] == '0':
                    num = 0
                elif s[i] == '1':
                    num = 1
                elif s[i] == '2':
                    num = 2
                elif s[i] == '3':
                    num = 3
                elif s[i] == '4':
                    num = 4
                elif s[i] == '5':
                    num = 5
                elif s[i] == '6':
                    num = 6
                elif s[i] == '7':
                    num = 7
                elif s[i] == '8':
                    num = 8
                elif s[i] == '9':
                    num = 9
                res = res * 10 + num 
            
            return res

        def int_to_str(n):
            s_list = []
            while n > 0:
                char = n % 10
                n //= 10

                if char == 0:
                    s_char = '0'
                elif char == 1:
                    s_char = '1'
                elif char == 2:
                    s_char = '2'
                elif char == 3:
                    s_char = '3'
                elif char == 4:
                    s_char = '4'
                elif char == 5:
                    s_char = '5'
                elif char == 6:
                    s_char = '6'
                elif char == 7:
                    s_char = '7'
                elif char == 8:
                    s_char = '8'
                elif char == 9:
                    s_char = '9'
                
                s_list.append(s_char)

            s_list.reverse()
            return ''.join(s_list)
        
        res_int = convert(num1) * convert(num2)
        return int_to_str(res_int)

