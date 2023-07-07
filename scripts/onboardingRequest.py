import os
import sys

repo = sys.argv[1]

if repo == "repo":
  with open('temp/verifyResult') as f:
    result = f.readline()   
    if not result:
        raise Exception("Bad verification.")
    else:
        os.system("echo 'Verification was good.'")

with open('temp/country') as f:
  country = f.readline().replace("\n","")

branchName = country + "/onboardingRequest"

os.system("git checkout -b" + branchName +" > /dev/null 2>&1")
os.system("rm -rf "+country)
os.system("mkdir -p " + country)
os.system("mkdir -p " + country+"/onboarding")
os.system("cp -r "+repo+"/onboarding " + country )
os.system("[ -e "+country+"/onboarding/DCC/TLS/Report ] && cat "+country+"/onboarding/DCC/TLS/Report")
os.system("[ -e "+country+"/onboarding/DCC/TLS/Report ] && rm "+country+"/onboarding/DCC/TLS/Report")

if os.path.exists("sync"):
  if os.path.exists(country+"/onboarding/DCC/UP/UP_SYNC.pem"): 
      os.system("rm "+country+"/onboarding/DCC/UP/UP_SYNC.csr")
else:
    if os.path.exists(country+"/onboarding/DCC/UP/UP_SYNC.pem"): 
      os.system("rm "+country+"/onboarding/DCC/UP/UP_SYNC.pem")

os.system("[ -d "+country + "/onboarding/DCC/auth"+" ] && mv " + country + "/onboarding/DCC/auth "+ country+"/onboarding/DCC/TLS")
os.system("[ -d "+country + "/onboarding/DCC/csca"+" ] && mv " + country + "/onboarding/DCC/csca "+ country+"/onboarding/DCC/SCA")
os.system("[ -d "+country + "/onboarding/DCC/up"+" ] && mv " + country + "/onboarding/DCC/up "+ country+"/onboarding/DCC/UP")
os.system("[ -f "+country + "/onboarding/DCC/SCA/CSCA.pem"+" ] && mv " + country + "/onboarding/DCC/SCA/CSCA.pem "+ country+"/onboarding/DCC/SCA/SCA.pem")
os.system("git add "+ country + " > /dev/null 2>&1")

result = os.popen("git commit -m 'Bot added Files from "+country+"'").read()

if not "nothing added to commit" in result:
  os.system("git push -f -u origin "+ branchName +" > /dev/null 2>&1")

#> /dev/null 2>&1
