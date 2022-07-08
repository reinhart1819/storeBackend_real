
def start_tests():
    print("------- Lists tests -------")

    nums = [1,2,3,4,5,6]

    print( nums[0])
    print( nums[1])

    nums.append(9)
    print(nums)

    for n in nums:
        print(n)


    for number in range(0,21):
        print(number)


def test1():
    print("test1")

    prices = [123,3,23,6475,58,89,45,34,87,34,-12,23, 123,-23,-123, 0, 123, 0, -29, 10]
    count = 0
    sum = 0
    sum_non_zero = 0
    zeros = 0
    for n in prices:
        sum += n

        if n > 0:
            sum_non_zero +=n

        if n == 0:
            zeros +=1    

        if n < 50:
            print (n)
            count += 1

    print(f"there are {count} prices lower then $50")


def test2():
    print("------- test 2 -------")

    users = [
        {
            "gender": "F",
            "name": "Louis",
            "color": "Green"
        },
        {
            "gender": "M",
            "name": "Manuel",
            "color": "Gray"
        },
        {
            "gender": "F",
            "name": "Rossy",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Renny",
            "color": "pink"
        },
        {
            "gender": "M",
            "name": "Roman",
            "color": "Purple"
        },
        {
            "gender": "m",
            "name": "John",
            "color": "Pink"
        },
        {
            "gender": "F",
            "name": "Susan",
            "color": "Black"
        },
    ]
    print(len(users))
    for user in users:
        print(user["name"])

    print("Users who like pink")
    for user in users:   
        if user["color"].lower() == "pink":
            print(user["name"]+ " " + "likes pink")


def test3():
    print("----- test 3 -----")

    prices = [123,3,23,6475,58,89,45,34,87,34,-12,23, 123,-23,-123, 0, 123, 0, -29, 10]
    solution = prices[0]
    for price in prices:
        if price > solution:
            solution = price
            break
    print(solution)
    
            
             
    



start_tests()
test1()
test2()
test3()