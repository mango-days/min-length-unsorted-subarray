# Find the Minimum length Unsorted Subarray, sorting which makes the complete array sorted
array = [ 10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60 ]
index_l = 1
index_r = len ( array ) - 2
flag_l = False
flag_r = False

while ( flag_l == False and flag_r == False ) :
    if array [ index_l ] > array [ index_l - 1 ] : index_l += 1
    else : 
        flag_l = True
        if ( array [ index_r ] < array [ index_r + 1 ] and array [ index_r ] > array [ index_l ] ) : index_r -= 1
        else : flag_r = True

print ( array [ index_l : index_r + 1 ])