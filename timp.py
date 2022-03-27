#integer number

start_time  = input("start hours:(hh:mm): ")  
start_time_h = int(start_time[0:2] )      
start_time_m = int( start_time[3:5] )                    




end_time = input("end hours:(hh:mm): ") 

end_time_m = int(end_time[0:2] ) 
end_time_m = int(end_time[3:5] ) 

duration_h = end_time_h - start_time_h
duration_m = end_time_m - start_time_m

duration_m_f = end_time_h - start_time_h * 60 + duration_m    +  24 * 60 * start_time_h > end_time_h


print("event duration:" , duration_m_f , 'minutes ')