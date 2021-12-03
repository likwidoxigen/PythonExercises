


finput ='./AdventOfCode/Day05/invalid.txt'
finput = './AdventOfCode/Day05/valid.txt'
finput = './AdventOfCode/Day05/Input.txt'
seats =[]


def get_loc(seat):
    directions = list(seat)
    start = 0
    stop = 0
    if "R" in directions or "L" in directions:
        stop = 7
    else:
        stop = 127
    what = 1
    # print(f"stop:{stop}")
    for step in directions:
        if step == "R" or step == "B":
            start = start + round((stop-start)/2)
            what = 1
        else:
            stop = stop - round((stop-start)/2)
            what = 2
    #print (f"start:{start}   stop:{stop}")
    return stop if what == 1 else start



def process_seat(seat):
    row = seat[0:-3]
    col = seat[-3:]
    rownum = get_loc(row)
    colnum = get_loc(col)
    seatID = rownum * 8 + colnum
    # print(f"row {rownum}, column {colnum}, seat ID {rownum * 8 + colnum}")
    return {'row':rownum, 'column':colnum, 'seat_ID':seatID }

def get_max_seatID(seats):
    max = 0
    for seat in seats:
        if seat['seat_ID'] > max:
            max = seat['seat_ID']
    return max

with open(finput, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if len(line) >= 3:
            seats.append(line.strip())

processed_seats= []
for seat in seats:
    processed_seats.append(process_seat(seat))

print(get_max_seatID(processed_seats))

seat_ids =[]
for seat in processed_seats:
    seat_ids.append(seat['seat_ID'])

seat_ids.sort()
prev_id = 0
for id in seat_ids:
    if prev_id == 0:
        prev_id = id-1
    #print(f"id: {id}  prev:{prev_id}")
    if id != (prev_id+1):
        print(f"your seat is {(prev_id+1)}")
    prev_id = id

