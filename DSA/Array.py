"""Array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array)."""

# Python program to demonstrate array in python
class List_info():
    def __init__(self):
        print("List is a Data Structure in python which is a collection of different data types ")
        self.arr = [1,2,'a','b']

    def show_append(self):
        print("Append a char or element")
        self.arr.append('c')
        print(self.arr)
    
    def show_extend(self):

        print("\nExtend the current arr with ['@','#','$']")
        self.arr.extend(['@','#','$'])
        print(self.arr)

    def show_insert(self):
        print("\n Inserting an element to an index of the arr")
        self.arr.insert(3,2)
        print(self.arr)

    def show(self):
        self.show_append()
        self.show_extend()
        self.show_insert()
        



obj = List_info()
obj.show()