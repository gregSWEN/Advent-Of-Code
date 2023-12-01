"use strict";
exports.__esModule = true;
exports.File = exports.Directory = void 0;
var fs = require("fs");
var filaName = 'data.txt';
var Directory = /** @class */ (function () {
    function Directory(name) {
        this.children = [];
        this.name = '';
        this.name = name;
    }
    Directory.prototype.addFile = function (file) {
        this.children.push(file);
        console.log("Added file: ".concat(file.name, " to ").concat(this.name, ", this is the current list of children: ").concat(this.children.forEach(function (value) { return console.log(value.name); })));
    };
    Directory.prototype.isFile = function () {
        return false;
    };
    Directory.prototype.removeFile = function (file) {
        this.children = this.children.filter(function (child) { return child === file; });
    };
    Directory.prototype.calculateSize = function () {
        var totalSize = 0;
        for (var _i = 0, _a = this.children; _i < _a.length; _i++) {
            var directory = _a[_i];
            totalSize += directory.calculateSize();
        }
        return totalSize;
    };
    Directory.prototype.containsDirectory = function (name) {
        if (name === this.name) {
            return true;
        }
        for (var child in this.children) {
            if (this.name === name) {
                return true;
            }
        }
        return false;
    };
    return Directory;
}());
exports.Directory = Directory;
/**
 * Class representation of a file
 * The lowest level leaf component and where all the work gets done.
 */
var File = /** @class */ (function () {
    function File(size) {
        this.name = '';
        this.children = [];
        this.fileSize = size;
    }
    File.prototype.calculateSize = function () {
        return this.fileSize;
    };
    File.prototype.isFile = function () {
        return true;
    };
    File.prototype.addFile = function () {
    };
    File.prototype.removeFile = function (file) {
    };
    File.prototype.containsDirectory = function (name) {
        return false;
    };
    return File;
}());
exports.File = File;
var fileSring = fs.readFileSync(filaName, 'utf-8');
var lines = fileSring.split('\n');
// We are essentially going throuhg and changing what we are doing at each level
// if its not a command, we are adding it to the current directory
// if its a file, we create a new file and add that to the current directory
// 
var topLevelDirectory = new Directory('/');
var currentDirectory = topLevelDirectory;
var directoryStack = [currentDirectory];
var totalSum = 0;
var _loop_1 = function (line) {
    var lineArr = line.split(' ');
    if (lineArr[0] === '$') {
        if (lineArr[1] === 'cd') {
            if (lineArr[2] === '..') {
                //Change to the last directory
                currentDirectory = directoryStack[directoryStack.length - 1];
                directoryStack.pop();
                console.log(directoryStack);
            }
            else {
                // Add the directory to the stack and make this the current directory
                // Find a way to find the directory name that matches the one passed in
                if (!currentDirectory.containsDirectory(lineArr[2])) {
                    console.log("Current directory does not contain " + lineArr[2]);
                    currentDirectory.addFile(new Directory(lineArr[2]));
                }
                directoryStack.push(currentDirectory);
                currentDirectory = currentDirectory.children.filter(function (directory) { return !directory.isFile; }).find(function (directory) { return directory.name === lineArr[2]; });
                console.log("Changing into directory: ".concat(lineArr[2], ", and current Directory is ").concat(currentDirectory));
            }
        }
        else if (lineArr[1] === 'ls') {
            console.log("Listing directories");
        }
    }
    else if (lineArr[0].match(/\d/)) {
        // Make a new file and add it to the current directory
        var file = new File(parseInt(lineArr[0]));
        currentDirectory.addFile(file);
        console.log("Adding a file, and currentDirectory is: " + currentDirectory.name);
    }
    else if (lineArr[0] === 'dir') {
        // add the directory to the current directory
        console.log("Adding directory " + lineArr[1] + " and current directory is " + currentDirectory.name);
        currentDirectory.addFile(new Directory(lineArr[1]));
        console.log("current directories children: ".concat(currentDirectory.children.forEach(function (value) { return console.log(value.name); })));
    }
};
for (var _i = 0, lines_1 = lines; _i < lines_1.length; _i++) {
    var line = lines_1[_i];
    _loop_1(line);
}
function recurseThroughTree(toplvlDirectory, sum) {
    var queue = [toplvlDirectory];
    var visited = new Set();
    while (queue.length > 0) {
        var currentDirectory_1 = queue.shift();
        if (!visited.has(currentDirectory_1)) {
            visited.add(currentDirectory_1);
        }
        for (var _i = 0, _a = currentDirectory_1.children; _i < _a.length; _i++) {
            var child = _a[_i];
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
