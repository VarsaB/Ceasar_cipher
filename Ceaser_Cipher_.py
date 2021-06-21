alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#function to encode and decode text
def ceaser(data,shift_by,direction):
  ceaser_text = ""
  if direction =="decode":
        shift_by*=-1
  for ch in data:
    if ch not in alphabet:
      ceaser_text+=ch
      continue
    else:
      ceaser_text+=alphabet[alphabet.index(ch)+shift_by]
  print(f"\n\n{direction}d message is {ceaser_text}\n")
rstart=True
while rstart:
  print("\n\t\t\tWelcome to Ceasor Cipher !!!!\n")
  #reading input from users
  direct = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direct =='encode' or direct == 'decode':
    text = input("\n\nType your message:\n").lower()
    shift = int(input("\n\nType the shift number:\n"))
    while shift > 26:
      shift%=26
    #Calling function to dencode or decode
    ceaser(data=text,shift_by=shift,direction=direct)
    cont = False
    while not cont:
      rs =input("\n\nDo you want to restart Ceasor Cipher ?  type yes or no\n").lower()
      if rs =="yes" or rs=="no":
        cont = True
        if rs == "no":
          rstart = False
      else:
        print("\nEnter Valid option \n")
  else:
    print("\n\nEnter Valid Option \n")