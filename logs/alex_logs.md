# INSTRUCTIONS FOR THE INDIVIDUAL LOG
* This file must be updated once a day after your work.
* First, save this in your project folder with your name. For example: `jacob_log.md`.
* After each day, copy and paste the template below, and fill in the data.
* Then: stage, commit & push it to your git repo.


### Log for 2021-06-03

> **Goals for today:** pull repo, set up the basic project structure with starter pyglet files, update readme.md, and create diagrams / plan

> **Accomplished:** pulled repo, set the the basic project structure with starter pyglet files, updated readme.md, and learned about the diagram/plan formats (UML and Gantt) and started to make them

> **Plans for next day:** finish diagram/plans in UML and Gantt format (finish UML and touch up Gantt), and make the original Game of Life in pyglet

> **Problems/bugs noted:** -


### Log for 2021-06-04

> **Goals for today:** Finish UML and touch up Gantt

> **Accomplished:** Finished Gantt and continued with UML

> **Plans for next day:** Make the rest of the UML diagrams and start process on recreating the original Game of Life in pyglet

> **Problems/bugs noted:** -


### Log for 2021-06-05

> **Goals for today:** Finish UML diagrams and start making the free play mode

> **Accomplished:** Made some progress on UML diagrams

> **Plans for next day:** Finish UML, and maybe start the free play mode

> **Problems/bugs noted:** -

> **Other notes:** I guess I heavily underestimated how long it'd take to learn about UML, then actually plan out the whole project in that foramt. Even though I'll start out the week off schedule, I'm not too worried, since it'll be all but guarunteed smooth sailing from here, due to this planning


### Log for 2021-06-08

> **Goals for today:** (Finally) finish UML and start making the free play mode

> **Accomplished:** (Finally) finished UML, it took a lot longer than expected

> **Plans for next day:** Touch up planning stage things and start making the free play mode

> **Problems/bugs noted:** -

> **Other notes:** didn't have too much time yesterday to work on this, so I didn't write a daily log


### Log for 2021-06-09

> **Goals for today:** Make UML revisions and continue making free play mode

> **Accomplished:** Made most of my UML revisions and continued making free play mode

> **Plans for next day:** Finish UML once and for all, and get a lot (if not all) of free play mode done

> **Problems/bugs noted:** -

> **Other notes:** I forgot to do these for the past couple days. Today and yesterday I worked on essentially the same stuff, with more of a focus on the free play mode than the UML yesterday, so this can almost act as a log for both days


### Log for 2021-06-10

> **Goals for today:** Finish UML and Gantt and planning revisions, and make the mode and scene functionality

> **Accomplished:** Finished UML and Gantt planning and revisions, and made some of the mode and scene functionality

> **Plans for next day:** Finish (or at least make progress on) implementation of Free play and finish the mode and scene switching functionality

> **Problems/bugs noted:** -

> **Other notes:** Since I'm conceptually done the free play mode (I've done a few tests, thought things through, and wrote down what the logic will be), I'm moving on to the basis of the "mini engine" I'm making for this game. Even though it says otherwise in my Gantt chart, I now believe the whole GameWindow -> Mode -> Scene architecture would be a good idea to build earlier on rather than later, since I've made it'll be so easy to add and connect more things as I build


### Log for 2021-06-12

> **Goals for today:** Continue with scene functionality and free play

> **Accomplished:** Made good progress on scene switching and free play

> **Plans for next day:** Finish free play and scene switching

> **Problems/bugs noted:** I can't upscale a loaded image in pyglet (it graphically "glitches" if it shows up at all), but I can downscale it. Won't be doing that, though, since my original purpose for resizing was to have smaller file sizes with lower resolution assets that I could just stretch out in-game, but I guess I can't do that

> **Other notes:** I didn't make one yesterday because I planed on making one today, and I knew that at least one of these two days I didn't need to make one, so I thought this would be fine. I also spent more time yesterday on the research assignment, so not as much got done here


### Log for 2021-06-13

> **Goals for today:** Finish scene functionality and free play

> **Accomplished:** Arguably finished the scene functionality, and made some good progress on free play (I made ways to create and display the universe (with SOME reaction to mouse presses), and worked on the logic a bit in another python file that I will inevitably delete once I implement its ideas)

> **Plans for next day:** Finish free play and scene switching (this time for sure), and get started on buttons and the main menu

> **Problems/bugs noted:** I can't pass in the parent mode and scene controllers to the scenes as arguments, or else I end up getting an ImportError due to a circular import. This has the easy solution of just linking them manually after instantiation, but that is a whole other bag of worms that I'll have to explore tomorrow, to make sure it's really the right choice

> **Other notes:** I have heavily deviated from the Gantt chart, to the point where I'll consider redoing it (especially sine it didn't take much time to do in the first place). At this point I strongly doubt I'll have the time to do any sort of edit mode. In fact, since I have to juggle the research assignment, math, and any other extra ICS3U or ICS4U extra work, I'll be scrambling to even finish target mode


### Log for 2021-06-14

> **Goals for today:** Revise/finish scene functionality and cellular automata logic, and make progress on free play

> **Accomplished:** Made the revisions of the scene functionality (namely how I linked them together with parents), and fully revised the cellular automata "update" function to the point where I'm happy to implement it visually. I started that visual implementation (free play mode), but didn't get too far

> **Plans for next day:** Finish that visual implementation (free play mode), which also means making UI elements like panels and buttons (that's also most of the work for the main menu)

> **Problems/bugs noted:** same as last time (circular import for parent controller import), but this time directed at the annotation side of things

> **Other notes:** I am running extremely low on time. I get that I don't have to have this completely done, but ideally I'd really want the free and target modes done (along with the main menu obviously) because all those together resemble a full game (the map editor would be a fun gimmick, but this wouldn't exactly feel incomplete without it)


### Log for 2021-06-15

> **Goals for today:** Revise/finish scene functionality and cellular automata logic, and make progress on free play

> **Accomplished:** Finally, fully finished the scene and mode switching, and got further in implementing the free play mode

> **Plans for next day:** Finish the free play, menu, and target modes (which includes elements like the buttons and target system)

> **Problems/bugs noted:** (nothing that hasn't already been fixed or isn't in obvious early development)

> **Other notes:** A common theme in this project has been me spending far more days than anticipated on one thing. First it was the UML, now it's the scene switching functionality. Of course I'm happy with how both of those turned out now that it's over, but it took way too long to get them there. If I spend tomorrow making as much as I can in terms of actual game modes, and Thursday polishing and adding all the documentation, I'll do fine in terms of timing


### Log for 2021-06-16

> **Goals for today:** Make the button UI element, and finish a basic version of the main menu and free play mode (sadly, target mode just isn't a practical goal anymore for my deadline)

> **Accomplished:** FINALLY, finished a (very) basic version of the main menu and free play mode (which also meant making the button UI element)

> **Plans for next day:** Polish off what I have, and make it presentable. This means: adding the pause panel, finishing my in-code documentation, cleaning up my logs and readme, making my report, adding the menu title, adding the backdrop, and adding sound FX. And when I get bored, I will "test out the free play mode"

> **Problems/bugs noted:** - (as you can tell by now, I don't like ending off nights with known bugs lingering)

> **Other notes:** Even though I now know I can't get target mode done by Friday, it was still extremely satisfying to see everything (and I say "everything" very lightly) come together today. I've become quite the fan of Conway's Game of Life while researching for this project and working on it, and, though you may think I'm biased, my version was a lot easier to use than the ones online. It may not have speed controls, but I'm (probably) gonna work on automatic dynamic speed (which is even better), and it may not be an infinite world, but that's not totally a bad thing (it creates new outcomes to explore. For instance, gliders turn into 2x2 static blocks when they hit the wall. That's pretty cool, I wonder what people could do with stuff like that)


### Log for 2021-06-17

> **Goals for today:** Add the pause panel, finish the in-code documentation, clean up the logs and readme, add the menu title, and do any other bug fixes if I run into any (I've given up on the bgm and sfx being done today)

> **Accomplished:** Small fixes of previously unknown bugs, and added some more buttons/features (forward and reset), and automtic stopping. Also, you can't click any button except for stop when you are actively playing. I got busy with the math exam and other assignments before I could move on to any of the actual things I wanted to do today

> **Plans for next day:** Do what I actually wanted to do today. This means: adding the pause panel, finishing my in-code documentation, cleaning up my logs and readme, making my report, adding the menu title, and adding sound FX. In that order. If I get done all that, I'll really click around and look for some bugs

> **Problems/bugs noted:** - (as you can tell by now, I don't like ending off nights with known bugs lingering)

> **Other notes:** I'll be fine if I don't completely get all of those things done, but I really need to do those documentation things the most


### Log for 2021-06-19

> **Goals for today:** Add the pause panel, finish the in-code documentation, clean up the logs and readme, add the menu title, and do any other bug fixes if I run into any

> **Accomplished:** Everything I wanted to: I added the pause panel and main menu title, and I cleaned up the in-code documentation, daily logs, and readme

> **Plans for next day:** Today's the last day that I'm formally working on this project as a school project, but as the summer goes on I'll keep going with it until my origina plan for it is realized. Even though I'll still use github, I won't be making any more of these logs. Sure, it is pretty fun looking back at all of them, and how I constantly fell further back behind schedule, but I just don't believe it's a practical thing to do as a part of a hobby passtime, at least for me

> **Problems/bugs noted:** Again, none, and I'm pretty confident in this, because I do a good amount of testing for all the different cases when I think of after I code in a new feature. The only reason one of them went under the radar (the one I fixed last time) was because that error is very hard to run into with pyglet's slow mouse position updates (and even then, it was a very minor error that seemingly doesn't effect the window itself)

> **Other notes:** Even though I didn't get all the modes I wanted to done, I'm pretty satisfied with the work I did here. I made all the infrastructure for something I'll definitely keep working at as summer starts. Being able to switch modes and scenes, and even bring up smaller sub-windows/panels in those scenes, all in pyglet, was pretty cool, and excited to find out what I have to come up with next. I'm also considering going further with this infrastructure stuff I did, and making a small "game engine" based off pyglet (or, at least turning the scene and mode switching into some sort of pakcage after some revisions)