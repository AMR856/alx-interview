#!/usr/bin/node
const process = require('process');
const request = require('request');

function printCharacters (characters, index) {
  request(characters[index], function (error, _, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
const url = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = url.concat('', process.argv[2]);
request(fullUrl, function (error, _, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
