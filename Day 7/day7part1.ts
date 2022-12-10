import * as fs from 'fs';


const filaName = 'data.txt';

export interface Component {
    // Interface like class to represent the directory that could contain 
    // Files or other directories
    // Main functions will be to add a file, add a directory, or return the file size.
    children: Component[];
    calculateSize(): number;

    isFile(): boolean;
}

export class Directory implements Component {
    public children: Component[] = [];
    private name: string = '';

    constructor(name: string) {
        this.name = name;
    }


    public addFile(...files: Component[]): void {
        for (const file of files) {
            this.children.push(file);
        }
       
    }


    public isFile(): boolean {
        return false;
    }
    public getName(): string {
        return this.name;
    }

    public removeFile(file: Component): void {
        this.children = this.children.filter(child => child === file);
    }


    public calculateSize(): number {
        let totalSize: number = 0;
        for (const directory of this.children) {
            totalSize += directory.calculateSize();
        }
        return totalSize
    }


}


/**
 * Class representation of a file 
 * The lowest level leaf component and where all the work gets done. 
 */
export class File implements Component{
    private fileName?: string = '';
    public children: Component[] = [];
    private fileSize: number;

    constructor(size: number) {
        this.fileSize = size;
    }
    public calculateSize(): number {
        return this.fileSize;
    }

    public isFile(): boolean {
        return true;
    }
}


const fileSring = fs.readFileSync(filaName, 'utf-8');
const lines = fileSring.split('\n');
// We are essentially going throuhg and changing what we are doing at each level
// if its not a command, we are adding it to the current directory
// if its a file, we create a new file and add that to the current directory
// 
let topLevelDirectory = new Directory('/');
let currentDirectory: Directory = topLevelDirectory;

let directoryStack = [currentDirectory];


for (const line of lines) {
    let lineArr = line.split(' ');
    if (lineArr[0] === '$') {
        if (lineArr[1] === 'cd') {
            if (lineArr[2] === '..') {
                //Change to the last directory
                currentDirectory = directoryStack[directoryStack.length-1];
                directoryStack.pop();
                console.log(directoryStack);
            }
            else {
                // Add the directory to the stack and make this the current directory
                // Find a way to find the directory name that matches the one passed in
                currentDirectory = directoryStack.find(directory => directory.getName() === lineArr[2])!;
                directoryStack.push(currentDirectory);
            }
        }
        else if (lineArr[1] === 'ls') {
            console.log('listing directories');
        }
    }
    else if (lineArr[0].match(/\d/)) {
        // Make a new file and add it to the current directory
        const file = new File(parseInt(lineArr[0]));
        currentDirectory.addFile(file);
    }
    else if (lineArr[0] === 'dir') {
        // add the directory to the current directory
        const directoryAdd = new Directory(lineArr[1]);
        directoryStack.push(directoryAdd);
        currentDirectory.addFile(directoryAdd);   
    }
}

let totalSum = 0



function recurseThroughTree(toplvlDirectory: Component): any {
    if (toplvlDirectory.isFile()) {
        totalSum += toplvlDirectory.calculateSize();
        return
    }
    for (const directory of toplvlDirectory.children) {

        if (directory.calculateSize() <= 100000) {
            return recurseThroughTree(directory);
        }
    }

}

console.log(totalSum);
