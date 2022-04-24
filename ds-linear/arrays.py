
expenses = {"January": 2200,
            "February": 2350,
            "March": 2600,
            "April": 2130,
            "May": 2190}

# In february how may spend compared to January
Feb=expenses["February"]-expenses["January"]
print(Feb)
qtr = expenses["January"]+expenses["February"]+expenses["March"]
print(qtr)
