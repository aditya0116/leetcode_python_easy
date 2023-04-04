class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs):
            comm = ""
            w = sorted(strs, key=len)
            for i in range(len(w[0])):
                flag = 0
                for n in range(len(strs)):
                    if w[0][i] == strs[n][i]:
                        flag += 1
                    else:
                        break
                if flag == len(strs):
                    comm += w[0][i]
                else:
                    break
            return comm
        else:
            return ""


obj = Solution()
print(obj.longestCommonPrefix(["cir","car"]))
