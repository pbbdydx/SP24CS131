"""E/DD.05 : Our Personal Autograder

The Autograder that is used by this class is a complex piece of software, but
that's because it has to understand an use any student submission. Because we're
engineers and scientists and we're testing our own code anyway, lets not focus
on that functionality. Instead, lets build an application that will compute our
final score in this class based on the assignments we've submitted and got back.

--------------------------------------------------------------------------------

We want to build a program, `get_grades`, that will display the grades we have
for every type of assignment we've done so far. We don't need to return anything
from our application, as it's just a utility that displays data!

 - Inputs:

The inputs for this application are three parallel lists that contain all of the
relevant data we need for our application. A small graphic of these inputs is
shown below:

  [assignment type]        [assignment points]
         |                         |
         |     [points earned]     |
         |            |            |
 [i] +-------+    +-------+    +-------+
  0  |  "A"  | -> |   5.6 | -> |  10.0 | -> Assignment (A) was 5.6 / 10.0
  1  |  "A"  |    |  12.0 |    |  10.0 |
  2  | "DD"  |    |  18.0 |    |  20.0 |
  3  | "DD"  | -> |  22.0 | -> |  20.0 | -> Design Doc (DD) was 22.0 / 20.0
  4  |  "A"  |    |  12.0 |    |  12.0 |         This one got extra credit!
  5  |  "F"  | -> |  95.0 | -> | 100.0 | -> Final (F) was 95.0 / 100.0
     +-------+    +-------+    +-------+

    Assignment Type:
        This will be one of the following strings:
            "A"     For "Assignment"
            "E"     For "Exercise"
            "DD"    For "Design Document"
            "KC"    For "Knowledge Check"
            "X"     For "Exam"
            "F"     For "Final"

        The constant `ALL_TYPES` also has all of these in this order that you
        can refer to throughout your program.

    Points Earned:
        A decimal number which represents the total number of points earned on
        that assignment. Can only ever be as low as '0.0', but effectively has
        no upper limit.

    Assignment Points:
        A decimal number representing the score the assignment was out of. If we
        divide the points earned by this number, we can get the percentage for
        the assignment!

At each index, the assignment type, points earned, and assignment points will
describe all of the data we need for that particular assignment. The order we
put our assignments into the list shouldn't matter, so long as the index in each
list actually refer to the same assignment. Because of this, we should ensure
that each list is the same length and print a error message and return if they
aren't.

 - Output:

Because our program isn't going to be providing any data outside of itself, only
showing it, our application shouldn't return anything.

 - Displays:

You are provided the function `display_data`, which will show everything you
need to display.

To do this, the function needs a few pieces of information that we'll have to
calculate from the inputs. That information is as follows:
    - score   : The weighted score (0.0, 1.0) for the whole course.
    - scores  : A list of unweighted scores (0.0, 1.0) for each assignment type.

For each assignment type, we'll have to calculate the unweighted percentage and
the letter grade that percentage represents. These lists should be in the same
order as the `ALL_TYPES` constant, with Assignments first, Exercises next, and
so on.

But before we can really do that, there are some things we'll have to make a
note of when calculating this data. Ask yourself, "How should we handle
assignments that are *not* in the input?" That is, what should happen if we
haven't taken the final yet, so it's not in our input? If we consider it a '0.0'
our score would tank! But if we consider it a `1.0` we might overly inflate our
score -- especially if we don't get a 100% later on... So what to do?

We'll follow the rules that Canvas does, just to keep things as consistent as
possible. To do that, we need to follow these rules.
    - If there are fewer than expected for any particular type, we will only use
        those assignments for the the unweighted percentage. For example, if we
        have 4 of a type, but expect 5, we average with 4, not 5.
    - If there are more than expected for any particular type, we will drop the
        lowest assignments till we're back at the expected count. For example,
        if we have 10 assignments, but only expect 7, we'd need to drop the
        lowest three values in the list to compute the unweighted percentage.
    - If it's neither of these things, compute the average normally!

Once we have the lists of data, we only need to compute the overall scores using
the weights in the syllabus just like we've done in previous assignments. The
function `get_weights` gives you the weights you need in order to account
convert these weird missing percentages into valid values.

--------------------------------------------------------------------------------

Wow! This might be simpler than the Autograder, but it's still a complicated
task! We should approach this piece by piece, using TDD to break apart the
problem into more manageable parts. Start this problem by designing your
approach and answer these questions:
    - What do we have to begin with?
    - What do we need at the end?

To complete this exercise, complete the required functions and ensure that the
each works as expected! Use your design skills to plan out and then tackle these
problems.

As a checklist, you must finish the following:
    - drop_lowest
    - get_grades
    - letter_grade
    - points_to_percents
    - round_one
    - unweighted_score
    - weighted_score

You are given two functions that you will use and that you should not change:
    - display_data
    - get_weights

Make sure to design things out before jumping into code!
"""

################################################################################
# Constants

ALL_TYPES = ["A", "E", "DD", "KC", "X", "F"]
"""All of the assignment types."""

MAX_TYPES = [7, 4, 10, 10, 2, 1]
"""The maximum number of assignments of each type."""

################################################################################
# Given Functions

def display_data(score, scores):
    """Displays all of the data for our program.

    The Autograder will have its own version of this function, so don't change
    it or you'll run into weird problems!

    This function requires you to complete the following functions:
        - `letter_grade` : To convert values to letter grades.
        - `round_one`    : To round decimal numbers to one decimal point.

    Args:
        score (float): Total weighted percentage. Between 0.0 and 1.0.
        scores (list[float]): A list of unweighted percentages. Must be 6 items
        long with each item between 0.0 and 1.0.

    Returns:
        Nothing.
    """
    TITLES = [
        "Assignments      : ",
        "Exercises        : ",
        "Design Documents : ",
        "Knowledge Checks : ",
        "Exams            : ",
        "Final            : ",
    ]

    # Display each section in the order of `ALL_TYPES`
    for i in range(len(TITLES)):
        print(TITLES[i], end="")

        value = scores[i] * 100.0
        if value < 0.0:
            print("\tNo data")

        else:
            print(
                letter_grade(value),
                "\t",
                round_one(value),
                "%",
                sep="",
            )

    # Display the final entry
    value = score * 100.0
    print(
        "\nOverall          : ",
        letter_grade(value),
        "\t",
        round_one(value),
        "%",
        sep="",
    )


def get_weights(scores):
    """Gets the appropriate weights to use with the provided scores. These
    weights allow scores which otherwise don't have entries to be ignored.

    The Autograder will have its own version of this function, so don't change
    it or you'll run into weird problems!

    Args:
        scores (list[float]): A list of unweighted percentages, from 0.0 to 1.0.
        This list should be exactly 6 items long.

    Returns:
        A list of scaled weights you can use with the provided scores. This list
        should be exactly 6 items long.
    """
    scale = 0.0
    weights = [0.14, 0.16, 0.15, 0.05, 0.25, 0.25]

    # Detect which weights should be zeroed out
    for i in range(len(weights)):
        if scores[i] >= 0.0:
            # Keep a total for scaling
            scale += weights[i]
        else:
            weights[i] = 0.0

    # Scale the weights
    if scale > 0.0:
        for i in range(len(weights)):
            weights[i] /= scale

    return weights


################################################################################
# Your Functions


def round_one(value):
    value*=10
    value+=0.5
    value//1 
    value/=10
    return value  # TODO; Write this function

def letter_grade(value):
   
    if value>=94:
        LGrade="A"
    elif value>=90:
        LGrade="A-"
    elif value>=87:
        LGrade="B+"
    elif value>=84:
        LGrade="B"
    elif value>=80:
        LGrade="B-"
    elif value>=77:
        LGrade="C+"
    elif value>=70: 
        LGrade="C"
    elif value>=60:
        LGrade="D"
    elif value<60:
        LGrade="F"
    return LGrade

def drop_lowest(lst):
    """Drops the lowest value from the list.

    Args:
        lst (list[float]): A list of decimal numbers.

    Returns:
        A new list with the lowest item dropped.

    Hint:
        This is a deceptively simple function.

        Consider how you would find where the value to remove is and then how
        you'd remove it separately! Make sure it works for all sizes of list!
    """
    if len(lst)==0:
        return
    
    lowestValue=lst[0]
    outl=[]
    LowestValueIndex=0
    for i in range(len(lst)):
        if lst[i]<lowestValue:
            lowestValue=lst[i]
            LowestValueIndex=i
        
    for i in range(len(lst)):
        if i == LowestValueIndex:
            pass
        else: outl+=[lst[i]]

    return outl  # TODO; Write this function

def points_to_percents(name, names, earned, listed):
    """Converts the points `got` and points `max` lists into a list percentages
    for the names matching `name`.

    All lists should be the same length.

    Args:
        name (str): The assignment name to convert.
        names (list[str]): A list of assignment names.
        earned (list[float]): A list of points earned.
        listed (list[float]): A list of points listed on the assignment.

    Returns:
        A list of percentages for the requested assignment name.
    """
    scores=[]

    if len(names)==len(earned) and len(earned)==len(listed):
        for i in range(len(names)):
            if names[i]==name:
                scores+=[earned[i]/listed[i]]

                  
    return scores  # TODO; Write this function

def unweighted_score(scores: list[float], length: int):
    """Calculate the unweighted score from a list of percentages.

    If `len(scores)` is greater than `length`, drop as many as is needed to only
    ever have at most `length` .

    Args:
        scores (list[float]): A list of scores.
        length (int): The maximum number of entries to use.

    Returns:
        The average score.
    """
    for i in range(len(scores)):
        if scores[i]<0:
            print("Invalid Score!")
            return
    # Drop all lowest values that we can
    while len(scores) > length:
        scores = drop_lowest(scores)
    
    sumOfScores=0
    for i in range(len(scores)):
        sumOfScores+=scores[i]
    avgScore=sumOfScores/len(scores)

    return avgScore  # TODO; Complete this function

def weighted_score(scores):
    """Calculates the weighted score for each assignment type.
    Args:
        scores (list[float]): A list of unweighted percentages, from 0.0 to 1.0.
        This list should be exactly 6 items long.
    Returns:
        The weighted percentage, from 0.0 to 1.0 inclusive.
    """

    weights = get_weights(scores)
    totalGrade=0
    for i in range(0,6):
        totalGrade+=(scores[i]*weights[i]);  #potential problem here , not sure what

    return totalGrade  # TODO; Complete this function 


def get_grades(types: list[str], earned: list[float], listed: list[float]): #problem at i=4

    """Calculates and displays all information related to grades.

    Args:
        types (list[str]): A list of assignment types. Can only be entries in
        `ALL_TYPES` otherwise that entry is ignored.
        earned (list[float]): The earned number of point on the problem.
        listed (list[float]): The number of points the assignment was worth.
    """

    # TODO; Complete this function; some things are missing.

    scores = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(len(ALL_TYPES)):

        percents = points_to_percents(ALL_TYPES[i],types,earned,listed);  # What should we do here
        # Convert percentages to the score for this assignment type
        if len(percents) == 0:
            scores[i] = -1.0  # If there is nothing, set to an invalid value
        else:
           scores[i]=unweighted_score(percents,MAX_TYPES[i])
    
    # Display all of the data
    print(f"weighted_scores({scores}) returns us {weighted_score(scores)}.")
    
    display_data(weighted_score(scores), scores)


################################################################################
# Main

def main():
    get_grades(["A","DD","E","X","KC","KC","KC","A","A","DD","DD", "E","F"],[90,90,100,99,64,100,85,75,92,20,20,85,90],[100,80,100,100,100,100,100,100,20,20,10,85,100])  # TODO; Your Testing Here


if __name__ == "__main__":
    main()
