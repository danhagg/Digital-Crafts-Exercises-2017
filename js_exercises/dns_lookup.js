var readline = require('readline');
var dns = require('dns');
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
rl.question("Gimme a web address ", function(answer) {
  rl.lookup(rl, function (err, addresses, family) {
    return addresses;
  });
}
