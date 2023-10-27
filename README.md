# Conway-Life-Game

Description:
This project contains a Python script that visualizes the evolution of cellular automaton as per the rules of Conway's Game of Life. Utilizing the `matplotlib` library, the script showcases the dynamics of cells on a grid over time through an animated display.

Dependencies:
- Python
- NumPy
- Matplotlib

Installation:
1. Clone the repository to your local machine.
```bash
git clone https://github.com/Oliveryfaso/Conway-Life-Game.git
```
2. Navigate to the project directory.
```bash
cd your-repository-name
```
3. Install the required dependencies.
```bash
pip install -r requirements.txt
```
Note: If the `requirements.txt` file doesn't exist, you can create it with the following content:
```plaintext
numpy
matplotlib
```

Usage:
1. Run the `game_of_life.py` script using Python.
```bash
python game_of_life.py
```
2. The script will generate an animated visualization of Conway's Game of Life, displayed in a window on your desktop.

Customization:
- You can customize the grid size and animation speed by modifying the `N` and `speed` variables respectively.
- Initial population of the grid can be adjusted by altering the probability values in the `np.random.choice` function.

Code Structure:
- The `update` function contains the logic for evolving the grid at each animation frame according to Conway's Game of Life rules.
- The grid is initialized with random values, and `matplotlib.animation.FuncAnimation` is used to create the animation.
- The script sets up the figure and axes, displays the grid, and runs the animation, which is shown using `plt.show()`.

License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Contribute:
- Issue Tracker: https://github.com/Oliveryfaso/Conway-Life-Game/issues
- Source Code: https://github.com/Oliveryfaso/Conway-Life-Game

Support:
If you are having issues, please let us know.
Email: 2021190905021std.uestc.edu.cn

Acknowledgements:
- Conway's Game of Life: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
