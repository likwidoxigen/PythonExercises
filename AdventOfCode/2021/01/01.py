

def process_input(line, compdict):
    return int(line.strip());

def main():
    file_dir = './'
    inputfile = "input01a.txt"
    count = 0
    with open (inputfile, 'r') as file:
        lines = file.readlines()
        compdict = {"previous": -1, "current": -1}
        for line in lines:
            if len(line, ) >0:
                compdict['previous'] = compdict['current']
                compdict['current'] = process_input(line, compdict)

                if ( compdict['previous'] != -1 and compdict['current'] - compdict['previous'] >=1):
                    count += 1
        
    print (count)

main()