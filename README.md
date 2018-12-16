# Monte-Carlo Area Estimator
* Estimating area of complex figures.

- [x] Random Sampling
- [ ] SubRandom Sampling (for lower discrepancy, ~kinda~). 

## To run it ~if you ever need to~ write 
```
MC(_list_of_vertices, \#of_iterations, visualise = True/False, s_type = "rand"/"subrand")
```
Which will run a single iteration of Monte-Carlo ~which is really annoying, i know but i don't give sh*t *'causeineverwantedtouseitanyway~

### OR

```
area(vertices, iters, mean_iters, s_type)
``` 
Which should theoretically calculate mean of mean_iters runs ~but it's buggy and it will plot mean_iters graphs on your screen (ouch)~


