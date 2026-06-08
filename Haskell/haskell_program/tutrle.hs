
import Turtle

-- Function to draw a circle
drawCircle :: Double -> IO ()
drawCircle radius = do
    pendown
    circle radius 360
    penup

main :: IO ()
main = do
    openField

    -- Set up drawing settings (e.g., color, line width) here
    let bodyColor = blue
    let eyeColor = white

    -- Draw Doraemon's face
    setheading 0
    fillcolor bodyColor
    beginfill
    drawCircle 60
    endfill

    -- Draw Doraemon's eyes
    penup
    goto (20, 100)
    fillcolor eyeColor
    beginfill
    drawCircle 10
    endfill

    penup
    goto (-20, 100)
    fillcolor eyeColor
    beginfill
    drawCircle 10
    endfill

    -- Draw Doraemon's nose
    penup
    goto (0, 70)
    fillcolor bodyColor
    beginfill
    drawCircle 6
    endfill

    -- Draw Doraemon's mouth
    penup
    goto (20, 55)
    pendown
    setheading (-60)
    circle 20 120
    penup
    goto (20, 55)
    pendown
    setheading (-120)
    circle (-20) 120

    penup
    goto (0, 0)

    -- Close the drawing window
    closeField
