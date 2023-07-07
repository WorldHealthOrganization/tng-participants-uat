import os
import glob
import json
import time

#   additions
#   assignees
#   author
#   autoMergeRequest
#   baseRefName
#   body
#   changedFiles
#   closed
#   closedAt
#   comments
#   commits
#   createdAt
#   deletions
#   files
#   headRefName
#   headRefOid
#   headRepository
#   headRepositoryOwner
#   id
#   isCrossRepository
#   isDraft
#   labels
#   latestReviews
#   maintainerCanModify
#   mergeCommit
#   mergeStateStatus
#   mergeable
#   mergedAt
#   mergedBy
#   milestone
#   number
#   potentialMergeCommit
#   projectCards
#   projectItems
#   reactionGroups
#   reviewDecision
#   reviewRequests
#   reviews
#   state
#   statusCheckRollup
#   title
#   updatedAt
#   url

prCommand = "gh pr view "+ os.environ.get("BRANCH") + " --json headRefName,comments,headRepositoryOwner,body,number,reviews,state,author,reviews"
country = os.environ.get("BRANCH")[0:3]
result = os.popen(prCommand).read()

pr = json.loads(result)

checksStatus = "gh pr checks "+ os.environ.get("BRANCH")

repeat = True
checkRunSucceeded = True
approve = True

while repeat:
  result = os.popen(checksStatus).read()
  print(result)
  time.sleep(5) # Sleep for 3 seconds
  
  if "fail" in result:
      checkRunSucceeded = False
      approve = False
      break;
  
  if result.count("pending") == 1:
      break;
      

noFailure = True
signedFolderPresent = True
csrNotSigned = True
csrNotPresent = True

files = glob.glob(country+"/**/Failure", recursive=True)
reviews = pr["reviews"]

change_requested = pr["state"] == "CHANGE_REQUESTED"

if len(files): 
    approve &= False
    noFailure &= False
    
if not (os.path.exists(country+"/onboarding/DCC/UP/signed") and os.path.exists(country+"/onboarding/DCC/TLS/signed") and os.path.exists(country+"/onboarding/DCC/SCA/signed")):  
    signedFolderPresent &= False
    approve &= False
    
if  os.path.exists(country+"/onboarding/DCC/UP/UP_SYNC.csr"):  
    csrNotSigned &= False
    approve &= False
    
if  os.path.exists(country+"/onboarding/DCC/UP/UP_SYNC.pem") and os.path.exists(country+"/onboarding/DCC/UP/UP_SYNC.csr"):  
    csrNotPresent &= False
    approve &= False
    
if not noFailure:
    comment = "Folder contains Failure files. Please resolve it."
    os.system("gh pr review "+country+"/onboardingRequest -r -b '"+comment+"'")
    
if not signedFolderPresent:
    comment = "Signed Folder not present."
    os.system("gh pr review "+country+"/onboardingRequest -r -b '"+comment+"'")

if not csrNotSigned: 
    comment = "CSR is not signed for UP. Please sign it."
    os.system("gh pr review "+country+"/onboardingRequest -r -b '"+comment+"'")
    
if not csrNotPresent: 
    comment = "CSR is still present, but already signed."
    os.system("gh pr review "+country+"/onboardingRequest -r -b '"+comment+"'")
    
if not checkRunSucceeded: 
    comment = "Tests Failed. Please resolve the issues."
    os.system("gh pr review "+country+"/onboardingRequest -r -b '"+comment+"'")
        
if approve:
    comment = "Everything fine."
    os.system("gh pr review "+country+"/onboardingRequest -a -b 'Everything fine.'")
