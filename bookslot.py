from datetime import date

print("enter the hour ")
h=input()
print ("enter the min 00/20/40")
m=input()

print("creating slot for {} : {}".format(h,m))


print ("slotrequestedfor {}-{}-{}".format(date.today(),h,m))