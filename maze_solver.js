// Mert Gulmus - 211ADB070

class Maze {
    constructor(filename) {
        this.filename = filename;
        this.array = this.readMaze();
    }

    // import maze from file
    importMaze = () => {
        const fs = require('fs');
        const data = fs.readFileSync(this.filename, 'utf8');
        return data;
    }

    // convert maze to 2D array
    readMaze = () => {
        const maze = this.importMaze();
        const mazeArray = maze.split('\n');
        mazeArray.forEach((row, index) => {
            // also remove \r from each row
            mazeArray[index] = row.replace('\r', '');
        });
        return mazeArray;
    }

    // find starting point
    findStart = () => {
        const maze = this.array;
        for (let i = 0; i < maze.length; i++) {
            for (let j = 0; j < maze[i].length; j++) {
                if (maze[i][j] === 'S') {
                    return [i, j];
                }
            }
        }
    }

    // find ending point
    findGoal = () => {
        const maze = this.array;
        for (let i = 0; i < maze.length; i++) {
            for (let j = 0; j < maze[i].length; j++) {
                if (maze[i][j] === 'G') {
                    return [i, j];
                }
            }
        }
    }
}

const maze = new Maze('mazes/maze_11x11.txt');
console.log(maze.importMaze());
console.log(maze.findStart());
console.log(maze.findGoal());
