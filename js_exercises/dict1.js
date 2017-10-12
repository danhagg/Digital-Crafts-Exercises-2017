var phonebookDict = {
  Alice: '703-493-1834',
  Bob: '857-384-1234',
  Elizabeth: '484-584-2923'
}

console.log(phonebookDict['Elizabeth'])

phonebookDict.kareem = '938-489-1234'
console.log(phonebookDict)

delete phonebookDict['Alice']
console.log(phonebookDict)

phonebookDict.Bob = 'xxx-xxx-xxxx'
console.log(phonebookDict)

for (var personName in phonebookDict) {
  var value = phonebookDict[personName]
  console.log(`${personName}: ${value}`)
}
