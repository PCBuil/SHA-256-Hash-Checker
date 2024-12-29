import hashlib

target = 0x0000000000000000000297fa0000000000000000000000000000000000000000
num=0

print(target)
#a=input("How much hashes? ")
for x in range(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
   hash = hashlib.sha256(str(num).encode()).hexdigest()

   if int(hash,16) <= target:
      print("Hash Found!")
      break
     
   print(hash)
   num += 1

b = input("Continue? ")

if b == "yes" :
   c = input("How much hashes? ")
   for x in range(int(c)):
      hash = hashlib.sha256(str(num).encode()).hexdigest()

      if int(hash,16) <= target:
         print("Hash Found")
         break 
     
      print(hash)
      num += 1
   
