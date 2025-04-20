car = {
  "brand": "Bmw",
  "model": "Competition",
  "year": 1999
}

x = car.setdefault("model", "Bronco")

print(x)
#output   Competition
