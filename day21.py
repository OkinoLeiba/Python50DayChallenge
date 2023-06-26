#python challenge day21
# Day 21: List of Tuples  
# Write  a  function  called  make_tuples  that  takes  two  lists, 
# equal  lists, and  combines them into a list of tuples. For 
# example,  if  list  a  is  [1,2,3,4]  and  list  b  is  [5,6,7,8],  your 
# function should return [(1,5), (2,6), (3,7), (4,8)]. 
 
# Extra Challenge: Even Number or Average  
# Write a function called even_or_average that ask a user to 
# input  five  numbers.  Once  the  user  is  done,  the  code  should 
# return  the  largest  even  number  in  the  inputted  numbers.  If 
# there is no even number in the list, the code should return the 
# average of all the five numbers. 
 
  
if __name__ == "__main__":
    
    def make_tuples(tela_tuple1, tela_tuple2) -> None:
        tela_tuple3 = []
        counter = 0
        while counter < len(tela_tuple2):
            tela_tuple3.append([tela_tuple1[counter], tela_tuple2[counter]])
            counter += 1
        tela_tuple3 = tuple(tela_tuple3)
        # return tela_tuple3
        
        tela_tuple4 = zip(tela_tuple1, tela_tuple1, strict=False)
        # tela_tuple5 = tuple(map(lambda a, b: tuple(a, b), tela_tuple1, tela_tuple2))
        print(tela_tuple3)
        
        
    def even_or_average() -> str|None:
        
        work_num = []
        even_list = []
        while True:
            num_input = input("Please Input Five Number: ")
            work_num.append(int(num_input))
            if len(work_num) == 5:
                break
        for num in work_num:
            if num % 2 == 0:
                even_list.append(num)
                continue
        if len(even_list) > 1:
            print("The largest even number: %d" %(max(even_list)))
        else:
            print("The average is: %d" %(sum(work_num) / len(work_num)))
            
            
        # num_result = [max(even) for even in num_input if num_input % 2 == 0]
        
        # for num in num_input:
        #     even_list = []
            
        #     if int(num) % 2 == 0:
        #         even_list.append(num)
        #         iterate = 0
        #         while iterate < len(even_list):
        #             max_num = even_list[iterate] > even_list[iterate+1]
        #             iterate =+ 1
        #     if int(num) % 2 != 0:
        #         num_sum += num
                #   break
                
        avg_list = []
        even_list2 = []
        while True: 
            num_input2 = input("Please Enter Five Numbers: ") 
            avg_list.append(int(num_input2)) 
            if int(num_input2) % 2 == 0: 
                even_list2.append(num_input2) 
                 
            if len(avg_list) == 5: 
                break 
        if len(even_list2) > 0: 
            return f"The largest even number: {max(even_list2)}"    
        else: 
            return f'The average is : {sum(avg_list) / len(avg_list):.2f}'
        
    tela_tuple1 = [1,2,3,4]
    tela_tuple2 = [5,6,7,8]
    
    # make_tuples(tela_tuple1, tela_tuple2)
    even_or_average()