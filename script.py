import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import copy
import math
import time

class State:
    def __init__(self, sheet, total_items, placed_items):
        self.sheet = sheet
        self.total_items = total_items
        self.placed_items = placed_items

def can_place_item(sheet, l, w, x, y):
    """Check if the item can be placed at position (x, y) on the sheet."""
    l_int = math.ceil(l)
    w_int = math.ceil(w)
    for i in range(l_int):
        for j in range(w_int):
            if x + i >= len(sheet) or y + j >= len(sheet[0]) or sheet[x + i][y + j] == 1:
                return False
    return True

def place_item(sheet, l, w, x, y):
    """Place the item at position (x, y) on the sheet."""
    l_int = math.ceil(l)
    w_int = math.ceil(w)
    new_sheet = copy.deepcopy(sheet)
    for i in range(l_int):
        for j in range(w_int):
            new_sheet[x + i][y + j] = 1
    return new_sheet

def branch_and_bound(L, W, items, max_iterations=100000, max_runtime=60):
    """
    Use branch and bound to place as many smaller items of different sizes on a larger sheet of size L*W.
    Stopping conditions are provided by max_iterations and max_runtime.
    """
    start_time = time.time()
    L_int = math.ceil(L)
    W_int = math.ceil(W)
    initial_sheet = [[0 for _ in range(W_int)] for _ in range(L_int)]
    initial_state = State(initial_sheet, 0, [])

    best_state = initial_state
    stack = [initial_state]

    iterations = 0  # To track the number of iterations

    while stack:
        current_state = stack.pop()

        iterations += 1
        if iterations % 1000 == 0:
            print(f"Iteration: {iterations}, Items placed so far: {current_state.total_items}, Stack size: {len(stack)}")

        # Check stopping conditions
        if iterations >= max_iterations:
            print(f"Stopping due to reaching max iterations: {max_iterations}")
            break
        if time.time() - start_time >= max_runtime:
            print(f"Stopping due to reaching max runtime: {max_runtime} seconds")
            break

        for item in items:
            l, w = item
            for i in range(L_int):
                for j in range(W_int):
                    if can_place_item(current_state.sheet, l, w, i, j):
                        new_sheet = place_item(current_state.sheet, l, w, i, j)
                        new_placed_items = current_state.placed_items + [((i, j), (i + l, j + w))]
                        new_total_items = current_state.total_items + 1
                        new_state = State(new_sheet, new_total_items, new_placed_items)

                        if new_total_items > best_state.total_items:
                            print(f"New best state found with {new_total_items} items.")
                            best_state = new_state

                        stack.append(new_state)

    print(f"Branch and bound completed after {iterations} iterations and {time.time() - start_time:.2f} seconds.")
    return best_state.total_items, best_state.placed_items

def visualize_placement(L, W, items, placed_items):
    """
    Visualize the placement of items on the larger sheet.
    """
    fig, ax = plt.subplots()
    ax.add_patch(patches.Rectangle((0, 0), W, L, edgecolor='black', facecolor='none', label=f"Larger Sheet {L}x{W}"))
    colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
    for idx, (start, end) in enumerate(placed_items):
        (x, y), (x2, y2) = start, end
        l, w = x2 - x, y2 - y
        color = colors[idx % len(colors)]
        ax.add_patch(patches.Rectangle((y, x), w, l, edgecolor='blue', facecolor=color, label=f"Item {l}x{w}"))

    # Add annotations
    ax.text(0.5, -0.1, f"Total Larger Sheet: {L} x {W}", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
    ax.text(0.5, -0.15, f"Total Items Placed: {len(placed_items)}", horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

    # Create a custom legend
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys())

    ax.set_xlim(0, W)
    ax.set_ylim(0, L)
    ax.set_aspect('equal', adjustable='box')
    plt.gca().invert_yaxis()
    plt.xlabel('Width')
    plt.ylabel('Length')
    plt.title('Placement of Items on the Larger Sheet')
    plt.show()

def run_branch_and_bound():
    try:
        L = float(length_large_entry.get())
        W = float(width_large_entry.get())
        items = []
        for entry in item_entries:
            l = float(entry[0].get())
            w = float(entry[1].get())
            items.append((l, w))

        print("Starting the branch and bound algorithm...")
        total_items, placed_items = branch_and_bound(L, W, items)
        print(f"Total items placed: {total_items}")
        print("Positions of placed items:")
        for item in placed_items:
            print(item)

        print("Visualizing the placement...")
        visualize_placement(L, W, items, placed_items)
        print("Visualization completed.")
    except ValueError:
        print("Please enter valid numeric values for all dimensions.")

def add_item_fields():
    row = len(item_entries) + 6
    length_entry = ttk.Entry(mainframe)
    width_entry = ttk.Entry(mainframe)
    length_entry.grid(row=row, column=0, sticky=(tk.W, tk.E))
    width_entry.grid(row=row, column=1, sticky=(tk.W, tk.E))
    item_entries.append((length_entry, width_entry))

# Create the GUI
root = tk.Tk()
root.title("2D Bin Packing")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(mainframe, text="Enter the dimensions of the larger sheet:").grid(row=0, column=0, columnspan=2)

ttk.Label(mainframe, text="Length:").grid(row=1, column=0, sticky=tk.W)
length_large_entry = ttk.Entry(mainframe)
length_large_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Width:").grid(row=2, column=0, sticky=tk.W)
width_large_entry = ttk.Entry(mainframe)
width_large_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Enter the dimensions of the smaller items:").grid(row=3, column=0, columnspan=2)

item_entries = []
add_item_fields()

add_button = ttk.Button(mainframe, text="Add Item", command=add_item_fields)
add_button.grid(row=5, column=0, columnspan=2)

run_button = ttk.Button(mainframe, text="Run", command=run_branch_and_bound)
run_button.grid(row=6, column=0, columnspan=2)

root.mainloop()
