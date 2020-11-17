print("Hello world")

#Tri par Selection
def tri_selection(tab):
   for i in range(len(tab)):
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab
tab = [98, 22, 15, 32, 2, 74, 63, 70]
 
print ("Le tableau trié par Selection est:")
print(tab)
print (tri_selection(tab))

#Tri par fusion
list=[1,4,6,8,0,3,9,2,5]

def fusion(left, right):
    res= []
    i=0
    j=0

    while i<len(left) and j<len(right):
        if(left[i] < right[j]):
            res.append(left[i])
            i=i+1
        else:
            res.append(right[j])
            j=j+1
    if i==len(left):
        res.extend(right[j:])
    if j==len(right):
        res.extend(left[i:])
    return res

def tri_fusion(tab, start, end):
    if ((len(tab))<=1):
        return tab
    else:
        milieu =(start + end)//2
        left = tab[:milieu]
        right = tab[milieu:]

        left = tri_fusion(left, 0, len(left))
        right = tri_fusion(right, 0,len(right))

        return fusion(left, right)

print("Le tableau trié par Fusion est:")
print(list)
print(tri_fusion(list, 0, len(list)))