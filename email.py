import re
validemail = False
@prob = False
endprob = False
charsprob = False
#email = input("Please enter your email").strip()
email = "a@a.gov.uk"
if not re.search(r".+, @{1}.+", email):
    @prob = True
    
if re.search(r"\.ac.uk$", email):
    validemail = True
    print("Valid Academic Email")
if re.search(r"\.gov.uk$", email):
    validemail = True
    print("Valid Government Email")
elif re.search(r"\.nhs.net$"):
    validemail = True
    print("Valid NHS Email")
else:
    print("error")
if endprob = 
