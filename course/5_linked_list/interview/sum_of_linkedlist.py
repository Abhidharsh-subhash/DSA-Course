from base import LinkedList


# def sum_lists(ll1, ll2):
#     first = ""
#     second = ""
#     first_current = ll1.head
#     second_current = ll2.head
#     while first_current and second_current:
#         first += str(first_current.value)
#         second += str(second_current.value)
#         first_current = first_current.next
#         second_current = second_current.next
#     total = int(first[::-1]) + int(second[::-1])
#     new_ll = reverse_num(total)
#     result_ll = LinkedList()
#     for i in str(new_ll):
#         result_ll.add(int(i))
#     return result_ll


def sum_lists(ll1, ll2):
    first_current = ll1.head
    second_current = ll2.head
    reminder = 0
    result = LinkedList()
    while first_current and second_current:
        total = first_current.value + second_current.value + reminder
        rem = total // 10
        reminder = rem if rem != 0 else 0
        result.add(total % 10)
        first_current = first_current.next
        second_current = second_current.next
    return result


def reverse_num(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev


ll1 = LinkedList()
ll2 = LinkedList()
ll1.add(7)
ll1.add(1)
ll1.add(6)
ll2.add(5)
ll2.add(9)
ll2.add(2)
print(ll1)
print(ll2)
print(sum_lists(ll1, ll2))
