# 2D Bin Stacking Problem

## Background

The 2D Bin Stacking Problem is a classic problem in operations research and computer science. It involves arranging smaller items of varying dimensions on a larger sheet (or bin) of fixed size in a way that maximizes the usage of the available space. This problem has numerous real-world applications, including:

- **Logistics and Warehousing**: Efficiently packing items into containers or pallets to optimize space and reduce transportation costs.
- **Manufacturing**: Cutting raw materials such as fabric, metal, or wood with minimal waste.
- **Retail**: Arranging products on shelves or in storage areas to maximize space and improve accessibility.

## Description of the Code

The provided Python code solves the 2D Bin Stacking Problem using the branch and bound algorithm and visualizes the placement of items on the larger sheet. The code also includes a graphical user interface (GUI) for user input and visualization.

### Key Components

1. **State Class**
   - Represents the state of the sheet, including the current layout (`sheet`), the total number of items placed (`total_items`), and the positions of the placed items (`placed_items`).

2. **can_place_item Function**
   - Checks if an item of given dimensions can be placed at a specific position on the sheet without overlapping other items.

3. **place_item Function**
   - Places an item on the sheet at the specified position and returns a new sheet with the item placed.

4. **branch_and_bound Function**
   - Implements the branch and bound algorithm to find the best way to place as many items as possible on the larger sheet. It considers various stopping conditions like maximum iterations and runtime.

5. **visualize_placement Function**
   - Uses `matplotlib` to create a visual representation of the placed items on the larger sheet.

6. **run_branch_and_bound Function**
   - Integrates the GUI with the branch and bound algorithm. It reads the user input, runs the algorithm, and visualizes the result.

7. **add_item_fields Function**
   - Adds fields in the GUI for users to input the dimensions of additional smaller items.

8. **GUI Setup**
   - Utilizes `tkinter` to create a user-friendly interface for inputting the dimensions of the larger sheet and smaller items, and for running the algorithm.

### Usage

1. **Install Required Libraries**
   - Ensure you have the required libraries installed:
     ```sh
     pip install tkinter matplotlib
     ```

2. **Run the Script**
   - Execute the script to launch the GUI:
     ```sh
     python script.py
     ```

3. **Input Dimensions**
   - Enter the dimensions of the larger sheet.
   - Add dimensions for each smaller item by clicking the "Add Item" button.

4. **Run the Algorithm**
   - Click the "Run" button to start the branch and bound algorithm.
   - The result will be displayed in the console, and a visualization of the placement will be shown.

### Example

```python
# Example usage of the branch_and_bound function
L = 10  # Length of the larger sheet
W = 10  # Width of the larger sheet
items = [(3, 3), (4, 2), (2, 5)]  # List of items with their dimensions

total_items, placed_items = branch_and_bound(L, W, items)
print(f"Total items placed: {total_items}")
print("Positions of placed items:")
for item in placed_items:
    print(item)

# Visualize the placement
visualize_placement(L, W, items, placed_items)
