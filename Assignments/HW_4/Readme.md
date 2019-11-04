HW #4 Memcached

Team name: The Original

Team Members:
Tejas Madappa
Chandra Mohan
Vedant Bhoj
Ketan Rudrurkar
Hao Ran Chen

Here are the characteristic of the program InMemoryCache.java.

1. Items will expire based on a time to live period.

2. Cache will keep most recently used items if you will try to add more items then max specified. 

3. For the expiration of items we can timestamp the last access and in a separate thread remove the items when the time to live limit is reached. This is nice for reducing memory pressure for applications that have long idle time in between accessing the cached objects.

4. We have also created test class: InMemoryCacheTest.java
