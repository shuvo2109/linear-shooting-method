# linear-shooting-method
This python program allows you to calculate the numerical values for Linear ODEs with boundary values. Check `Theory.pdf` for more clarity about what kind of ODEs to solve and other details.

## Required Python Version
This program requires `Python 3.X` or above. It was originally written using `Python 3.10`.

## How to Use
Open the `shooting_method.py` file using a suitable editor (Notepad++ recommended) to edit the functions `p`, `q` and `r`. These functions correspond to the p(x), q(x) and r(x) functions respectively as provided in the `Theory.pdf` file. Use Python syntax for editing the functions and make sure to `return` proper `value`. Do not change anything else in the file.

Once you have changed the `shooting_method.py` file, save it and run it. Enter the values of `a`, `b`, `alpha`, `beta` and `N` (these variables retain their meanings from `Theory.pdf`) and the script will calculate and display the numerical values using 4th Order Runge-Kutta Method.

## Required Libraries and Modules
This program uses the `math` module. Any other modules might be required depending on how the user defines `p`, `q` and `r`.

## Files Included
- `Theory.pdf` contains the mathematical background of the code and all underlying calculations
- `shooting_method.py` contains the code to be editted and executed.

## Contact Information
For any queries or confusion, contact: rahman.fahimur21@gmail.com

