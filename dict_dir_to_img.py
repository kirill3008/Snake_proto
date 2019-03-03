left = 'left'
up = 'up'
right = 'right'
down = 'down' 
#dir to part from prev, dir to next part 
dir_img = {
    (left,left):'hor.png',
    (right,right):'hor.png',
    (up,up):'wert.png',
    (down,down):'wert.png',
    (right,down):'left_down.png',
    (up,left):'left_down.png',
    (left,down):'right_down.png',
    (up,right):'right_down.png',
    (right,up):'left_up.png',
    (down,left):'left_up.png',
    (left,up):'right_up.png',
    (down,right):'right_up.png'
}
# direction to tail from prev part
tail_img = {
    left:'tail_left.png',
    right:'tail_right.png',
    up:'tail_up.png',
    down:'tail_down.png'
}
# direction to next part
head_img = {
    left:'head_right.png',
    right:'head_left.png',
    up:'head_down.png',
    down:'head_down.png'
}