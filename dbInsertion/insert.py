import pymysql as sql
import random
from pymysql.err import Error
mydb = sql.connect(host="localhost",user="test",password="481526",db="bookSouls",autocommit=True)
cur = mydb.cursor()
numberOfTimes = 50
categoriesForQuickies = ['Inspire me','Spirituality','entrpreneurship ,health,personal finanace']
title = "Fugiat irure minim do commodo ex minim incididunt eiusmod magna ipsum sint ex magna qui."
content = """
Occaecat sit cillum ipsum duis labore. Aute cupidatat et occaecat sit consequat enim consequat consequat minim ea. Voluptate minim irure deserunt irure consectetur esse velit anim. Nostrud irure commodo ea anim labore ad officia mollit id exercitation minim ut excepteur. Et magna in laborum do. Velit duis do qui nisi nisi labore irure pariatur laboris dolore qui dolor. Laboris aliqua ullamco esse veniam nisi nisi reprehenderit.

Do laboris tempor tempor est. Sint officia velit cupidatat quis pariatur dolor laboris pariatur voluptate do officia. Enim adipisicing pariatur et nostrud id et proident Lorem aute nostrud cupidatat eiusmod Lorem velit. Ipsum ullamco laborum cillum aute aute dolore esse.

Cillum commodo nulla voluptate mollit. Laborum commodo amet dolor eu laboris et est labore consectetur voluptate. Incididunt quis amet consectetur cupidatat ad esse dolor eu dolore. Sint sit sint consequat pariatur culpa minim.

Elit non ullamco dolor elit est fugiat commodo qui Lorem. Tempor aliquip consectetur et consectetur id. Cupidatat non tempor officia velit est ad aliquip commodo. Quis veniam ad consequat occaecat duis. Ex eiusmod ullamco id aliquip deserunt voluptate ad dolore culpa aliqua velit aliqua.

Deserunt irure culpa aute mollit do anim anim labore exercitation. Id exercitation magna ea id irure exercitation aliqua ullamco nisi. Laborum commodo elit irure enim exercitation nulla nisi. Consequat aute labore qui ad non aliquip commodo voluptate. Culpa tempor excepteur cupidatat esse esse sit ad. Eiusmod reprehenderit laborum aliquip tempor laboris pariatur duis fugiat sit nostrud duis eiusmod.

Ex ad do sint aliqua. Mollit cupidatat aliquip exercitation enim ad culpa incididunt mollit sit labore commodo adipisicing eu consectetur. Eu dolor qui pariatur reprehenderit veniam anim est tempor ut irure velit aliquip exercitation deserunt.
"""

try:
    for i in range(numberOfTimes):
        indexForQuickies = random.randint(0,len(categoriesForQuickies)-1) 
        sql = 'insert into quickies values ('+str(i)+',"'+categoriesForQuickies[indexForQuickies]+'","'+title+'",current_date()'+',"'+content+'");'
        cur.execute(sql)

except Error as e:
    print(e)
finally:
    print("it is finished")    
