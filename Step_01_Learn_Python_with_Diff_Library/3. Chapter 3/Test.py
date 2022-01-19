name = "sarju"

print(name)
print(type(name))

print(name[0])
print(name[0:1])
print(name[0:4])
print(name[0:5])
print(name[:1])
print(name[0:])
print(name[1:5:2])
print(name[::])

nametwo = "   Hello guys! how are you?"

print(len(nametwo))
ans = nametwo.endswith("dd")
print(ans)
ans = nametwo.startswith("h")
print(ans)
ans = nametwo.index("u")
print(ans)
ans = nametwo.count("a")
print(ans)
print(nametwo)
ans = nametwo.strip()
print(ans)
ans = nametwo.count(" ")
print(ans)