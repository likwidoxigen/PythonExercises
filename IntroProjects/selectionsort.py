listicle = ["peas", "caroots", "sausage", "oxtail"]
print(listicle)

saved_value = listicle[2]
#print(f"Saved Value: {saved_value}")
listicle[2] = listicle[3]

print(listicle)
listicle[3] = saved_value


print(listicle)

print(listicle[3])