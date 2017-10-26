//Languages such as Java provide the ability to declare methods private, meaning that they can only be called by other methods in the same class.

//JavaScript does not provide a native way of doing this, but it is possible to emulate private methods using closures. Private methods aren't just useful for restricting access to code: they also provide a powerful way of managing your global namespace, keeping non-essential methods from cluttering up the public interface to your code.


function counter () {
  var count = 0;
  var actuallyCount = function () {
    count++;
    return count;
  }
  return actuallyCount;
}

var a = counter()
a()
a()

function counter1 (init) {
  var count = init;
  var actuallyCount = function () {
    count++;
    return count;
  }
  return actuallyCount;
}

var b = counter1()
b()
b()



// counter.increment, counter.decrement and counter.value are closures that share the same environment. Thanks to JavaScript's lexical scoping, they each have access to the privateCounter variable and changeBy function.
var makeCounter = function () {
  var privateCounter = 0
  function changeBy (val) {
    privateCounter += val
  }
  return {
    increment: function () {
      changeBy(1)
    },
    decrement: function () {
      changeBy(-1)
    },
    value: function () {
      return privateCounter
    }
  }
}

var counter1 = makeCounter();
var counter2 = makeCounter();
alert(counter1.value()); /* Alerts 0 */
counter1.increment();
counter1.increment();
alert(counter1.value()); /* Alerts 2 */
counter1.decrement();
alert(counter1.value()); /* Alerts 1 */
alert(counter2.value()); /* Alerts 0 */
