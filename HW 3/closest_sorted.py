import bisect

def find(arr,seach_ele,k):

   t =  bisect.bisect(arr,seach_ele)
   a = t-1 
   b = t
   count = 0

  
   
   for i in range(0,len(arr)):
      if(count < k):
         if(a < 0):
    
            b= b+1
         elif b > len(arr)-1:
            a = a-1 

         else:

            abs_left = abs(seach_ele- arr[a])
            abs_right = abs(arr[b]-seach_ele)
            if(abs_left) > (abs_right):
            

          
             b = b+1
            elif(abs_right) > (abs_left):
           
                      a = a - 1  
            else:
               a = a-1

            # if(len(temp_array) == k):
            #    break
         count = count + 1
      else:
         break
   
   return arr[a+1:b]
   

# array = [1,2,3,4,4,7]
# find(array, 5.2,2)

