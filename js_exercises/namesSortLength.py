var people = [
    'Dom',
    'Lyn',
    'Kirk',
    'Autumn',
    'Trista',
    'Jesslyn',
    'Kevin',
    'John',
    'Eli',
    'Juan',
    'Robert',
    'Keyur',
    'Jason',
    'Che',
    'Ben'
]


people1 = []

function compare(a, b) {
    if (a.length < b.length) {
        return -1
    }
    if (a.length > b.length) {
        return 1
    }
    // a must be equal to b
    return 0
}


people.sort(compare(a, b) {
    return a - b
})
console.log(people)
