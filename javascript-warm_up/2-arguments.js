#!/usr/bin/node

const args = process.argv;

const numberOfArguments = args.length - 2;

if (numberOfArguments === 0) {
  console.log("No argument");
} else if (numberOfArguments === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}