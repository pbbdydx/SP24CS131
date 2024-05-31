def read_txt(fn: str) -> list[str]:
    """Reads a text file, returning a list containing every word in order. A
    message stating the total number of words that were read should be printed.

    As an example, the words can look like this:

        Words: 15

    Args:
        fn (str): The filename to read.

    Returns:
        list[str]: A list of all words in the file.
    """
    file=open(fn,"r")

    allWords = file.read()
    split = allWords.split()
    print("There are", len(split), "words in the file.")
    file.close()

    return allWords

def write_txt(fn: str, text: str) -> None:
    """Write out the text provided to the specified file.

    Args:
        fn (str): The filename to write.
        text (str): The text to write to the file.
    """
    file = open(fn, "w")
    file.write(text)
    file.close 

def append_txt(fn: str, text: str) -> None:
    """Write out the text in append mode to the specified file.

    Args:
        fn (str): The filename to write.
        text (str): The text to append to the file.
    """
    file=open(fn, "a")
    file.write(text)
    file.close


def read_csv(fn: str) -> list[list[int]]:
    """Read an arbitrary CSV file of integers. Should support both uniform and
    jagged lists.

    You can assume that all inputs from the file will be integers and that they
    can be converted without issue.

    Args:
        fn (str): The filename to read.

    Returns:
        list[list[int]]: A 2D list of integers containing the data from the CSV
        file.
    """
    l=[]
    file= open(fn,"r")
    line = file.readline()
    while line!="":
        line = line.split(",")
        for i in range(len(line)):
            l[i]= int(l[i])
        l+=[line]
        line=file.readline()

    file.close()
    print(l)
    return l 

def write_csv(fn: str, data: list[list[int]]) -> None:
    """Writes a 2D list to a CSV file. Should support both uniform and jagged
    lists.

    Args:
        fn (str): The name to write.
        data (list[list[int]]): The data to write out.
    """    
    pass


def copy_file(src: str, dst: str) -> None:
    """Copies the source file to the destination file.

    This should copy the file line by line.

    Args:
        src (str): The name of the file to read.
        dst (str): The name of the file to write.
    """
    pass

def main():
    # read_txt("R10.txt")
    # write_txt("R10.txt", "does this work? \nyes it does")
    # append_txt("R10.txt", "append \n append\n banananananna")
    # read_csv("R10.csv")
    pass

if __name__ == "__main__":
    main()
    