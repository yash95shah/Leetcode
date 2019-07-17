class Nstacks_with_array:
    def __init__(self, num_of_stacks, stacks_capacity):
        self.stacks_capacity, self.num_of_stacks = stacks_capacity, num_of_stacks
        self.data_store, self.top_of_stack, self.nextitem, self.nextavailable = [0] * self.stacks_capacity, \
                                                                                [-1] * self.num_of_stacks, [i + 1 for i
                                                                                                            in range(
                self.stacks_capacity - 1)], 0
        self.nextitem.append(-1)

    def push(self, stack_num, data):
        print("Top of stack: " + str(self.top_of_stack))
        print("Next Linked Item List: " + str(self.nextitem))
        print("Next Available: " + str(self.nextavailable))
        where_to_push = self.nextavailable
        print("Pushing item:---------------------------- " + str(data))
        self.nextavailable = self.nextitem[where_to_push]
        self.data_store[where_to_push] = data
        self.nextitem[where_to_push] = self.top_of_stack[stack_num]
        self.top_of_stack[stack_num] = where_to_push
        print("The array looks like: " + str(self.data_store))

        return

    def pop(self, stack_num):
        self.data_store[self.top_of_stack[stack_num]] = 0
        temp_val = self.nextitem[self.top_of_stack[stack_num]]
        self.nextitem[self.top_of_stack[stack_num]] = self.nextavailable
        self.nextavailable = self.top_of_stack[stack_num]
        self.top_of_stack[stack_num] = temp_val
        return

    def print_please(self):
        print(self.data_store)


created_by_me = Nstacks_with_array(3, 6)
created_by_me.push(0, 5)
created_by_me.push(0, 6)
created_by_me.push(1, 3)
created_by_me.push(2, 8)
created_by_me.push(0, 9)
created_by_me.pop(0)
created_by_me.pop(0)
created_by_me.print_please()
