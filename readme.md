# Readme

This is your notepad for planning your project. It is a one-time document.

It also serves as the landing page when someone visits your repo; in that sense, it's a kind of greeting & marketing tool as well.

## OUR PROJECT

### Group members

Alex Macri

### What it is

The Game of Life: The Game. A game based on the Game of Life, John Conways' cellular atomata game where you set up a "universe" of cells as live or dead, and see how they interact, grow, and die with eachother.

### User Stories

You can: Play the original game created by John Conway, you can play a set of pre-made target mode levels where you create a structure under constraints that will make a specific output, and you can create your own "target mode" levels (and export them for friends to try).

### Components

Original Game of Life: A solid recreation of the original, made with pygame, is at the center of the entire project.

Target system and map editor: A target system is the entire point of target mode, which is a big draw for this game in general. And, a map editor will keep the game interesting long after the pre-made target mode levels have been completed. The map editor also brings a community aspect to the project, as you can import and export any maps you want

Intuitive UI and menu: Many other recreations of this game I've seen online have been severely lacking in this area, so this an area where my version will stand out. For instance, instead of speed controls, it will have dynamic speeding (updates slightly faster as time goes on), and a single-update forward button in some modes. Also, to pick cells, you can click and drag, as if you were making art in MS Paint
### Assets

- Crossed/lined out square image for forbidden cell
- Green square image for target cell
- Background unpressed image for buttons
- Background pressed image for buttons
- Font for buttons and UI
- Sound for an update while the game of life is playing
- Sound for winning a target mode round
- Sound for UI button clicks
- Sound for UI button unclicks
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
(this plan wasn't remotely realized, how it actually happened can be seen in my logs)