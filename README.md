# Legacy Of Brynjolf


To run/execute the program, type below command in the command line:
```
$ python3 main.py < room.txt(optional file name) >
```
If you provide a file name which is existing in the current path:
- The input file which actually contains the blueprint of the Room containing the guards and exit (may be).

If you do not provide any file name (as it is optional)
- You will be asked to enter any file name to process or you can hit enter to go further (here you can be processed with already pre-defined "room.txt" file). And it will provide one of the possible solutions/path to reach the exit.

And even if you pass any file with Room blueprint:
- Defined functions in Room class will check for Brynjolf, Guards and Exit co-ordinates. If the given room blueprint doesn't consist Brynjolf or Exit co-ordinates, it'll exit from the process.

Here you can give any input to try it on your own to give an escape route to the legendary Brynjolf or let your algorithm do the magic by hitting enter with empty input.


### Specifications
This Brynjolf alogorithm uses:
- Recursion Algorithm used to find the path.
- Brynjolf will cover the path to exit (E/O) in four directions named Left (l), Right (r), Up (u) or Down (d) until he hit a wall (X) or overlap any guard on his way (G) or he reaches end of the boundaries.
- Accordingly the guards will also move in the same direction as **Brynjolf**.