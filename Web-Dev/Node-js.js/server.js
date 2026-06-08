const express = require('express')
const app = express()

app.use(express.static("public"))
app.use(express.urlencoded({ extended: true }))

// set up route
app.set('view engine', 'ejs')
app.use(logger)

app.get('/', (req, res) => {
    // console.log("Here")
    res.render('index', {
        text: "text in server"
    })
})

const userRouter = require('./routes/users')

app.use('/users', userRouter)

function logger(req, res, next) {
    console.log(req.originalUrl)
    next()
}

app.listen(3000, () => {
    console.log("App listening on port 3000")
})