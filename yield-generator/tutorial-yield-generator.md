## [Yield in Python Tutorial: Generator & Yield vs Return Example](https://www.guru99.com/python-yield-return-generator.html)

### What are Generators in Python?

Generators are functions that return an iterable generator object. The values from the generator object are fetched one at a time instead of the full list together and hence to get the actual values you can use a for-loop, using next() or list() method. 

### When to use Yield Instead of Return in Python

- Use yield instead of return when the data size is large
- Yield is the best choice when you need your execution to be faster on large data sets
- Use yield when you want to return a big set of values to the calling function
- Yield is an efficient way of producing data that is big or infinite.