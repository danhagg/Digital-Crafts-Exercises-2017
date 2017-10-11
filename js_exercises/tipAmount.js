function tipAm (service, bill) {
  if (service === 'good') {
    var tip = bill * 0.2
  } else if (service === 'fair') {
    tip = bill * 0.15
  } else if (service === 'bad') {
    tip = bill * 0.1
  }
  console.log(tip)
  return tip
}

tipAm('good', 100)
