def reverse(stri):
  mylist = [stri[i] for i in range(len(stri)-1,-1,-1)]
  return ''.join(mylist)

x=reverse('I am theja')
print(x)  

# or just stri[::-1]