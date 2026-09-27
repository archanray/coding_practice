def solution1(clients):
    max_count = 0
    shelf_count = 0
    max_client = 0
    
    for client in clients:
        if client > max_client:
            shelf_count += client - max_client - 1
        else:
            shelf_count -= 1
        max_count = max(max_count, shelf_count)
        max_client = max(max_client, client)
    return max_count

def solution(clients):
    n = len(clients)
    shelf = []
    client_ID = 0
    max_count = 0
    count = 0
    pack_ID = 1
    
    while client_ID < n:
        if clients[client_ID] > pack_ID:
            # put packages in shelf
            shelf += list(range(pack_ID, clients[client_ID]))
            count = count+clients[client_ID]-pack_ID
            max_count  = max(max_count, count)
            pack_ID = clients[client_ID]+1
            client_ID += 1
        else:
            if len(shelf) == 0:
                pack_ID += 1
                pass
            else:
                # client picks from shelf
                shelf.remove(clients[client_ID])
                if pack_ID < n:
                    # pack still comes
                    shelf.append(pack_ID)
                    pack_ID+=1
            client_ID += 1
        print(shelf, max_count)
    return max_count

# inputs = [1, 2, 3, 4, 5]
# inputs = [3, 2, 4, 5, 1]
inputs = [3, 2, 7, 4, 5, 6, 1]
print(solution(inputs), solution1(inputs))