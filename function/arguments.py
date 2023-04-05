def year_of_birth(name,age):# first example for arguments invoke it 3 times with diffrent country name
    year=2023-age
    print(f"Hello{name},you were born in {year}")


def my_country(country="Kenya"):# second example  invoke it 3times
    print (f"Hello you are from {country}")

def hello(*names): # third example invoke it 3 times 
    print(f"Hello {names}")

def sum (*nums):# invoke it a number of times
    answer=0
    for num in nums:
        answer +=num
    return answer
                
           
        #    def multiply_many(**kwargs):
        #      answer=1
        #      for num in kwargs.values():
        #           answer*=num
        #           return answer

        # A function named concatenate_args that takes any number of 
        # string arguments in positional arguments format and concatenates them into a single string

def concatenate_args(*args):
        result = " "
        for arg in args:
              result += arg
        return result


        # A function named concatenate_kwargs that takes any number of string arguments in keyword arguments 
        #  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
     return ''.join(kwargs.values())

     
     