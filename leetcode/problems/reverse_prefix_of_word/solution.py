class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        if ch not in word:
            return word 
            
        st = []

        for i in word:
            if i == ch:
                st.append(i)
                break
            else:
                st.append(i)

        leng = len(st)

        list = []

        while st:
            list.append(st.pop())

        for i in range (leng, len(word)):
            list.append(word[i])

        return "".join(list)



    


           

            