function directions(...args) { 
    var [start, ...remaining] = args; // Extracts the first element as `start`, rest goes to `remaining`
    var [finish, ...stops] = remaining.reverse(); // Reverses remaining, extracts the last element as `finish`, rest as `stops`

    console.log(`drive through ${args.length} towns`);
    console.log(`start in ${start}`);
    console.log(`the destination is ${finish}`);
    console.log(`stopping ${stops.length} times in between`);
}

directions("Truckee", "Tahoe City", "Sunnyside", "Homewood", "Tahoma");
