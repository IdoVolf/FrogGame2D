🛠️ prCr – Level Creator for *Frog Wilds*

prCr is a lightweight, tile-based level editor designed to help you (yes, you!) build and edit levels for the game *Frog Wilds*.

📚 How to Use

🎭 Layer System
- Press TAB to switch between two layers:
  - Layer 0 – Back layer: used for main gameplay tiles (e.g., ground, walls). Collision is detected here.
  - Layer 1 – Front layer: used for decorative elements like trees or clouds, placed visually on top of layer 0.

🎨 Drawing Tiles
- Hold Left Click to draw the currently selected tile.
- Press Right Click to erase a tile.
- Note: In version 1.1, there's no tile preview yet – just draw and see what you get!

🔢 Switching Tiles
Press the number keys (1–8) to select a tile type:
1. Grass
2. Dirt
3. Sky
4. Tree Branch
5. Tree Leaf
6. Sun
7. Clouds
8. Cave/Stone

💾 Saving Your Work
- Press S to save the current screen.
- It will create a .json file inside the levels/ folder.

🗂️ Adding Levels
To add a new level:
1. Create a folder called levelX (replace X with a number).
2. Inside that folder, add all your screens as .json files.
3. Name each screen like levelX0, levelX1, etc.

🔁 Updating Screens
- Press U to enter update mode.
- A new update/ folder will be created.
- Place the file you want to update in that folder.
- Press U again to load it for editing.
- ⚠️ Make sure the folder contains only one file to avoid confusion.

♻️ Resetting Canvas
- Press R to reset and clear the canvas (start fresh).

👷 Contributing
Feel free to fork the project, make levels, and send a pull request. We’d love to see your creations!
