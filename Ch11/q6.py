def solution(food_times, k):
    answer = 0
    food_left = len(food_times)
    food_idx = 0
    
    times = 0
    while times <= k:
        print(answer)
        
        if food_left <= 0:
            answer = -1
            break;
        
        if food_idx > len(food_times) - 1:
            food_idx = 0
        # print(f"food_times[{food_idx}]: {food_times[food_idx]}")
        
        if food_times[food_idx] == 0:
            food_idx += 1
            food_left -= 1
            # print(food_left)
            continue;
        else:
            food_times[food_idx] -= 1
            answer = food_idx + 1
            food_idx += 1
            times += 1
    
    print(answer)
    return answer