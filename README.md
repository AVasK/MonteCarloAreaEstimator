# Monte-Carlo Area Estimator
* Estimating area of complex figures.

![Screenshot][pic]
[pic]: https://github.com/AVasK/MonteCarloAreaEstimator/blob/master/pic.jpg "How it all looks in real life"

- [x] Random Sampling
- [ ] SubRandom Sampling (for lower discrepancy, ~~__in theory__~~). 

## To run it ~if you ever need to~ write 
```python
MC(_list_of_vertices, iters, visualise = True or False, s_type = "rand" or "subrand")
```
Which will run a single iteration of Monte-Carlo ~which is really annoying, i know but i don't give sh*t~

### __OR__

```python
area(vertices, iters, mean_iters, s_type)
``` 
Which should theoretically calculate mean of mean_iters runs ~but it's buggy AF and **it will plot mean_iters graphs on your screen** and blow-up your PC occasionally~


