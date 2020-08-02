**These are notes on Panda3d, the 3D modeling api for python that I eventually decided on to use for my drone 3D modeling program**

* So, I pulled out MOST of my information from the documentation provided by the api's website: https://docs.panda3d.org/1.10/python/index

* I also found these youtube tutorials to be very effective for learning panda3d: https://youtu.be/LNMz52Pkl_U

* To start off, I highly recommend (and went through it myself) the introduction to Panda3D tutorial on the above site. 
  * It definitely takes some time to complete, but I reccomend it heavily.
  * Unfortunately, the tutorial does not talk too much about how to import models for use into panda3D, which I will explain how I did below.
  
* How to import/create models into Panda3d:
  * 3D modeling "cheat-sheet": https://docs.panda3d.org/1.10/python/more-resources/cheat-sheets (under "models")
  * The 3D modeling program that Panda3d recommends (and that I would recommend as well despite my lack of 3D modeling knowledge) would be Blender
    * Blender is essentially just a 3D modeling program that allows for easy import, manipulation, and export of 3D models of differing file types.
    * For more information on Blender, see the "Notes on Blender"
    * The main file type of Blender is "filename.blender", which is a bit of problem for panda3d, since it does not accept that file type 
    * Here lied the main problem that I came across with using Blender, for a bit I was stuck, just trying to figure out how to export files in a format that panda3d would accept and model.
    * The main issue that I ran into was that Blend2Bam, the utility that panda3d reccomends to transfer ".blend" files to ".bam" files (which can be loaded by panda3d), was deprecated for the current version of Blender (at the time of my research, it may not be now). So, for a while I truely believed I was stuck and made little progress into my 3D modeling software.
    * However, after a little while I was able to find a reddit thread that was describing an issue sort of similar to mine, but it was talking about exporting ".gltf" files to ".bam" files. I got curious, and I looked at the export options provided by Blender natively. I did not see ".gltf" as an option so I was confused why the person had this problem until I looked into the preferences on Blender. To my surprise, I found out that Blender actually had an option to export to ".gltf" that was not enabled it. So, I turned on that option and downloaded the converter that was provided on the reddit thread (https://github.com/Moguri/panda3d-gltf). Then, I was able to (after some conversion of files) convert ".blender" files to ".bam" files!
    * I will note that this may have been easier for someone that has experience in 3D modeling programs, but unfortunately this was VERY new to me personally.
  * Important Note!: This method for file transfer is not completely perfect, it (for some reason) imports the models as without color and entirely black (which is not TOO much of a problem, but for anyone continuing this research, you may want to have a look into it). I tried exporting the models and transferring them several times and this problem persisted.
 
 ** Important notes on what I used from Panda3d:**
   * So, this is a brief summary on what I used from panda3d to create my 3d environment

* Panda3d worlds:
  * Panda3d contains "worlds", which are essentially the three-dimensional space that objects lie in
  * The main resource that I used for reference in creating worlds in this software was this tutorial: https://grimfang-studio.org/data/books/book1/Panda3D%20Book%201.pdf
    * This gives a brief explanation of worlds, and how they work, as well as a brief introduction to objects/models/actors as well. (objects are the representations of 3d models, and actors are specific types of objects that present their own functions)
  * In VERY basic summary, in order to create a world:
    * You have to have the correct imports (which are listed in my document)
    * You have to initialize the showbase, the documentation of which is listed here: https://docs.panda3d.org/1.10/python/reference/direct.showbase.ShowBase
    * Then in code you obviously have to create an object related to the world (where the showbase is initiated), then you have to call ".run()" on that object
    
* Panda3d Models/Objects:
  * I would refer again to this tutorial: https://grimfang-studio.org/data/books/book1/Panda3D%20Book%201.pdf for the creation of models
  * Also, I would refer to this example program created in Panda3d: https://docs.panda3d.org/1.10/python/introduction/tutorial/starting-panda3d
    * Start with this page and I would recommend running through the rest of the example program's tutorial
    * Also, I would reccommend going through the documentation that it provides.
  * There is also a fairly lengthy tutorial on Models and Actors here: https://docs.panda3d.org/1.10/python/programming/models-and-actors/index
    * I would go through this and read the explanation personally.
  * In order to create models, I would also recommend going through this, which talks about panda3d scene graphs: https://docs.panda3d.org/1.10/python/programming/scene-graph/scene-graph-manipulations
    * Mainly, pay attention to the "reparentTo" function, as it is VERY important for properly loading models.
  * In a VERY basic summary, in order to create objects in a world (done in the "init" function of whatever class, but doesn't NEED to necessarily)
    * You have to load the model (shown in code) and create a new model object with the "loadModel" function
    * You have to reparent the model to the graph's main scene node with "reparentTo" (shown in code)
    * Then, I would recommend this but it is not a necessity, you SHOULD set the model's scale and position (the posistion is auto-set to x=0,y=0,z=0)

* Panda3d sequences:
  * I would refer to this tutorial for sequences: https://docs.panda3d.org/1.10/python/programming/intervals/sequences-and-parallels
  * Also, this is another good tutorial which covers "posinterval" which I used a LOT to move the drone: https://docs.panda3d.org/1.10/python/introduction/tutorial/using-intervals-to-move-the-panda
  * This example program created by the panda3d devs is helpful too: https://docs.panda3d.org/1.10/python/introduction/tutorial/starting-panda3d
  * Also, while I did not use "Tasks" to accomplish this program, here is a message board on both "tasks" and "sequences": https://discourse.panda3d.org/t/sequence-and-task-solved/5469
  * In a VERY basic summary, in order to create sequences:
    * You first need to create a blank (or not blank) sequence object
    * Then, you need to attach some sort of animation to that sequence object through the ".seq.add()"
    * More information on animations here: https://docs.panda3d.org/1.10/python/programming/models-and-actors/actor-animations
