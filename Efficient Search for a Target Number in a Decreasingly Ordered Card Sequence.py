# Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
#
# alt
# This may seem like a simple problem, especially if you're familiar with the concept of binary search, but the strategy and technique we learning here will be widely applicable, and we'll soon use it to solve harder problems.

# Problem
# We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.
#
# Input
# cards: A list of numbers sorted in decreasing order. E.g. [13, 11, 10, 7, 4, 3, 1, 0]
# query: A number, whose position in the array is to be determined. E.g. 7
# Output
# position: The position of query in the list cards. E.g. 3 in the above case (counting from 0)
def locate_card(cards, query):

#     creating a variable position with the value 0
    position = 0
#     set up a loop for repetition
    while True:
#         check if the element at the current position matche the query
        if cards[position] == query:
            # Answer found! Return and exit..
            return position
        position += 1
    # check if we have reached the end of an array
    # if position == len(cards):
    #     # number not found, return -1
    #     return -1

