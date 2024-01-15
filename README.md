# Linear Regression Analysis
This program performs linear regression analysis and calculates the Pearson correlation coefficient for a given dataset. It reads the dataset from a file and calculates the slope, intercept, and correlation coefficient.

# Usage
1. Make sure you have Python installed on your system.
2. Clone this repository or download the code files.
3. Prepare a dataset file with numeric values, where each value represents a data point on the y-axis. Each data point should be on a separate line.
4. Run the program by executing the following command: 
```
python main.py <dataset_file>
```
** Note: Replace <dataset_file> with the path to your dataset file.

The program will process the dataset and display the linear regression line equation and the Pearson correlation coefficient.

# Example
* Suppose you have a dataset file named data.txt with the following contents:
```
2
4
6
8
10
```

* You can run the program with the following command:

```
python main.py data.txt
```

* The output will be:
```
Linear Regression Line: y = 2.000000x + 2.000000
Pearson Correlation Coefficient: 1.0000000000
```