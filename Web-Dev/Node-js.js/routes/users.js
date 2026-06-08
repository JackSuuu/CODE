const express = require('express')
const router = express.Router()

// router always go /users at begining
router.get("/", (req, res) => {
    res.send("User List")
})

router.get('/new', (req, res) => {
    res.render("users/new", { firstName: "Jack"})
})

router.post("/", (req, res) => {
    const isValid = true
    if (isValid) {
        users.push({ firstName: req.body.firstName })
        res.redirect(`/users/${user.length - 1}`)
    } else {
        console.log("Error")
        res.render('users/new', { firstName: req.body.firstName })
    }
})

router.route(":/id").get((req, res) => {
    res.send(`Get user with id ${req.params.id}`)
}).put((req, res) => {
    res.send(`Update user with id ${req.params.id}`)
}).delete((req, res) => {
    res.send(`Delete user with id ${req.params.id}`)
})

router.get('/:id', (req, res) => {
    res.send(`Get user with id ${req.params.id}`)
})

router.put('/:id', (req, res) => {
    res.send(`Update user with id ${req.params.id}`)
})

router.delete('/:id', (req, res) => {
    res.send(`Delete user with id ${req.params.id}`)
})

const users = [{name: "Jack"}, {name: "Luly"}]
router.param("id", (req, res, next, id) => {
    req.user = users[id]
    // console.log(req.user)
    next()
})

module.exports = router