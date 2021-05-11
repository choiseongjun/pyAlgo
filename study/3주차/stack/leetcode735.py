def asteroidCollision( asteroids):
    for i in range(len(asteroids)-1):
        if asteroids[i+1]-asteroids[i]:
            print(asteroids[i])





if __name__ == '__main__':
    asteroids = [5, 10, -5]
    asteroidCollision(asteroids)