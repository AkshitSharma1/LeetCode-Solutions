class DSU:
    def __init__(self,n):
        self.size = [1]*n
        self.parent = list(range(n))
    def find(self,x):
        #finds the parent of x while performing path compression
        if self.parent[x]==x: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        if x_parent==y_parent: return False
        if self.size[x_parent]<self.size[y_parent]:
            #swap both the nodes
            x_parent,y_parent = y_parent,x_parent
        self.parent[y_parent]=x_parent
        self.size[x_parent]+=self.size[y_parent]
        return True


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        dsu = DSU(n)
        email_to_account = defaultdict(lambda :-1)
        for i in range(n):
            #we go through all accounts and their emails
            for email in accounts[i][1:]:
                if email_to_account[email]==-1: 
                    email_to_account[email] = i
                else:
                    #we perform union
                    dsu.union(i,email_to_account[email])
        
        email_by_root = defaultdict(set)
        for i in range(n):
            for email in accounts[i][1:]:
                #we find the root of i and then append to set
                email_by_root[dsu.find(i)].add(email)
            
        #grouped all emails by root, now we have to return in sorted order
        answer = []
        seen = set()
        for i in range(n):
            root = dsu.find(i)
            if root in seen: continue
            seen.add(root)
            temp_list = [accounts[root][0]]
            #we extend the list
            temp_list.extend(sorted(list(email_by_root[root])))
            answer.append(temp_list.copy())
        return answer
