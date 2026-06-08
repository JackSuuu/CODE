
class Person {
    constructor(name) {
        this.name = name;
    }

    get getName() {
        return this.name;
    }
}

// Name export
export function Performance() {}
export default { Person };  // if add default keyword, don't need {} in import file