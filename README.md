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

Here the command line will prompt with 3 choices:

```
Do you want to:
                    (1) Run Establishment
                    (2) Run Enlightenment
                    Or you can exit by typing 0

```

Enter the choice of yours as input and proceed.

1. Establishment
----------------
 - Sample Room1:
    ```
    // room1.txt
    [ 0, 'X', 0, 'X']
    ['G', 0,  0, 'E']
    [ 0, 'B', 0,  0 ]
    ['X', 0, 'G', 0 ]
    ```
 - The sequence is required here to proceed.
 - Takes the sequence as input and prints the room after executing all possible moves until the brynjolf left without moves.
    ```
    input: ludrrr

    [ 0, 'X', 0, 'X']
    ['G', 0,  0, 'E']
    ['B', 0,  0,  0 ]
    ['X','G', 0,  0 ]
    output: (lose: executed 2 moves of 5)

    input: urrd

    ['G', 'X',  0,  'X']
    [ 0,   0,   0,  'E']
    [ 0,   0,   0,  'G' ]
    ['X',  0,   0,   0 ]
    output: (win: executed 3 moves of 5)
    ```
 - The moves will decide whether brynjolf win or lose and also it'll will prompt if the sequence is undecided after certain moves.
    ```
    input: uuuuuu

    ['G', 'X', 'G', 'X']
    [ 0,  'B',  0,  'E']
    [ 0,   0,   0,   0 ]
    ['X',  0,   0,   0 ]
    output: (undecided: executed 4 moves of 6)
    ```

2. Enlightenment
----------------
 - Sample Room:
    ```
    // room.txt
    [ 0,  0,  0,  'X']
    ['G', 0,  0,  'X']
    [ 0, 'B', 0,  'E']
    ['X', 0,  'G', 0 ]
    ```
 - Here the input sequence is optional. It'll print the winning path/sequence if nothing is provided.
    ```
    input: <no input>
    output: win: rr
    ```
 - Otherwise it'll execute all the moves from the squence and will print the remaining winning moves if exists.
    ```
    input: ududu
    output: win: drr
    ```
 - If there is no way to win after a certain wrong move it'll prompt as below:
    ```
    input: d
    output: stuck: no way to win
    ```


Here you can give any input to try it on your own to give an escape route to the legendary Brynjolf or let your algorithm do the magic by hitting enter with empty input.


### Specifications
This Brynjolf alogorithm uses:
- Python version 3
- Recursion Algorithm used to find the path.
- Brynjolf will cover the path to exit (E/O) in four directions named Left (l), Right (r), Up (u) or Down (d) until he hit a wall (X) or overlap any guard on his way (G) or he reaches end of the boundaries.
- Accordingly the guards will also move in the same direction as **Brynjolf**.

### Requirements
 * pytest
    - Install it by typing following command:
    ```
    $ pip install -U pytest
    ```
 * python version 3

#### To run pytest
    ```
    pytest test.py -s
    ```
