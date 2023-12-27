This fill will contain the progress I made.

### Initial:
Data Loading, Testing for Duplicate and Null values.

Only the Latitude and Longitute Columns have Null values.
These values are to be filled using the latitude and longitude values of the same pin code, or if pin code is unreliable, use the distributor code.

Some Pincodes are unreliable, such as 0, 89, 92, 123456, and 63748

Decided to cluster by skipping the missing values.
Can't cluster the points directly, so decided to divide them into batches and cluster them.
I think the best way to go about this is to cluster them into batches, and then cluster them again. This might sound like more work, but it decreases the work load a lot


Things I want to try:
- Try other clustering methods, as k means could potentially be bad. (Not in this case after reading, because all points that need to be clustered are locally situated).
- Optimise the current algorithm to run faster.
