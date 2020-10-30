# Kata-Java-HumanAfterAll
This kata is inspired by the [french social security number system](https://en.wikipedia.org/wiki/INSEE_code).

## Instructions
You have to add behaviours to an existing `__init__` method in the Human class.
This method takes in parameters a string (the social security number).

With this information you have to initiate the following attributes :
- sex (string)
- year_of_birth (string)
- month_of_birth (string)
- place_of_birth (string)

# Rules & examples
The rules to read a french social security number are :
- Sex
    - "Male" if the first digit is a 1
    - "Female" if the fist digit is a 2
    - You can use the Sex enum (`src/enums/Sex`) to assign the correct value
- Year of birth
    - The last passed year ending by the 2<sup>nd</sup> and 3<sup>rd</sup> digit
- Month of birth
    - The month of the year given by the 4<sup>th</sup> and 5<sup>th</sup> digit
- Place of birth
    - The department given by the 6<sup>th</sup> and 7<sup>th</sup> digit
    
For example, the number 1 98 06 78 123 456 78 represents :
- A male
- Born in 1998
- Born in June
- Born in the department 78

## Code
In the `src/main` folder, you will find the class `Human` with the current implementation of `__init__` to complete.

## Test it
You can test your implementation by running the `src/test/HumanTest` class.