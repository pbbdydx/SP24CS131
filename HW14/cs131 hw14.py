
## CS131  Assignment 14
## Prajwal Bhandari
## April 2024

def isin(a,b:list) -> bool:
    for _ in range(len(b)):
        if b[_] == a:
            return True
    return False


def round_one(value: float ) -> float:
    return ((value*10+ 0.5)//1.0)/10


def load_data(fn: str) ->  tuple[int,list[list[int]]]: 
    num_entries = 0
    doc_list = []
    try:
        file = open(fn,"r")
        row = file.readline() 
        row_num = 0
        while row != "":
            row = row.strip().split(",")

            modified_row=[]
            for i in range(len(row)):
                try: 
                    modified_row.append(int(row[i]))
                except ValueError:
                    print("Row ",row_num, ", col ", i, " is not a valid entry.", sep="" )
                    
            num_entries += len(modified_row)
            doc_list.append(modified_row)
            row_num += 1
            row = file.readline()
        file.close()
    except FileNotFoundError:
        return -1, doc_list
    return num_entries, doc_list


def save_data(fn: str, data: list[tuple[float, float, tuple[int, ...]]]) -> None:
    # write each list in data as  "mean, median, tuple(modes)"
    file = open(fn,"w")   
    for i in range(len(data)):
        for j in range(2):
            file.write(str(data[i][j]) + ",")
        for k in range(len(data[i][2])-1):
            file.write(str(data[i][2][k]) + ",")
        # write the last element of the tuple without a comma, and start a new line
        file.write(str(data[i][2][len(data[i][2])-1]) + "\n")

    file.close()

def find_mean(l: list[int]) -> float:
    assert len(l) > 0, "List cannot be empty"

    sum=0
    for i in range(len(l)):
        sum+=l[i]
    return round_one(sum/len(l))


def find_median(l: list[int]) -> float:
    assert len(l) > 0, "List Cannot be empty!"
    if len(l) == 1:
        return round_one(l[0])
    if len(l) == 2:
        return round_one((l[0]+l[1])/2)
    
    min, max = l[0], l[0]
    minindex , maxindex = 0, 0

    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
            minindex = i
        if l[i] > max: 
            max = l[i]
            maxindex = i
    l.pop( minindex )
    if minindex < maxindex: 
        l.pop(maxindex-1) # have to pop -1 since previous pop shifts everything
    else: 
        l.pop(maxindex) # if we pop an element that comes after the max, then the index doesnt change

    return find_median(l)


def find_mode(l: list[int]) -> tuple[int, ...]:
    assert len(l) > 0, "List cannot be empty"
    frequenies={}
    max_freq = 0 
    modes = []
    for _ in range(len(l)):
        try:
            frequenies[l[_]] += 1
        except KeyError:
            frequenies[l[_]] = 1
        
        if frequenies[l[_]] > max_freq:
            max_freq = frequenies[l[_]]
    for _ in range(len(l)):
        if frequenies[l[_]] == max_freq and not isin(l[_], modes):
            modes.append(l[_])
    return tuple(modes)


def analysis(fn_in: str, fn_out: str) -> None:
    num_entries , data = load_data(fn_in)

    analyzed_list = []

    for q in range(len(data)):
        mean, median, mode = find_mean(data[q]), find_median(data[q].copy()), find_mode(data[q])
        analyzed_list.append((mean,median,mode))
    print("Loaded", num_entries, "integers.")

    save_data(fn_out,analyzed_list)



def main():
    analysis("HW14\\dataset_1.csv","HW14\\data_analysis.csv")
if __name__== "__main__":
    main()