const invokeIf = (condition, fnTrue, fnFalse) => (condition) ? fnTrue() : fnFalse()  
const showWelcome = () => console.log("Welcome!!!")  
const showUnauthorized = () => console.log("Unauthorized!!!")  

invokeIf(false, showWelcome, showUnauthorized) // "Welcome" 
// invokeIf(true, showWelcome, showUnauthorized) // "Unauthorized"