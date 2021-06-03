# Readme

This is your notepad for planning your project. It is a one-time document.

It also serves as the landing page when someone visits your repo; in that sense, it's a kind of greeting & marketing tool as well.

## OUR PROJECT

### Group members

Alex Macri

### What it is

A game based on the Game of Life, John Conways' cellular atomata game where you set up a "universe" of cells as live or dead, and see how they interact, grow, and die with eachother.

### User Stories

You can: play the original game created by John Conway, you can play a set of pre-made target mode levels, where you create a structure under constraints that will make a specific output, and you can create your own "target mode" levels, and export them for friends to try.

### Components

Original Game of Life: a solid recreation of the original, made with pygame, is at the center of the entire project.

Target system and map editor: a target system is the entire point of target mode, and though the map editor sounds like a tacked-on mode for bored players at first, it's actually a development tool first and foremost, that I'm just allowing players to use. To quickly and efficiently create target map levels for target mode, I'll need an effective format to store and display it in, and a good editor to easily create them in

Intuitive UI and menu: needless to say, these components will highly effect the overall user experience. Getting these components right will mean the difference between OK software and great software. The main menu will have one button for each mode: Free Play, Target Mode, and Map Editor. The UI and controls for each mode will slightly vary from one another. During setup, the player will be able to scroll up/down to zoom out/in, and right click/drag to traverse the screen. On the player control sidebar, there will be a switch to toggle what happens when you left click/drag, between making a cell live or dead. During setup, there will be a start and reset button. Those are all the same between the modes, but in free play mode, there will be a pause button, which pauses the playing game in its current state for you to manually edit, and a forward arrow button while paused to manually update and advance once. In edit mode, there will be all the extras of free play mode, and also a toggle to switch between editing the usual live/dead cell placing mode, and the target/forbidden cell placing mode. In the target/forbidden placing mode, the player control sidebar will also change. There will be no time controls like pause or play (since these cells are static), and instead of the toggle for live/dead, there will be two switches, both to toggle what happens when you left click/drag, between making or erasing cells, and making a target cell or forbiddne cell (if you aren't erasing). In edit mode, there will also be a save and export button at the bottom of each player control panel

### Assets

- White square image for live cell
- Black square image for dead cell
- Crossed/lined out square image for forbidden cell
- Green square image for target cell
- Background image for sidebar UI
- Background image for buttons
- Font for buttons and UI
- Sound for an update while the game of life is playing
- Sound for winning a target mode round
- Sound for UI button clicks
- BGM for menus
- BGM for free play
- BGM for target mode
- BGM for edit mode while placing target/forbidden cells (free play BGM will play while testing with live/dead cells)

### Projected schedule

Planning/structure diagrams:                2021-06-04
Original game of life in Pyglet:            2021-06-07
Target system and target mode:              2021-06-11
Edit mode:                                  2021-06-14
Menus:                                      2021-06-15
Final touches and sound/music:              2021-06-16
