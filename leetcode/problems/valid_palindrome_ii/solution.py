class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l1 = []

        for ch in s:
            l1.append(ch)

        org_l = l1.copy()
        org_r = l1.copy()

        left = 0
        right = len(l1) -1

        while left<right:

            if l1[left] == l1[right]:
                left += 1
                right -= 1

            else:
                org_l.pop(left)
                org_r.pop(right)
                break

        l_final = org_l.copy()
        r_final = org_r.copy()

        left = 0
        right = len(org_l) - 1

        while left<right:
            org_l[left],org_l[right] = org_l[right],org_l[left]
            left +=1
            right -= 1

        left = 0
        right = len(org_r) -1

        while left<right:
            org_r[left],org_r[right] = org_r[right],org_r[left]
            left +=1
            right -= 1

        return org_l == l_final or org_r == r_final