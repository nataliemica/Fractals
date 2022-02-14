def mandelbrot(x,y,threshold):
    c = complex(x,y)
    z = complex(0,0)
    
    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 4:
            return i%20
        
    return (threshold - 1)%20