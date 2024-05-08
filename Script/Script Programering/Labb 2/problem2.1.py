#problem 2.1 (!!!Klar)
# Global variables
we_wish = "We wish you a Merry Christmas "
happy_new = "and a Happy New Year"

#This funtion prints "We wish you a Merry Christmas and a Happy New Year"
def wish ():
  for lyric in range(2):
    print(we_wish)
  print(f"{we_wish}{happy_new}")
wish()
print()

# This function prints "Good tidings we bring to you and your kin"
def tidings (good_tidings):
  print(good_tidings)
  return f"{we_wish}{happy_new}"
print(tidings("Good tidings we bring to you and your kin"))
print()

#This function prints "Now bring us some figgy pudding"
def nowbring_outhere (now_bring, out_here):
    for lyric in range(2):
        print(now_bring)
    return now_bring + out_here
print(nowbring_outhere("Now bring us some figgy pudding", ", now bring some out here"))
print()

# This function prints "Good tidings we bring to you and your kin"
print(tidings("Good tidings we bring to you and your kin"))
print()

# This function prints "We won't go until we get some"
def wewont_outhere (we_wont, outhere):
    for lyric in range(2):
        print(we_wont)
    return we_wont + outhere
print(wewont_outhere("We won't go until we get some", ", so bring some out here"))
print()

# This function prints "Good tidings we bring to you and your kin"
print(tidings("Good tidings we bring to you and your kin"))
print()

#This funtion prints "We wish you a Merry Christmas and a Happy New Year"
wish()
print()