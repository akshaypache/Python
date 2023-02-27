

# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     for j in range(i): 
#         print("*",end="_")
#     print(end="\n")





# 1 2 3 4 5 6 7 8 9 10 
# 2 4 6 8 10 12 14 16 18 20 
# 3 6 9 12 15 18 21 24 27 30 
# 4 8 12 16 20 24 28 32 36 40 
# 5 10 15 20 25 30 35 40 45 50 
# 6 12 18 24 30 36 42 48 54 60 
# 7 14 21 28 35 42 49 56 63 70 
# 8 16 24 32 40 48 56 64 72 80 
# 9 18 27 36 45 54 63 72 81 90

# ctrl + / ----------> comment

# for a in range(1,10):
#     for b in range(1,11):
#         print(a*b,end="\t")
#     print()

# a = 10
# print(a==11)

# print("H\tello\\n guys")
# escape char

# a = 'this is my mom\'s mobile'
# print(a)




# 1 1 1 1 1 1 1 1 1 1 
# 2 2 2 2 2 2 2 2 2 2 
# 3 3 3 3 3 3 3 3 3 3 
# 4 4 4 4 4 4 4 4 4 4 
# 5 5 5 5 5 5 5 5 5 5 
# 6 6 6 6 6 6 6 6 6 6 
# 7 7 7 7 7 7 7 7 7 7 
# 8 8 8 8 8 8 8 8 8 8 
# 9 9 9 9 9 9 9 9 9 9 



# 1 2 3 4 5 6 7 8 9 10 
# 1 2 3 4 5 6 7 8 9 10 
# 1 2 3 4 5 6 7 8 9 10 
# 1 2 3 4 5 6 7 8 9 10 
# 1 2 3 4 5 6 7 8 9 10 
# 1 2 3 4 5 6 7 8 9 10 
# 1 2 3 4 5 6 7 8 9 10 
# 1 2 3 4 5 6 7 8 9 10 
# 1 2 3 4 5 6 7 8 9 10


#     * 
#    ** 
#   *** 
#  **** 
# ***** 

# range(1,10)     
# for i in [1,2,3,4,5]:
#     for j in range(i,5):      #
#         print(end=" ")
#     for k in range(i):
#         print(end="* ")
#     print(end="\n")
    
    

# ----*
# ---**
# --***
# -****
# *****

   
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j,end="\t")
#     print()

# 11 12 13 14 15
# 21 22 23 24 25
# 31 32 33 34 35 
# 41 42 43 44 45
# 51 52 53 54 55

# 1)
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

# for i in [1,2,3,4,5]:
#     for j in range(1,6):
#         if(i+j>=6):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# 2)
# 1 1 1 1 1 
# 0 0 0 0 0 
# 0 0 0 0 0 
# 0 0 0 0 0 
# 0 0 0 0 0 

# for i in [1,2,3,4,5]:
#     for j in range(1,6):
#         if(i==1):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
        
#     print()

# 3)
# 1 0 0 0 0 
# 1 0 0 0 0 
# 1 0 0 0 0 
# 1 0 0 0 0 
# 1 0 0 0 0 
# for i in [1,2,3,4,5]:
#     for j in range(1,6):
#         if(j==1):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()



# 1 0 0 0 0 
# 0 1 0 0 0 
# 0 0 1 0 0 
# 0 0 0 1 0 
# 0 0 0 0 1 

# for i in [1,2,3,4,5]:
#     for j in range(1,6):
#         if(i==j):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()



# 4)
# 1 1 1 1 1 
# 0 1 1 1 1 
# 0 0 1 1 1 
# 0 0 0 1 1 
# 0 0 0 0 1 


# for i in [1,2,3,4,5]:
#     for j in range(1,6):
#         if(i<=j):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# 5)
# 1 0 0 0 0 
# 1 1 0 0 0 
# 1 1 1 0 0 
# 1 1 1 1 0 
# 1 1 1 1 1 

# for i in [1,2,3,4,5]:
#     for j in range(1,6):
#         if(i>=j):
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()




# 6)
# 1 0 1 0 1 
# 0 1 0 1 0 
# 1 0 1 0 1 
# 0 1 0 1 0 
# 1 0 1 0 1 

# a = int(input("bhagwan ke nam pe dede re baba = "))
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         if (i+j)%2 == 0:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()





# 7)
# 1 1 1 1 1 
# 1 0 0 0 1 
# 1 0 0 0 1 
# 1 0 0 0 1 
# 1 1 1 1 1 

# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or i==5 or j==1 or j==5:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()


# 8)
# * * * * * 
# * *   * *
# *   *   *
# * *   * *
# * * * * *


# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or i==5 or j==1 or j==5 or i==j or i+j==6:
#             print(end="* ")
#         else:
#             print(end="  ")
#     print()

# 11 12 13 14 15
# 21 22 23 24 25
# 31 32 33 34 35 
# 41 42 43 44 45
# 51 52 53 54 55

# 9)
# * 
# * * 
# *   *
# *     *
# * * * * *


# for i in range(1,6):
#     for j in range(1,6):
#         if j==1 or i==5 or i==j:
#             print(end="* ")
#         else:
#             print(end="  ")
#     print()




