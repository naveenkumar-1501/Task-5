x=[15,'star',35.0,20,65.9]
y=lambda x:isinstance(x,(int,str))
z=list(map(y,x))
print(z)