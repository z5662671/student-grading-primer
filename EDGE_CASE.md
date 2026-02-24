# Document your edge case here
- To get marks for this section you will need to explain to your tutor:
1) The edge case you identified
2) How you have accounted for this in your implementation

One edge case that I accounted for was there being no students when calling the stats endpoint. To handle
this edge case i added a check that made sure there was at least 1 student before attempting to calculate
count, average, min and max.