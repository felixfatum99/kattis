def propose_reject(P, R):
    s = dict()

    while unmatched(P):
        p = find_p(P)
        rname = p.pref[len(p.pref)-1]
        r = R[rname]
        if r.unmatched:
            s[p.name]=r.name
            r.current_partner = p
            p.unmatched = False
            r.unmatched = False
            p.pref.pop()
        elif not r.unmatched:
            if r.pref[r.current_partner.name] > r.pref[p.name]:
                del s[r.current_partner.name]
                s[p.name] = r.name
                p.pref.pop()
                p.unmatched = False
                r.current_partner.unmatched = True
                r.current_partner = p
            else:
                p.pref.pop()
    for i in s:
        print(i, s[i])

def find_p(p):
    for i in range(len(p)):
        if p[i].unmatched and len(p[i].pref) > 0:
            return p[i]

def unmatched(l):
    r = False
    for i in range(len(l)):
        if l[i].unmatched and len(l[i].pref)>0:
            r = True
            break
    return r

def room_mate():
    return 
    
def run():
    n = [int(x) for x in input().split(" ", -1)]
    p = []
    r = dict()
    for i in range(n[0]):
        if i < n[0]/2:
            l = [x for x in input().split(" ", -1)]
            pr = proposer(l[0], l[1:])
            p.append(pr)
        else:
            l = [x for x in input().split(" ", -1)]
            rj = rejecter(l[0], l[1:])
            r[l[0]]= rj      
    
    if ((n[0]/2)*(n[0]/2))>=n[1]:
        propose_reject(p, r)
    else:
        print("-")

class proposer:
    def __init__(self, name: str, l: list):
        self.pref = l
        self.pref.reverse()
        self.name = name
        self.unmatched = True

class rejecter():
    def __init__(self, name: str, l: list):
        self.name = name
        self.pref = self.todict(l)
        self.unmatched = True
        self.current_partner = ""

    def todict(self, l: list):
        d = dict()
        for i in range(len(l)):
            d[l[i]] = i+1
        return d

run()