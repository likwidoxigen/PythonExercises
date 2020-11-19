def scramble(r_items, s_items):
    if len(r_items) == 0:
        print(' '.join(s_items))
    else:
        # Recursive case: For each call to scramble()
        # move a letter from remaining to scrambled
        for i in range(len(r_items)):
            # The letter at index i will be scrambled
            scramble_item = r_items[i]
            # Remove letter to scramble from remaining letters list
            remaining_items = r_items[:i] + r_items[i+1:]
            # Scramble letter
            scramble(remaining_items, s_items + [scramble_item])

names = "Joe Bob Jim"
name_list = names.split(' ')
scramble(name_list, [])