class Solution(object):
    def simplifyPath(self, path):
        stack=[]
        curr=""
        for c in path + "/":
            if c=="/":
                #.. aalowel matjich
                if curr=="..":
                    if stack: stack.pop()
                elif curr !="" and curr !=".":
                    stack.append(curr)
                curr=""
            else:
                curr+=c
        return "/" +"/".join(stack)




        