'''You are given A painters and an array C of N integers where C[i] denotes the length of the ith board. Each painter takes B units of time to paint 1 unit of board. You must assign boards to painters such that:

Each painter paints only contiguous segments of boards.
No board can be split between painters.
The goal is to minimize the time to paint all boards.


Return the minimum time required to paint all boards modulo 10000003.'''
A = 2
B = 5
C = [1, 10]

#Time Complexity: O(N × log(sum(C)))
# Space Complexity: O(1)
def is_possible(painters,time,time_per_board,board_arr):
    painters_count=1
    time_sum=0
    for i in range(len(board_arr)):
        time_sum+=board_arr[i]*time_per_board
        if time_sum>time:
            time_sum=board_arr[i]*time_per_board
            # add this extra if low starts from 1*time_per_board
            # if time_sum> time:
            #     return False
            painters_count+=1
    if painters_count<=painters:
        return True
    else:
        return False

def optimal(painters,time_per_board,board_arr):
    low=max(board_arr)*time_per_board
    high=sum(board_arr)*time_per_board
    while low<=high:
        mid=low+(high-low)//2
        if is_possible(painters,mid,time_per_board,board_arr):
            high=mid-1
        else:
            low=mid+1
    return low % 10000003

print(optimal(A,B,C))