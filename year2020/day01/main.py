import os
from util import get_input


#
#   Find the two entries in the expense reports that sum to year2020
#   and calculate the product of these two numbers.
#

def product_of_sum():
    expense_reports = get_input('./input')
    for i, val_1 in enumerate(expense_reports):
        for j, val_2 in enumerate(expense_reports[i+1:]):
            for val_3 in expense_reports[j+i+2:]:
                if val_1 + val_2 + val_3 == 2020:
                    print(val_1, val_2, val_3, val_1 * val_2 * val_3)
                    return






def main():
    product_of_sum()
    return


if __name__ == '__main__':
    main()


