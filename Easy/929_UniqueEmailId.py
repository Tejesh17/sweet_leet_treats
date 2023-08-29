def returnEmail (email: str)-> str:
    em = email.split("@")
    em[0] = em[0].replace(".","")
    em[0] = (em[0].split("+"))[0]
    return em[0]+"@"+ em[1]

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        allmails = []
        for email in emails:
            e = returnEmail(email)
            if(e not in allmails):
                allmails.append(e)
        return len(allmails)