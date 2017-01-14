def draw_stars(arr):
    for val in arr:
        stars = ""
        if type(val) is int:
            for count in range(0,val):
                stars += "*"
            print stars
        elif type(val) is str:
            for count in range(0,len(val)):
                stars += val[0].lower()
            print stars



x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# x = [4,6,1,3,5,7,"yoman"]
draw_stars(x)
