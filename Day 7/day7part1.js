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
    Directory.prototype.addFile = function () {
        var files = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            files[_i] = arguments[_i];
        }
        for (var _a = 0, files_1 = files; _a < files_1.length; _a++) {
            var file = files_1[_a];
            this.children.push(file);
        }
    };
    Directory.prototype.isFile = function () {
        return false;
    };
    Directory.prototype.getName = function () {
        return this.name;
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
    return Directory;
}());
exports.Directory = Directory;
/**
 * Class representation of a file
 * The lowest level leaf component and where all the work gets done.
 */
var File = /** @class */ (function () {
    function File(size) {
        this.fileName = '';
        this.children = [];
        this.fileSize = size;
    }
    File.prototype.calculateSize = function () {
        return this.fileSize;
    };
    File.prototype.isFile = function () {
        return true;
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
                currentDirectory = directoryStack.find(function (directory) { return directory.getName() === lineArr[2]; });
                directoryStack.push(currentDirectory);
            }
        }
        else if (lineArr[1] === 'ls') {
            console.log('listing directories');
        }
    }
    else if (lineArr[0].match(/\d/)) {
        // Make a new file and add it to the current directory
        var file = new File(parseInt(lineArr[0]));
        currentDirectory.addFile(file);
    }
    else if (lineArr[0] === 'dir') {
        // add the directory to the current directory
        var directoryAdd = new Directory(lineArr[1]);
        directoryStack.push(directoryAdd);
        currentDirectory.addFile(directoryAdd);
    }
};
for (var _i = 0, lines_1 = lines; _i < lines_1.length; _i++) {
    var line = lines_1[_i];
    _loop_1(line);
}
var totalSum = 0;
function recurseThroughTree(toplvlDirectory) {
    if (toplvlDirectory.isFile()) {
        totalSum += toplvlDirectory.calculateSize();
        return;
    }
    for (var _i = 0, _a = toplvlDirectory.children; _i < _a.length; _i++) {
        var directory = _a[_i];
        if (directory.calculateSize() <= 100000) {
            return recurseThroughTree(directory);
        }
    }
}
console.log(totalSum);
