import { ChildProcess } from 'child_process';
import * as fs from 'fs';
import { updateLanguageServiceSourceFile } from 'typescript';


const filaName = 'data.txt';

export interface Component {
    // Interface like class to represent the directory that could contain 
    // Files or other directories
    // Main functions will be to add a file, add a directory, or return the file size.
    children: Component[];
    calculateSize(): number;

    isFile(): boolean;

    name: string;
    addFile(file: Component): void;
    removeFile(file: Component): void;
    containsDirectory(name: string): boolean;
}

export class Directory implements Component {
    public children: Component[] = [];
    public name: string = '';

    constructor(name: string) {
        this.name = name;
    }


    public addFile(file: Component): void {
        this.children.push(file);
        console.log(`Added file: ${file.name} to ${this.name}, this is the current list of children: ${this.children.forEach(value => console.log(value.name))}`)
    }


    public isFile(): boolean {
        return false;
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

    public containsDirectory(name: string): boolean {
        if (name === this.name) {
            return true;
        }
        for (const child in this.children) {
            if (this.name === name) {
                return true;
            }
        }
        return false;
    }


}


/**
 * Class representation of a file 
 * The lowest level leaf component and where all the work gets done. 
 */
export class File implements Component{
    public name: string = '';
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
    public addFile(): void {
        
    }
    public removeFile(file: Component): void {
        
    }
    public containsDirectory(name: string): boolean {
        return false;
    }
}


const fileSring = fs.readFileSync(filaName, 'utf-8');
const lines = fileSring.split('\n');
// We are essentially going throuhg and changing what we are doing at each level
// if its not a command, we are adding it to the current directory
// if its a file, we create a new file and add that to the current directory
// 
let topLevelDirectory = new Directory('/');
let currentDirectory: Directory  = topLevelDirectory;

let directoryStack: Directory[] = [currentDirectory];

let totalSum = 0

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
                if (!currentDirectory.containsDirectory(lineArr[2])) {
                    console.log("Current directory does not contain " + lineArr[2])
                    currentDirectory.addFile(new Directory(lineArr[2]));
                }
                directoryStack.push(currentDirectory);
                currentDirectory = currentDirectory.children.filter(directory => !directory.isFile).find(directory => directory.name === lineArr[2])!;
                console.log(`Changing into directory: ${lineArr[2]}, and current Directory is ${currentDirectory}`);
            }
        }   
        else if (lineArr[1] === 'ls') {
            console.log("Listing directories")
        }
    }
    else if (lineArr[0].match(/\d/)) {
        // Make a new file and add it to the current directory
        const file = new File(parseInt(lineArr[0]));
        currentDirectory.addFile(file);
        console.log("Adding a file, and currentDirectory is: " +  currentDirectory.name);
        
    }
    else if (lineArr[0] === 'dir') {
        // add the directory to the current directory
        console.log("Adding directory " + lineArr[1] + " and current directory is " +  currentDirectory.name)
        currentDirectory.addFile(new Directory(lineArr[1]));   
        console.log(`current directories children: ${currentDirectory.children.forEach(value => console.log(value.name))}`)
    }
}

function recurseThroughTree(toplvlDirectory: Component, sum: number): number {
    const queue = [toplvlDirectory];

    const visited = new Set<Component>();


    while (queue.length > 0) {
        const currentDirectory = queue.shift();

        if (!visited.has(currentDirectory!)) {
            visited.add(currentDirectory!);
        }

        

        for (const child of currentDirectory!.children) {

            if (!child.isFile()) {
                queue.push(child);
                if (child.calculateSize() <= 100000) {
                    sum += child.calculateSize();
                }
            }
            
        }

    }

    return sum;
}
    


console.log(recurseThroughTree(topLevelDirectory, 0));

