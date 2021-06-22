# Feedback

## Overview

**Group:** Alex

**Date marked:** 2021-06-21

**General comment:** Excellent work. Represents a high level of competence with Python and a good understanding and exploration of the software development process. There are various gaps to fill in your approach that will make it easier to realize the more ambitious goals for this project, but this is a high level of achievement for ICS4U.

### Marks

**K/U:** Level 4+

> The knowledge/understanding mark is primarily for code quality.

**T:** Level 4+

> The thinking mark is primarily for code organization & documentation.

**C:** Level 4++

> The communication mark is primarily for logs and reporting.

**A:** Level 4++

> The application mark is primarily for use of Git & Agile (planning, committing, folder structure).

### ICS3U / 4U

In the sections below, the first few come from the ICS3U version of the project, and evaluations are mostly relevant to that level. The final section contains ICS4U-specific notes.

## Commit history

98 commits / 13 days ~= 7.5 commits / day. Quite frequent for a single team member. In a professional team, fewer is probably more desirable because of the clutter it generates to look through / verify in a proper code vetting process. This can be done by only committing either before/after significant changes or 1-2x a day (e.g. code & log as separate commits), whichever is more frequent. For example, the 3 commits on June 4 for logs could be one commit, and individual commits for each documented class aren't really necessary. As a filter for worthwhile commits, you can ask yourself: "Would someone want to either (a) see what the code looked like on this day or (b) check the changes I made to see what happened and how it affected their code?" However, your descriptive commit messages do a lot to mitigate this because they do allow the location of potentially breaking changes for the purposes of rollbacks of bug-fixing.

## Logging

**Individual log for Alex:** Good record both of having logs for each day and an (almost) daily commit for each log. The logs are highly detailed with a good mix of high-level and technical commentary. I can get a very good sense of how progress updated and plans were revised. P.S. [Accurate estimation is impossible](https://codebots.com/library/way-of-working/why-are-software-estimates-so-hard)!

## Design & planning

Excellent. A good chunk of time was spent on the design and planning phase, thinking quite thoroughly about overall layout and even revising it. It may seem like the oversights, such as how modes will be switched by buttons, are significant, but they're comparatively minor compared to nailing down the framework that makes such questions even possible. As you noted in your logs, the work done in advance gave you a pretty clear direction and, for the most part, your plan was possible to realize. The final report also describes additional aspects of the planning, including a Word doc for brainstorming.

## Structure of project

* logs are in logs folder: ✓

* code is in src folder: ✓

* images, sounds, etc. are in assets folder: ✓ 

* folders and files are named descriptively: ✓ Although `run.py` is a nontraditional filename. Typically, it will be called `main.py` or `__init__.py` (the latter because of [a pre-3.2 standard](https://docs.python.org/3/reference/import.html#regular-packages), no longer relevant but quite likely to be seen in the wild when you work with others' codebases).

* redundant files have been cleaned up: ✓

## Code documentation

* readme.md complete: ✓

* docstrings on all functions: ✓ Some could be more detailed. An example is `Free.mouse_press`, where the docstring is "Event handler for a mouse press" followed by a 40-line body whose purpose can't be guessed from that overivew. A full docstring might read: "Handle a mouse press. Determine the state and the bounds of the button in which the press occurred, then activate the button if possible."

* type annotations on all functions: ✓

* comments for hard-to-understand or dense blocks of code: Yes, quite consistent in this area.

* sources: Only a reference to Conway's Game of Life. (Others might not have been used.)

## Code quality

* Files: Very good division into different files as a reflection of the modules of your design.

* Functions: Mostly good; many functions have one responsibility and are reasonable length. There are, however, some exceptions. For example, in `Free.update_universe`, the density of that function strongly suggests that parts could be extracted. I'll discuss this further in the ICS4U section.

* Constants: ✓ (as enums). Note that there are some constants in `assets.py` that should be uppercase, e.g. `DEAD_RGBA`.

* Imports: Good. All at the tops of their relevant files and not many redundancies.

* Style: Excellent. Three points, in descending order of importance: (1) Docstrings are not all uniform format. Remember: an imperative, full sentence. "Event handler for a mouse press" vs. "Handle a mouse press." (2) Occasionally there is visual crowding where comments are interleaved with code without blank line separators. (3) There are some spelling & grammar errors that the IDE should catch ("seperate"). There was only one name I noticed was questionable: `Free.__generate_universe_states`; from the point of view of `Free`, it would seem to be the state of the universe and as such be singular, whereas it's named from the cell's point of view -- misleading me into thinking each state would generate all previous ones. 

* Testing: Just described playtesting.

* Algorithms: Very good solutions to the problems. Interestingly, there are few algorithms since this became mainly a design/organization project. The main one is of course the cell update algorithm, which is quite a good approach to optimizing the problem of interacting cells (namely, by creating records of cells to resurrect or kill, instead of making the mistake of doing it as you iterate and thereby corrupting the state for unchecked cells, adding an implementation detail of which index you start at, etc...).

## Features

An ambitious set of features, of which a solid number were completed, and with more-than-satisfactory thoroughness. Even simply adding a way to switch back to the menu mode does a good job of demonstrating the flexibility of the UI structure. One UX feature I would say is semi-important is disabling buttons that are unavailable to prevent confusion. For example, when the simulation is running, there is no feedback when pressing 'Reset' -- nothing happens but the symbolism tells me it should.

## Final report

Very good description of your process, your obstacles, your successes. Well-written and specific. I would only suggest paragraphs for organization as a minimum, and subheaders as an ideal.

## Additional ICS4U requirements

* User stories: We didn't spend very much time on this. As such, the extremely basic ones that are there are OK. For your own benefit, there are many resources to investigate on user stories; here's a [random one](https://www.mountaingoatsoftware.com/agile/user-stories).

* UML diagrams: The revised version is nice and clean. Lots of attention paid to small details. Fairly accurately represents the end state, too.

* Planning diagrams: Good Gantt chart. I don't think i've ever seen targets "climb up" from the bottom of the chart, though. They should all be falling.

* Modular approach: Overall very good. There are several core OOP principles in view here, not least implementation of interfaces and encapsulation (you were quite careful with encapsulation, and concern for it even slowed down your decision about how to interact with GameWindow.) There are a few notes to make:
  
** Given how much power you've given Scenes, I'm not sure Modes are needed, even as a state; if they are to exist, I would assume that they're handling more of the game logic ("model"), such that all the universe tracking in `Free` (a `Scene`) could be in `FreeMode`, with `FreeScene` handling only the UI logic ("view").

** `Free.__update.universe` and similar functions are begging for a `Universe` class. The fact that much of this logic will be relevant in other modes (or at the very least made available to future modes) makes it very odd to incorporate in a `Scene`, which (to reiterate) should only be interface-related.

*** As a minor related note, if you were to go full MVC and separate out logic from interface, you would create some doubles, for example a `CellSprite` owned by either a `Universe` or a `Cell` that would handle things like `__define_sprite` and `__update_sprite`. (In fact, a small change like this would be worthwhile even without an MVC rewrite.)

** The many if/elif blocks in `Free.mouse_press` and `Free.mouse_release` are suspicious in OOP. They are parallel to switch/case, which in OOP is considered a [code smell](https://www.c-sharpcorner.com/article/switch-statement-a-code-smell/). The alternative is to always move in the direction of self-handling cases, for example through polymorphism. Imagine if you could replace these functions with a block that reads: `for button in self.buttons: if button.is_active() and button.is_pressed(): button.execute()`, possibly with `return` if you need to enforce the `elif` part of it (to avoid simultaneous presses on a touchscreen). This would require `button.execute` to be mapped to a different function depending on the button, of course, which is often done by either creating a class per button (with very little to override) or, as you've done, simply extend the parameterization of your `Button` class to include the command it should execute. This is actually closest to how classic GUIs like tkinter work: when you instantiate a `Button`, you have to supply the `command`, and you'll notice that you never have to check for mouse presses in the bounds of buttons. (In full MVC, you would go a step further and use the [`Observer/Observable`](https://en.wikipedia.org/wiki/Observer_pattern) pattern, which is beyond the scope of the course.)

* Test suite: Given the time constraints and the one-month nature of this implementation of ICS4U, I will waive this. For future reference: [unittest](https://docs.python.org/3/library/unittest.html)

* Building: Given the time constraints and the one-month nature of this implementation of ICS4U, I will waive this. For future reference: [pyinstaller](https://datatofish.com/executable-pyinstaller/)

* Manual: Given the time constraints and the one-month nature of this implementation of ICS4U, I will waive this.
