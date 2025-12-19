class Solution:
    def simplifyPath(self, path: str) -> str:
  
        path_res = path.split('/')
        result = []
        for i in range(len(path_res)):
            if path_res[i] == "/" or path_res[i] == "." or path_res[i] == "":
                continue
            if path_res[i] == "..":
                if result == []:
                    continue
                else:
                    result.pop()
            else:
                result.append(path_res[i])
        # if result == []:
        #     return "/"
        
        # res_str = "/"
        # for n in result:
        #     res_str = res_str + n + "/"

        return "/" + "/".join(result)
        
        # return res_str[:-1]



r = Solution()
assert r.simplifyPath("/home/") == "/home"
assert r.simplifyPath("/home//foo/") == "/home/foo"
assert r.simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures"
assert r.simplifyPath("/../") == "/"
assert r.simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d"

print("Tests have passed.")