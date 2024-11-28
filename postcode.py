import re

address = "University of Kent, Canterbury, Kent, CT2 7NT"
place, city, county, postcode = address.split(", ", 3)
print(postcode)
pattern = r'[A-Z]{1,2}[0-9][0-9A-Z]?\s?[0-9][A-Z]{2}'

postcode1 = re.search(pattern, address)

if postcode1:
    result = postcode1.group(0)
    print(f"Extracted postcode: {result}")
else:
    print("No postcode found")