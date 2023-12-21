# 0x04. Loops, conditions and parsing

## Introduction
Loops are used to repeat a block of code until a certain condition is met. The two main types of loops in bash are for and while.
-   `for`  loops iterate over a list of items and execute a block of code for each item. Here's a basic example:

```
for i in 1 2 3
do
   echo $i
done
```
-   `while`  loops execute a block of code as long as a certain condition is true. Here's a basic example:

```
i=1
while [ $i -le 3 ]
do
   echo $i
   i=$((i+1))
done
```
Conditions in bash are used to make decisions in our code. We often use them with if, elif, and else statements to execute different blocks of code based on whether certain conditions are true or false. Here's a basic example:

```
if [ "$a" -gt "$b" ]
then
    echo "a is greater than b"
elif [ "$a" -eq "$b" ]
then
    echo "a is equal to b"
else
    echo "a is less than b"
fi
```
In this example, -gt checks if $a is greater than $b, and -eq checks if $a is equal to $b. There are many other condition checks you can use in bash.

## Files/Tasks

  
|     Tasks           |Files                       |
|----------------|-------------------------------|
|0. Create a SSH RSA key pair|`0-RSA_public_key.pub`            |
|1. For Best School loop|`1-for_best_school`            |
|2. While Best School loop|`2-while_best_school`|
|3. Until Best School loop|`3-until_best_school`|
|4. If 9, say Hi!|`4-if_9_say_hi`|
|5. 4 bad luck, 8 is your chance|``5-4_bad_luck_8_is_your_chance``|
|6. Superstitious numbers|`6-superstitious_numbers`|
|7. Clock|`7-clock`|
|8. For ls|`8-for_ls`|
|9. To file, or not to file|`9-to_file_or_not_to_file`|
|10. FizzBuzz|`10-fizzbuzz`|
  

