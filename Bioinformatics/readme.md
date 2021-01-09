
## Python for Bioinformatics 
### Chapter 2
#### Problems
1. what is the different between  ```range``` and ```arange``` functions ?

Answ.
```range()``` is a built-in python class while ```arange()``` is a function belongs to a third party library ```NumPy```.
Ref.
https://realpython.com/how-to-use-numpy-arange/#:~:text=The%20main%20difference%20between%20the,using%20the%20Python%20for%20loop.

2. Using the ```numpy.random``` module, create a vector of random numbers?

Answ.

```

import numpy as np
y = np.random.random(10)
print(y)

```

```
[0.97865888 0.45305264 0.31631339 0.95946004 0.41120162 0.44141162 0.20908311 0.54928171 0.44097501 0.9714066 ]
```

3. Without using the ```for``` or ```while``` commands , computer the average of a vector of ```1 million``` random numbers.

Answ.

```

import numpy as np
data = np.random.random(1000000)
avgg = np.average(data)
print(avgg)

```


4. Compute the sum of the columns of a large matrix of random numbers. 

Answ.



5. Create a vector of random numbers having a range of``` -1 to +1```.

Answ.




6. Create a matrix of random numbers . Multiply this matrix by  scalar in a single Python command.

Answ.




7.  Create a ```5 x 3 ``` matrix of random numbers. Create a vector of three random numbers. What happens when you run a ```matrix * vector``` ? 


Answ.




8.  Compute the transpose of a matrix.

Answ.



9. Create a random DNS string and write a Python script to convert the letters to an array of numbers``` (A=1 , C=2 ,  G=3, T=4 )```. Do not use loops ```(for , while )``` to accomplish this conversion. (This can be accomplished in five commands, including the creation of the DNA string. )  

Answ.







