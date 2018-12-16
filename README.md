# Monte-Carlo Area Estimator
* Estimating area of complex figures.

- [x] Random Sampling
- [?] SubRandom Sampling (for lower discrepancy, ~kinda~). 

## To run it ~if you ever need it~ write 
```
MC(_list_of_vertices, \#of_iterations, visualise = True/False, s_type = "rand"/"subrand")
```
Which will run a single probe of Monte-Carlo

### OR

```
area(vertices, iters, mean_iters, s_type)
``` 
Which should theoretically calculate mean of mean_iters runs ~but it's buggy and it will plot mean_iters graphs on your screen (ouch)~


