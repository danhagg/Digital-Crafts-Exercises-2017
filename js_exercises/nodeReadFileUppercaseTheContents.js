var readline = require('readline');
var fs = require('fs');
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
rl.question("Gimme a filname ", function(answer) {
  fs.readFile(answer, function (error, buffer) {
    if (error) {
      console.error(error.message);
      return;
    }
    var contents = buffer.toString();
    var backwards = contents.toLowerCase();
    fs.writeFile(answer, backwards, function (error) {
      if (error) {
        console.error(error.message);
        return;
      }
      console.log('File Save: ', answer);
    });
  });
  rl.close();
})
