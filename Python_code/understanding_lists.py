
numbers=[10,20,30,40,50];
print(numbers);
print(numbers[1:3]);
print(numbers[:3]);
numbers.append(60);
numbers.append(70);
numbers.append(99);
print('After appending Numbers : '+str(numbers));
numbers.remove(99);
print('After removing wiered Number : '+str(numbers));
numbers.append(420);
print('After adding bad Number : '+str(numbers));
del numbers[6];
print('After deleting using del keyword : '+str(numbers));