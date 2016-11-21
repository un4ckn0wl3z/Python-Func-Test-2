"""
Anuwat Khongchuai IT431 ID:273
"""
def FindCirFullRadiusAndCirArea(r):
	CFR = 2*3.14*r
	CA = 3.14*(r**2)
	return CFR, CA

r = float(input("Enter Radius: "))
CFR, CA = FindCirFullRadiusAndCirArea(r)

print("CFR is "+str(CFR))
print("CA is "+str(CA))
