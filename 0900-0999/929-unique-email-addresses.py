# https://leetcode.com/problems/unique-email-addresses/description/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # email = local + @ + domain
        
        addresses = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local.split('+')[0]
            local = local.replace('.', '')
            addresses.add(local + '@' + domain)

        return len(addresses)
