# https://leetcode.com/problems/subdomain-visit-count/description/
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        subdomainVisits = {}

        # Build map of subdomains
        for domain in cpdomains:
            visitCount, domainString = domain.split(' ')
            if domainString not in subdomainVisits:
                subdomainVisits[domainString] = int(visitCount)
            else:
                subdomainVisits[domainString] += int(visitCount)

            subdomain = domainString
            while True:
                subdomains = subdomain.split('.', 1)
                if len(subdomains) == 1:
                    break
                subdomain = subdomains[1]
                if subdomain not in subdomainVisits:
                    subdomainVisits[subdomain] = int(visitCount)
                else:
                    subdomainVisits[subdomain] += int(visitCount)
        
        result = []
        for domain in subdomainVisits:
            rep = subdomainVisits[domain]
            subdomainVisitString = str(rep) + ' ' + domain
            result.append(subdomainVisitString)
        return result