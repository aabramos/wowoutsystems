def LoktarOgar(minNum, maxNum, multiple1, multiple2, string1, string2):
  '''
    Simple function to print a range of numbers, printing strings on the
    indicated multiples.

    Args:
        minNum: The first number that will be printed.
        maxNum: The last number that will be printed.
        multiple1: Define the multiple that will print the string1.
        multiple2: Define the multiples that will print the string2.
        string1: An string that will be printed instead of the number
        when the number is a multiple of multiple1.
        string2: An string that will be printed instead of the number
        when the number is a multiple of multiple2.

    Returns:
        None
  '''
  for number in range(minNum, maxNum + 1):
    if number % multiple1 == 0 and number % multiple2 == 0:
      print(string1 + string2)
    elif number % multiple1 == 0:
      print(string1)
    elif number % multiple2 == 0:
      print(string2)
    else:
      print(number)
