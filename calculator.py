x = input("What's your speed in km/h? ")
try:
  val = int(x) * 1.609
  print("Your speed is", float(val), "miles/h")
except:
    x = -1
    print("Not a number")
print("Done")
