#Tomas Hornicek, no collaborators,no sources,no extension
#Problem 3
def neighbor_sum(a_list):
    b_list = []
    for index in range(len(a_list)):
        if index == 0:
            total = a_list[0]+ a_list[1]

        elif index == len(a_list) - 1:
            total = a_list[index] + a_list[index - 1]
        else:
            total = a_list[index] + a_list[index - 1] + a_list[index + 1]
        b_list.append(total)
    return b_list
print(neighbor_sum([17, 32, 1, 8, 11, 90]))


#Problem4
def get_income_tax(list_of_incomes):
    return [calculate_tax(income) for income in list_of_incomes]

def calculate_tax(income):
    total_tax = 0
    if income >= 12550:
        income -= 12550
    else:
        income = 0
    if income >= 523601:
        total_tax += (income - 523600) * 0.37
    if income >= 209426:
        if income >= 523601:
            total_tax += (523600 - 209425) * 0.35
        else:
            total_tax += (income - 209425) * 0.35
    if income >= 164926:
        if income >= 209426:
            total_tax += (209425 - 164925) * 0.32
        else:
            total_tax += (income - 164925) * 0.32
    if income >= 86376:
        if income >= 164926:
            total_tax += (164925 - 86375) * 0.24
        else:
            total_tax += (income - 86375) * 0.24
    if income >= 40526:
        if income >= 86376:
            total_tax += ( 86375 - 40525) * 0.22
        else:
            total_tax += (income - 40525) * 0.22
    if income >= 9951:
        if income >= 40526:
            total_tax += (40525 - 9950) * 0.12
        else:
            total_tax += (income - 9950) * 0.12
    if income >= 9950:
        total_tax += 9950 * 0.1
    else:
        total_tax += income * 0.1
    return total_tax

print(get_income_tax([112550]))

#Problem 5

class SetSuite:
    def __init__(self,list_of_lists):
        self.list_of_sets = [set(list) for list in list_of_lists]

    def add_set(self,a_list):
        a_set = set(a_list)
        self.list_of_sets.append(a_set)

    def get_sets(self):
        return [list(set) for set in self.list_of_sets]

    def union_all(self):
       return set().union(*self.list_of_sets)

    def intersection_all(self):
        if len(self.list_of_sets) > 0:
            return list(self.list_of_sets[0].intersection(*self.list_of_sets))
        else:
            return list()

#Testing
my_SetSuite = SetSuite([[1,2,3],[3,3,5],[7,8,3,2,2],[3,6,6,9,10]])

intersection = my_SetSuite.intersection_all()
print(intersection)
print(my_SetSuite.get_sets())
union = my_SetSuite.union_all()
print(union)
get = my_SetSuite.get_sets()
print(get)
add = my_SetSuite.add_set((1,3,3,5,4))
print(my_SetSuite.get_sets())

new_SetSuite = SetSuite([])
print(new_SetSuite.intersection_all())

#Problem6

def pascal(row):
    if row == 0:
        return [1,]
    else:
        result = []
        previous_row = pascal(row - 1)
        for i in range(row + 1):
            if i == 0:
                result.append(1)
            elif i == row:
                result.append(1)
            else:
                row_member = previous_row[i] + previous_row[i -1]
                result.append(row_member)
        return result
print(pascal(0))
print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))
print(pascal(5))
print(pascal(6))

#Problem7

def perfect_power(num_1,num_2):
    if num_2 == num_1:
        return True
    elif num_2 < num_1:
        return False
    else:
        return perfect_power(num_1,num_2/num_1)
#Testing
print(perfect_power(5, 125))
print(perfect_power(5, 25))
print(perfect_power(5, 10))
print(perfect_power(2, 8))

