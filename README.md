## Schematic
<br>
 <img src="http://williamscotten.com/Actioniks/assets/img/hardware.png" width="400">
<br>

## How to Use
 
### Taking Pictures of the Cube:
 
To take a picture of the first side, the user places the cube with the white side face up beneath the usb webcam.  In order to snap the photo, the user clicks button 0 on the Pynq board.  The Pmod OLED will then print out what the board registered as the nine colors of the board.  The user then can choose whether those are colors are correct to move on to the next side, or if they are not, they can retake the picture of that side of the cube by pressing Button 1 on the Pynq board.  The order of taking the pictures is Front > Top > Back > Bottom > Left > Right.  The board can only solve the cube if the front facing side is the white side.  Once all of the pictures have been taken, the board will calculate the solution, assuming that a possible cube orientation was provided by the pictures. 
 
### Example Output after Picture is Taken:
<br>
 <img src="http://williamscotten.com/Actioniks/assets/img/pmod_output.jpg" width="400">
<br>

### Following the Solution from the Pmod:
 
Once the board is done calculating the solution (it should only take a second or two), it will the user the first move to make.  The board assumes that the user starts solving the cube with the same starting orientation as the one in the pictures.  For instance, holding the cube with the green side on top but having the Pynq board think  the orange side is the top will result in an unsolved cube.  The Pmod prints out the moves one by one, and waits for the user to press Button 0 before moving on to the next move.  The names of the moves the Pmod reads back to the user are the same as what people in the Rubik’s Cube community understand.  For instance, “Right Inverted” as understood by Cube solvers around the world is the same “Right Inverted” that is read back to the user.  The visual representations of the moves are shown below.  When the Pmod reads “Inverted” after a move’s name, it just means go in the opposite direction of that move.  When the Pmod reads “Twice” after a move’s name, that just means execute that move twice.  
 
### Example Solution Output after all Sides are Inputted:
<br>
 <img src="http://williamscotten.com/Actioniks/assets/img/jupyter_output.jpg" width="700">
<br>

 
### Pmod Instructions in Visual Form
<img src="http://williamscotten.com/Actioniks/assets/img/front.jpg" width="200"> <img src="http://williamscotten.com/Actioniks/assets/img/back.jpg" width="200"> <img src="http://williamscotten.com/Actioniks/assets/img/down.jpg" width="200">

<img src="http://williamscotten.com/Actioniks/assets/img/left.jpg" width="200"> <img src="http://williamscotten.com/Actioniks/assets/img/right.jpg" width="200"> <img src="http://williamscotten.com/Actioniks/assets/img/up.jpg" width="200">
